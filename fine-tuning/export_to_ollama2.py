"""
export_to_ollama.py — Export fine-tuned LoRA models to Ollama

Flow for each model:
  1. Load base model + LoRA adapter from FT-models/ via Unsloth
  2. Export merged model to GGUF (q4_k_m quantization by default)
  3. Write an Ollama Modelfile
  4. Register the model in Ollama via `ollama create`

Usage:
    # Export all three fine-tuned models
    python export_to_ollama.py

    # Export a specific model
    python export_to_ollama.py --model qwen
    python export_to_ollama.py --model granite
    python export_to_ollama.py --model llama

    # Use a different quantization
    python export_to_ollama.py --quant q8_0

Requirements:
    pip install unsloth
    ollama must be installed and running (https://ollama.com)
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List

from unsloth import FastLanguageModel

# ── Model registry (must match FT_model_creation.py) ─────────────────────────

MODELS = {
    "qwen": {
        "hf_id":      "Qwen/Qwen2.5-Coder-0.5B-Instruct",
        "short_name": "Qwen2.5-Coder-0.5B",
        "ollama_ft":  "qwen2.5-coder-0.5b-ft",   # ollama model name for FT version
        "ollama_base":"qwen2.5-coder:0.5b",        # ollama tag for base version
    },
    "granite": {
        "hf_id":      "ibm-granite/granite-4.0-1b",
        "short_name": "Granite-4.0-1B",
        "ollama_ft":  "granite-4.0-1b-ft",
        "ollama_base":"granite4.1:1b",
    },
    "llama": {
        "hf_id":      "meta-llama/Llama-3.2-1B-Instruct",
        "short_name": "Llama-3.2-1B",
        "ollama_ft":  "llama3.2-1b-ft",
        "ollama_base":"llama3.2:1b",
    },
}

# ── Configuration ─────────────────────────────────────────────────────────────

MAX_SEQ_LENGTH   = 4096
LOAD_IN_4BIT     = True
DEFAULT_QUANT    = "q4_k_m"   # recommended: good quality/size balance
                               # alternatives: q8_0, q5_k_m, f16, q2_k

FT_MODELS_DIR    = "FT-models"    # where FT_model_creation.py saved the adapters
GGUF_EXPORT_DIR  = "gguf-exports" # where GGUF files will be written
MODELFILE_DIR    = "modelfiles"   # where Ollama Modelfiles will be written

# System prompt — same as used during fine-tuning generation task
SYSTEM_PROMPT = (
    "You are an expert Solidity developer. Generate complete, production-ready "
    "smart contracts. Use Solidity ^0.8.x. Focus on correctness, security, and "
    "clarity. Optimize for gas efficiency."
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def check_ollama() -> bool:
    """Check that Ollama is installed and the daemon is running."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def run_ollama_create(model_name: str, modelfile_path: str) -> bool:
    """Run `ollama create <model_name> -f <modelfile>`. Returns True on success."""
    print(f"  [ollama] Running: ollama create {model_name} -f {modelfile_path}")
    result = subprocess.run(
        ["ollama", "create", model_name, "-f", modelfile_path],
        capture_output=False,   # stream output directly to terminal
        text=True,
    )
    return result.returncode == 0


