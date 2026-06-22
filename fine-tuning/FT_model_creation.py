"""
FT_model_creation.py — Fine-tuning script for smart contract generation
Models  : Qwen/Qwen2.5-Coder-0.5B-Instruct    (Qwen ChatML template)
          ibm-granite/granite-4.0-1b            (Granite 4.0 role template)
          meta-llama/Llama-3.2-1B-Instruct      (Llama-3 header template)
Method  : LoRA via Unsloth + TRL SFTTrainer
Dataset : FT_dataset/dataset.jsonl  (produced by create_finetuning_dataset.py)

Usage:
    # Fine-tune all three models sequentially
    python FT_model_creation.py

    # Fine-tune a specific model only
    python FT_model_creation.py --model qwen
    python FT_model_creation.py --model granite
    python FT_model_creation.py --model llama
"""

import os
import json
import random
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from unsloth import FastLanguageModel
import torch
from datasets import Dataset
from transformers import TrainingArguments
from trl import SFTTrainer, SFTConfig

# ── Model registry ─────────────────────────────────────────────────────────────
#
# chat_template values:
#   "qwen"     — <|im_start|>/<|im_end|>                    (Qwen2.5-Instruct)
#   "granite4" — <|start_of_role|>/<|end_of_role|>/<|end_of_text|>  (Granite 4.0)
#   "llama3"   — <|begin_of_text|> / header_id / eot_id     (Llama 3.x)
#
MODELS = {
    "qwen": {
        "hf_id":         "Qwen/Qwen2.5-Coder-0.5B-Instruct",
        "short_name":    "Qwen2.5-Coder-0.5B",
        "chat_template": "qwen",
    },
    "granite": {
        "hf_id":         "ibm-granite/granite-4.0-1b",
        "short_name":    "Granite-4.0-1B",
        "chat_template": "granite4",
    },
    "llama": {
        "hf_id":         "meta-llama/Llama-3.2-1B-Instruct",
        "short_name":    "Llama-3.2-1B",
        "chat_template": "llama3",
    },
}

# ── Shared training configuration ──────────────────────────────────────────────

MAX_SEQ_LENGTH  = 4096
LOAD_IN_4BIT    = True       # QLoRA — keeps VRAM low on ≤16 GB GPUs

# LoRA
LORA_R          = 16
LORA_ALPHA      = 16
LORA_DROPOUT    = 0
TARGET_MODULES  = ["q_proj", "k_proj", "v_proj", "o_proj",
                   "gate_proj", "up_proj", "down_proj"]

# Training
BATCH_SIZE              = 2
GRADIENT_ACCUMULATION   = 4     # effective batch = 8
NUM_EPOCHS              = 3
LEARNING_RATE           = 2e-4
WARMUP_STEPS            = 50
LOGGING_STEPS           = 10
SAVE_STEPS              = 100
VAL_SPLIT               = 0.05  # 5 % held out for validation

# Paths
DATASET_PATH = "FT_dataset/dataset.jsonl"


# ── Chat template formatters ───────────────────────────────────────────────────

def format_qwen(example: Dict) -> Dict[str, str]:
    """
    Qwen ChatML format — used by Qwen2.5-Coder-0.5B-Instruct.

    Structure:
        <|im_start|>system
        {instruction}<|im_end|>
        <|im_start|>user
        {input}<|im_end|>
        <|im_start|>assistant
        {output}<|im_end|>
    """
    text = (
        f"<|im_start|>system\n{example['instruction']}<|im_end|>\n"
        f"<|im_start|>user\n{example['input']}<|im_end|>\n"
        f"<|im_start|>assistant\n{example['output']}<|im_end|>"
    )
    return {"text": text}


def format_granite4(example: Dict) -> Dict[str, str]:
    """
    Granite 4.0 role format — used by ibm-granite/granite-4.0-1b.

    Verified from official model card expected output:
        <|start_of_role|>system<|end_of_role|>{instruction}<|end_of_text|>
        <|start_of_role|>user<|end_of_role|>{input}<|end_of_text|>
        <|start_of_role|>assistant<|end_of_role|>{output}<|end_of_text|>

    Note: this is NOT ChatML — Granite 4.0 uses its own distinct role tokens.
    """
    text = (
        f"<|start_of_role|>system<|end_of_role|>{example['instruction']}<|end_of_text|>"
        f"<|start_of_role|>user<|end_of_role|>{example['input']}<|end_of_text|>"
        f"<|start_of_role|>assistant<|end_of_role|>{example['output']}<|end_of_text|>"
    )
    return {"text": text}


def format_llama3(example: Dict) -> Dict[str, str]:
    """
    Llama-3 header format — used by Llama-3.2-1B-Instruct (and all Llama 3.x).

    Structure:
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        {instruction}<|eot_id|>
        <|start_header_id|>user<|end_header_id|>
        {input}<|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        {output}<|eot_id|>
    """
    text = (
        "<|begin_of_text|>"
        "<|start_header_id|>system<|end_header_id|>\n"
        f"{example['instruction']}<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n"
        f"{example['input']}<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n"
        f"{example['output']}<|eot_id|>"
    )
    return {"text": text}


