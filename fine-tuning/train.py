"""
train.py — Fine-tuning script for smart contract generation
Model  : Qwen/Qwen2.5-Coder-1.5B-Instruct
Method : LoRA via Unsloth + TRL SFTTrainer
Dataset: finetuning_dataset/dataset.jsonl  (produced by create_finetuning_dataset.py)
"""

import os
import json
import random
import argparse
from datetime import datetime
from typing import List, Dict, Optional

import torch
from datasets import Dataset
from transformers import TrainingArguments
from trl import SFTTrainer
from unsloth import FastLanguageModel

# ── Configuration ──────────────────────────────────────────────────────────────

MODEL_NAME      = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
MAX_SEQ_LENGTH  = 4096
LOAD_IN_4BIT    = True          # QLoRA — keeps VRAM low on ≤16 GB GPUs

# LoRA
LORA_R          = 16
LORA_ALPHA      = 16
LORA_DROPOUT    = 0.05
TARGET_MODULES  = ["q_proj", "k_proj", "v_proj", "o_proj",
                   "gate_proj", "up_proj", "down_proj"]  # include MLP layers

# Training
BATCH_SIZE              = 2
GRADIENT_ACCUMULATION   = 4     # effective batch = 8
NUM_EPOCHS              = 3
LEARNING_RATE           = 2e-4
WARMUP_STEPS            = 50
LOGGING_STEPS           = 10
SAVE_STEPS              = 100
VAL_SPLIT               = 0.05  # 5% held out for validation

# Paths
DATASET_PATH    = "finetuning_dataset/dataset.jsonl"
OUTPUT_DIR      = "outputs"
MODEL_SAVE_DIR  = "smart-contract-model"

# Chat template tokens (ChatML — matches Qwen2.5-Instruct)
BOS = "<|im_start|>"
EOS = "<|im_end|>"

# ── Prompt formatter ───────────────────────────────────────────────────────────

def format_prompt(example: Dict) -> Dict[str, str]:
    """
    Convert a dataset example to a single training string using the ChatML
    format that Qwen2.5-Instruct was trained with.

    Structure:
        <|im_start|>system
        {instruction}<|im_end|>
        <|im_start|>user
        {input}<|im_end|>
        <|im_start|>assistant
        {output}<|im_end|>
    """
    text = (
        f"{BOS}system\n{example['instruction']}{EOS}\n"
        f"{BOS}user\n{example['input']}{EOS}\n"
        f"{BOS}assistant\n{example['output']}{EOS}"
    )
    return {"text": text}

# ── Data loading ───────────────────────────────────────────────────────────────

def load_dataset(path: str, val_split: float = VAL_SPLIT,
                 seed: int = 42) -> tuple[Dataset, Optional[Dataset]]:
    """
    Load JSONL dataset, format prompts, and split into train / validation.
    """
    print(f"[DATA] Loading dataset from {path} ...")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Run create_finetuning_dataset.py first."
        )

    with open(path, 'r', encoding='utf-8') as f:
        raw = [json.loads(line) for line in f if line.strip()]

    print(f"[DATA] {len(raw)} total examples loaded")

    # Log task distribution
    task_counts: Dict[str, int] = {}
    for ex in raw:
        t = ex.get("task_type", "unknown")
        task_counts[t] = task_counts.get(t, 0) + 1
    for task, count in task_counts.items():
        print(f"  {task:30} {count:5} ({count/len(raw)*100:.1f}%)")

    # Format prompts
    formatted = [format_prompt(ex) for ex in raw]

    # Filter out examples that exceed max sequence length
    # (rough token estimate: ~3 chars per token)
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
    else:
        print(f"[DATA] Train: {len(formatted)}  |  No validation split\n")
        return Dataset.from_list(formatted), None

# ── Model loading ──────────────────────────────────────────────────────────────

def load_model():
    """Load base model and attach LoRA adapters via Unsloth."""
    print(f"[MODEL] Loading {MODEL_NAME} ...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name     = MODEL_NAME,
        max_seq_length = MAX_SEQ_LENGTH,
        dtype          = None,          # auto-detect (bf16 on Ampere+, fp16 otherwise)
        load_in_4bit   = LOAD_IN_4BIT,
    )

    print("[MODEL] Attaching LoRA adapters ...")
    model = FastLanguageModel.get_peft_model(
        model,
        r                   = LORA_R,
        target_modules      = TARGET_MODULES,
        lora_alpha          = LORA_ALPHA,
        lora_dropout        = LORA_DROPOUT,
        bias                = "none",
        use_gradient_checkpointing = "unsloth",  # Unsloth's optimised checkpointing
        random_state        = 42,
    )

    # Print trainable parameter count
    total_params     = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"[MODEL] Trainable parameters: {trainable_params:,} / {total_params:,} "
          f"({100 * trainable_params / total_params:.2f}%)\n")

    return model, tokenizer

