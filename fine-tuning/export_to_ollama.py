"""
export_to_ollama.py — Export fine-tuned LoRA adapters to Ollama (GGUF + Modelfile)

Loads each adapter saved by FT_model_creation.py from FT-models/FT-{short_name},
merges it into its base model, converts to GGUF via Unsloth, and registers the
result with Ollama. Unsloth auto-generates the Modelfile (incl. chat template).

Usage:
    python export_to_ollama.py                  # export all three models
    python export_to_ollama.py --model qwen     # export a single model
    python export_to_ollama.py --quant q8_0     # different quantization

Requires the Ollama CLI on PATH (https://ollama.com/download) to auto-register;
otherwise the script prints the manual `ollama create` command.
"""

import argparse
import shutil
import subprocess

from unsloth import FastLanguageModel

MAX_SEQ_LENGTH = 4096
LOAD_IN_4BIT   = True   # must match how each adapter was trained

MODELS = {
    "qwen":    {"short_name": "Qwen2.5-Coder-0.5B"},
    "granite": {"short_name": "Granite-4.0-1B"},
    "llama":   {"short_name": "Llama-3.2-1B"},
}


def export_one(model_key: str, quant: str) -> None:
    short_name  = MODELS[model_key]["short_name"]
    adapter_dir = f"FT-models/FT-{short_name}"
    gguf_dir    = f"ollama-models/{short_name}-GGUF"
    ollama_name = f"sc-{model_key}"   # name shown in `ollama list`

    print("\n" + "=" * 70)
    print(f"[EXPORT] {short_name}")
    print(f"  Adapter source : {adapter_dir}")
    print(f"  GGUF output    : {gguf_dir}")
    print(f"  Quantization   : {quant}")
    print("=" * 70)

    # 1. Reload the saved LoRA adapter on top of its base model
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name     = adapter_dir,
        max_seq_length = MAX_SEQ_LENGTH,
        dtype          = None,
        load_in_4bit   = LOAD_IN_4BIT,
    )

    # 2. Merge LoRA -> base, convert to GGUF (builds llama.cpp on first run,
    #    can take 5-10 min). Also writes gguf_dir/Modelfile automatically.
    model.save_pretrained_gguf(gguf_dir, tokenizer, quantization_method=quant)

    # 3. Register with Ollama, if the CLI is available
    modelfile = f"{gguf_dir}_gguf/Modelfile"
    if shutil.which("ollama"):
        print(f"[OLLAMA] Creating model '{ollama_name}' ...")
        subprocess.run(["ollama", "create", ollama_name, "-f", modelfile], check=True)
        print(f"[OLLAMA] Done. Run with: ollama run {ollama_name}")
    else:
        print("[OLLAMA] 'ollama' CLI not found on PATH. To finish manually, run:")
        print(f"    ollama create {ollama_name} -f {modelfile}")

    del model, tokenizer


def main():
    parser = argparse.ArgumentParser(description="Export fine-tuned models to Ollama")
    parser.add_argument("--model", choices=list(MODELS.keys()) + ["all"], default="all")
    parser.add_argument("--quant", default="q4_k_m",
                         help="GGUF quantization, e.g. q4_k_m, q5_k_m, q8_0, f16")
    args = parser.parse_args()

    targets = list(MODELS.keys()) if args.model == "all" else [args.model]
    for key in targets:
        export_one(key, args.quant)


if __name__ == "__main__":
    main()