def write_modelfile(
    modelfile_path: str,
    gguf_path: str,
    system_prompt: str,
) -> None:
    """Write an Ollama Modelfile pointing to the exported GGUF."""
    # Ollama requires an absolute path in FROM when loading a local GGUF
    abs_gguf = str(Path(gguf_path).resolve())
    content = (
        f"FROM {abs_gguf}\n"
        f"\n"
        f"SYSTEM \"\"\"\n{system_prompt}\n\"\"\"\n"
        f"\n"
        f"PARAMETER temperature 0.1\n"
        f"PARAMETER top_p 0.9\n"
        f"PARAMETER stop \"<|im_end|>\"\n"
        f"PARAMETER stop \"<|eot_id|>\"\n"
        f"PARAMETER stop \"<|end_of_text|>\"\n"
    )
    Path(modelfile_path).parent.mkdir(parents=True, exist_ok=True)
    with open(modelfile_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [modelfile] Written: {modelfile_path}")


# ── Core export pipeline ──────────────────────────────────────────────────────

def export_model(model_key: str, quant: str) -> None:
    """
    Full export pipeline for one fine-tuned model:
      1. Load base model + LoRA adapter
      2. Save merged GGUF
      3. Write Modelfile
      4. Register in Ollama
    """
    cfg        = MODELS[model_key]
    hf_id      = cfg["hf_id"]
    short_name = cfg["short_name"]
    ollama_ft  = cfg["ollama_ft"]

    adapter_dir  = str(Path(FT_MODELS_DIR) / f"FT-{short_name}")
    gguf_out_dir = str(Path(GGUF_EXPORT_DIR) / f"FT-{short_name}")
    modelfile_path = str(Path(MODELFILE_DIR) / f"{ollama_ft}.Modelfile")

    print("\n" + "=" * 65)
    print(f"  Model       : {short_name}")
    print(f"  Adapter dir : {adapter_dir}")
    print(f"  GGUF dir    : {gguf_out_dir}")
    print(f"  Quantize    : {quant}")
    print(f"  Ollama name : {ollama_ft}")
    print("=" * 65 + "\n")

    # ── 1. Verify adapter exists ──────────────────────────────────────────────
    if not Path(adapter_dir).exists():
        print(f"  [ERROR] Adapter directory not found: {adapter_dir}")
        print(f"          Run FT_model_creation.py --model {model_key} first.")
        return

    # ── 2. Load base model + LoRA adapter via Unsloth ────────────────────────
    print(f"  [load] Loading base model: {hf_id}")
    print(f"  [load] Applying adapter from: {adapter_dir}")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name     = adapter_dir,   # Unsloth reads adapter_config.json here
        max_seq_length = MAX_SEQ_LENGTH,
        dtype          = None,
        load_in_4bit   = LOAD_IN_4BIT,
    )

    # ── 3. Export to GGUF ─────────────────────────────────────────────────────
    print(f"\n  [export] Saving GGUF ({quant}) to: {gguf_out_dir}")
    Path(gguf_out_dir).mkdir(parents=True, exist_ok=True)
    model.save_pretrained_gguf(
        gguf_out_dir,
        tokenizer,
        quantization_method=quant,
    )

    # Unsloth names the output file as <dir>/<model_name>-{quant}.gguf
    # Find the actual GGUF file written
    gguf_files = list(Path(gguf_out_dir).glob("*.gguf"))
    if not gguf_files:
        print(f"  [ERROR] No GGUF file found in {gguf_out_dir} after export.")
        return
    gguf_path = str(gguf_files[0])
    print(f"  [export] GGUF written: {gguf_path}")

    # ── 4. Write Modelfile ────────────────────────────────────────────────────
    write_modelfile(modelfile_path, gguf_path, SYSTEM_PROMPT)

    # ── 5. Register in Ollama ─────────────────────────────────────────────────
    print(f"\n  [ollama] Registering model as '{ollama_ft}' ...")
    success = run_ollama_create(ollama_ft, modelfile_path)

    if success:
        print(f"\n  [OK] '{ollama_ft}' is now available in Ollama.")
        print(f"       Test with: ollama run {ollama_ft}")
        print(f"       Base model: ollama run {cfg['ollama_base']}")
    else:
        print(f"\n  [ERROR] ollama create failed for {ollama_ft}.")
        print(f"          You can retry manually:")
        print(f"          ollama create {ollama_ft} -f {modelfile_path}")

    # ── 6. Free memory before next model ─────────────────────────────────────
    import torch
    del model, tokenizer
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("=" * 65 + "\n")


# ── Entry point ───────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export fine-tuned smart contract models to Ollama"
    )
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()) + ["all"],
        default="all",
        help="Which model to export. 'all' exports all three (default).",
    )
    parser.add_argument(
        "--quant",
        default=DEFAULT_QUANT,
        choices=["q4_k_m", "q5_k_m", "q8_0", "f16", "q2_k"],
        help=f"GGUF quantization method (default: {DEFAULT_QUANT}).",
    )
    parser.add_argument(
        "--skip-ollama",
        action="store_true",
        help="Export GGUF and write Modelfile but skip the ollama create step.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("=" * 65)
    print(" " * 15 + "EXPORT FINE-TUNED MODELS TO OLLAMA")
    print("=" * 65)

    # Check Ollama is available unless skipping
    if not args.skip_ollama:
        if not check_ollama():
            print("\n[ERROR] Ollama is not running or not installed.")
            print("        Install from https://ollama.com, start the daemon,")
            print("        then re-run. Or use --skip-ollama to export GGUF only.")
            sys.exit(1)
        print("  [OK] Ollama daemon is running.")

    targets: List[str] = (
        list(MODELS.keys()) if args.model == "all" else [args.model]
    )
    print(f"  Models to export : {', '.join(targets)}")
    print(f"  Quantization     : {args.quant}")
    print(f"  Skip ollama step : {args.skip_ollama}")
    print("=" * 65)

    for model_key in targets:
        export_model(model_key, args.quant)

    print("=" * 65)
    print(f"[DONE] Export complete for: {', '.join(targets)}")
    if not args.skip_ollama:
        print()
        print("  Registered Ollama models:")
        for k in targets:
            print(f"    FT  : ollama run {MODELS[k]['ollama_ft']}")
            print(f"    Base: ollama run {MODELS[k]['ollama_base']}")
    print("=" * 65)


if __name__ == "__main__":
    main()