# ── Training ───────────────────────────────────────────────────────────────────

def build_trainer(model, tokenizer, train_dataset: Dataset,
                  val_dataset: Optional[Dataset]) -> SFTTrainer:
    """Construct the SFTTrainer."""

    # Use bf16 if available (Ampere/Ada GPUs), otherwise fp16
    use_bf16 = torch.cuda.is_bf16_supported()
    use_fp16 = not use_bf16

    run_name = f"sc-finetune-{datetime.now().strftime('%Y%m%d_%H%M')}"

    training_args = TrainingArguments(
        output_dir                  = OUTPUT_DIR,
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
        save_total_limit            = 3,        # keep last 3 checkpoints only
        evaluation_strategy         = "steps" if val_dataset else "no",
        eval_steps                  = SAVE_STEPS if val_dataset else None,
        load_best_model_at_end      = bool(val_dataset),
        optim                       = "adamw_8bit",
        lr_scheduler_type           = "cosine",
        report_to                   = "none",   # set to "wandb" if you use W&B
        seed                        = 42,
    )

    trainer = SFTTrainer(
        model               = model,
        tokenizer           = tokenizer,
        train_dataset       = train_dataset,
        eval_dataset        = val_dataset,
        dataset_text_field  = "text",
        max_seq_length      = MAX_SEQ_LENGTH,
        packing             = False,    # disable packing — contracts vary greatly in length
        args                = training_args,
    )

    return trainer

# ── Entry point ────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fine-tune smart contract generation model")
    parser.add_argument("--dataset",    default=DATASET_PATH, help="Path to dataset.jsonl")
    parser.add_argument("--output-dir", default=OUTPUT_DIR,   help="Checkpoint output directory")
    parser.add_argument("--save-dir",   default=MODEL_SAVE_DIR, help="Final model save directory")
    parser.add_argument("--epochs",     type=int,   default=NUM_EPOCHS,    help="Training epochs")
    parser.add_argument("--lr",         type=float, default=LEARNING_RATE, help="Learning rate")
    parser.add_argument("--no-val",     action="store_true", help="Skip validation split")
    return parser.parse_args()


def main():
    args = parse_args()

    print("=" * 70)
    print(" " * 15 + "SMART CONTRACT MODEL FINE-TUNING")
    print("=" * 70)
    print(f"  Model       : {MODEL_NAME}")
    print(f"  Dataset     : {args.dataset}")
    print(f"  Epochs      : {args.epochs}")
    print(f"  LR          : {args.lr}")
    print(f"  LoRA r / α  : {LORA_R} / {LORA_ALPHA}")
    print(f"  4-bit QLoRA : {LOAD_IN_4BIT}")
    print(f"  Output      : {args.output_dir}")
    print("=" * 70 + "\n")

    # ── 1. Load dataset ────────────────────────────────────────────────────────
    val_split = 0.0 if args.no_val else VAL_SPLIT
    train_dataset, val_dataset = load_dataset(args.dataset, val_split=val_split)

    # ── 2. Load model ──────────────────────────────────────────────────────────
    model, tokenizer = load_model()

    # ── 3. Build trainer ───────────────────────────────────────────────────────
    trainer = build_trainer(model, tokenizer, train_dataset, val_dataset)

    # ── 4. Train ───────────────────────────────────────────────────────────────
    print("[TRAIN] Starting training ...\n")
    train_result = trainer.train()

    print("\n[TRAIN] Training complete.")
    print(f"  Training loss     : {train_result.training_loss:.4f}")
    print(f"  Total steps       : {train_result.global_step}")
    print(f"  Total time        : {train_result.metrics.get('train_runtime', 0):.1f}s")

    # ── 5. Save final model ────────────────────────────────────────────────────
    print(f"\n[SAVE] Saving model to {args.save_dir} ...")
    model.save_pretrained(args.save_dir)
    tokenizer.save_pretrained(args.save_dir)
    print(f"[SAVE] Done.\n")

    print("=" * 70)
    print("[SUCCESS] Fine-tuning complete!")
    print(f"          Model saved to : {args.save_dir}/")
    print(f"          Checkpoints in : {args.output_dir}/")
    print("=" * 70)


if __name__ == "__main__":
    main()