FORMATTERS = {
    "qwen":     format_qwen,
    "granite4": format_granite4,
    "llama3":   format_llama3,
}


# ── Data loading ───────────────────────────────────────────────────────────────

def load_dataset_split(
    path: str,
    formatter,
    val_split: float = VAL_SPLIT,
    seed: int = 42,
) -> Tuple[Dataset, Optional[Dataset]]:
    """
    Load JSONL dataset, apply the model-specific chat template formatter,
    filter oversized examples, shuffle, and split into train / validation.
    """
    print(f"[DATA] Loading dataset from {path} ...")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Run create_finetuning_dataset.py first."
        )

    with open(path, "r", encoding="utf-8") as f:
        raw = [json.loads(line) for line in f if line.strip()]
    print(f"[DATA] {len(raw)} total examples loaded")

    # Log task distribution
    task_counts: Dict[str, int] = {}
    for ex in raw:
        t = ex.get("task_type", "unknown")
        task_counts[t] = task_counts.get(t, 0) + 1
    for task, count in sorted(task_counts.items()):
        print(f"  {task:30} {count:5d} ({count / len(raw) * 100:.1f}%)")

    # Apply formatter
    formatted = [formatter(ex) for ex in raw]

    # Filter examples that would exceed max sequence length
    # (rough estimate: ~3 chars per token)
    char_limit = MAX_SEQ_LENGTH * 3
    before = len(formatted)
    formatted = [ex for ex in formatted if len(ex["text"]) <= char_limit]
    dropped = before - len(formatted)
    if dropped:
        print(f"[DATA] Dropped {dropped} examples exceeding ~{MAX_SEQ_LENGTH} tokens")

    # Shuffle and split
    random.seed(seed)
    random.shuffle(formatted)

    if val_split > 0 and len(formatted) > 20:
        val_size  = max(1, int(len(formatted) * val_split))
        train_raw = formatted[val_size:]
        val_raw   = formatted[:val_size]
        print(f"[DATA] Train: {len(train_raw)}  |  Validation: {len(val_raw)}\n")
        return Dataset.from_list(train_raw), Dataset.from_list(val_raw)

    print(f"[DATA] Train: {len(formatted)}  |  No validation split\n")
    return Dataset.from_list(formatted), None


# ── Model loading ──────────────────────────────────────────────────────────────

def load_model(hf_id: str):
    """Load base model and attach LoRA adapters via Unsloth."""
    print(f"[MODEL] Loading {hf_id} ...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name     = hf_id,
        max_seq_length = MAX_SEQ_LENGTH,
        dtype          = None,      # auto-detect: bf16 on Ampere+, fp16 otherwise
        load_in_4bit   = LOAD_IN_4BIT,
    )

    print("[MODEL] Attaching LoRA adapters ...")
    model = FastLanguageModel.get_peft_model(
        model,
        r                          = LORA_R,
        target_modules             = TARGET_MODULES,
        lora_alpha                 = LORA_ALPHA,
        lora_dropout               = LORA_DROPOUT,
        bias                       = "none",
        use_gradient_checkpointing = "unsloth",
        random_state               = 42,
    )

    total     = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"[MODEL] Trainable params: {trainable:,} / {total:,} "
          f"({100 * trainable / total:.2f}%)\n")

    return model, tokenizer


# ── Trainer construction ───────────────────────────────────────────────────────

# Per-model correct EOS tokens (must exist in their vocab)
EOS_TOKENS = {
    "qwen":     "<|im_end|>",       # Qwen ChatML — this is the real turn-end token
    "granite4": "<|end_of_text|>",  # Granite 4.0
    "llama3":   "<|eot_id|>",       # Llama 3.x
}

def build_trainer(
    model,
    tokenizer,
    train_dataset: Dataset,
    val_dataset: Optional[Dataset],
    checkpoint_dir: str,
    chat_template: str,
) -> SFTTrainer:

    use_bf16 = torch.cuda.is_bf16_supported()
    use_fp16 = not use_bf16
    run_name = f"sc-finetune-{datetime.now().strftime('%Y%m%d_%H%M')}"

    eos = EOS_TOKENS[chat_template]
    tokenizer.eos_token = eos
    tokenizer.pad_token = eos

    # Pre-tokenize datasets — required when skip_prepare_dataset=True
    def tokenize(batch):
        out = tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_SEQ_LENGTH,
            padding=False,
        )
        out["labels"] = out["input_ids"].copy()
        return out

    train_dataset = train_dataset.map(
        tokenize,
        batched=True,
        remove_columns=["text"],
        desc="Tokenizing train dataset",
    )
    if val_dataset is not None:
        val_dataset = val_dataset.map(
            tokenize,
            batched=True,
            remove_columns=["text"],
            desc="Tokenizing val dataset",
        )

    training_args = SFTConfig(
        output_dir                  = checkpoint_dir,
        run_name                    = run_name,
        per_device_train_batch_size = BATCH_SIZE,
        gradient_accumulation_steps = GRADIENT_ACCUMULATION,
        num_train_epochs            = NUM_EPOCHS,
        learning_rate               = LEARNING_RATE,
        warmup_steps                = WARMUP_STEPS,
        bf16                        = use_bf16,
        fp16                        = use_fp16,
        logging_steps               = LOGGING_STEPS,
        save_steps                  = SAVE_STEPS,
        save_total_limit            = 3,
        eval_strategy               = "steps" if val_dataset else "no",
        eval_steps                  = SAVE_STEPS if val_dataset else None,
        load_best_model_at_end      = bool(val_dataset),
        optim                       = "adamw_8bit",
        lr_scheduler_type           = "cosine",
        report_to                   = "none",
        seed                        = 42,
        max_length                  = MAX_SEQ_LENGTH,
        packing                     = False,
        dataset_text_field          = "text",
        dataset_kwargs              = {"skip_prepare_dataset": True},
        eos_token                   = eos,
        remove_unused_columns       = False,   # ← keep all columns during collation
    )

    trainer = SFTTrainer(
        model            = model,
        processing_class = tokenizer,
        train_dataset    = train_dataset,
        eval_dataset     = val_dataset,
        args             = training_args,
    )

    return trainer


# ── Single-model pipeline ──────────────────────────────────────────────────────

def run_single_model(
    model_key: str,
    dataset_path: str,
    no_val: bool = False,
) -> None:
    """Run the full fine-tuning pipeline for one model."""

    cfg        = MODELS[model_key]
    hf_id      = cfg["hf_id"]
    short_name = cfg["short_name"]
    formatter  = FORMATTERS[cfg["chat_template"]]

    checkpoint_dir = f"checkpoints/FT-{short_name}"
    model_save_dir = f"FT-models/FT-{short_name}"

    print("\n" + "=" * 70)
    print(f"  Model       : {hf_id}")
    print(f"  Short name  : {short_name}")
    print(f"  Template    : {cfg['chat_template']}")
    print(f"  Dataset     : {dataset_path}")
    print(f"  Epochs      : {NUM_EPOCHS}")
    print(f"  LR          : {LEARNING_RATE}")
    print(f"  LoRA r / α  : {LORA_R} / {LORA_ALPHA}")
    print(f"  4-bit QLoRA : {LOAD_IN_4BIT}")
    print(f"  Checkpoints : {checkpoint_dir}")
    print(f"  Output      : {model_save_dir}")
    print("=" * 70 + "\n")

    # 1. Load dataset
    val_split = 0.0 if no_val else VAL_SPLIT
    train_dataset, val_dataset = load_dataset_split(
        dataset_path, formatter, val_split=val_split
    )

    # 2. Load model
    model, tokenizer = load_model(hf_id)

    # 3. Build trainer
    trainer = build_trainer(
        model, tokenizer, train_dataset, val_dataset, checkpoint_dir,
        chat_template = cfg["chat_template"],
    )

    # 4. Train
    print("[TRAIN] Starting training ...\n")
    result = trainer.train()
    print("\n[TRAIN] Training complete.")
    print(f"  Training loss : {result.training_loss:.4f}")
    print(f"  Total steps   : {result.global_step}")
    print(f"  Runtime       : {result.metrics.get('train_runtime', 0):.1f}s")

    # 5. Save
    print(f"\n[SAVE] Saving model to {model_save_dir} ...")
    model.save_pretrained(model_save_dir)
    tokenizer.save_pretrained(model_save_dir)
    print(f"[SAVE] Done.\n")

    print("=" * 70)
    print(f"[SUCCESS] {short_name} fine-tuning complete!")
    print(f"          Model saved to : {model_save_dir}/")
    print(f"          Checkpoints in : {checkpoint_dir}/")
    print("=" * 70 + "\n")

    # Free VRAM before loading the next model
    del model, tokenizer, trainer
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# ── Entry point ────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fine-tune smart contract generation models (Qwen, Granite, Llama)"
    )
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()) + ["all"],
        default="all",
        help="Which model to fine-tune. 'all' runs all three sequentially (default).",
    )
    parser.add_argument(
        "--dataset",
        default=DATASET_PATH,
        help="Path to dataset.jsonl",
    )
    parser.add_argument(
        "--no-val",
        action="store_true",
        help="Skip validation split",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("=" * 70)
    print(" " * 12 + "SMART CONTRACT MODEL FINE-TUNING")
    print("=" * 70)

    targets: List[str] = (
        list(MODELS.keys()) if args.model == "all" else [args.model]
    )
    print(f"  Models to fine-tune : {', '.join(targets)}")
    print(f"  Dataset             : {args.dataset}")
    print("=" * 70)

    for model_key in targets:
        run_single_model(
            model_key    = model_key,
            dataset_path = args.dataset,
            no_val       = args.no_val,
        )

    print("\n" + "=" * 70)
    print(f"[DONE] All {len(targets)} model(s) fine-tuned successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()