"""
Fine-tuning script for smart contract generation.
Models  : Qwen/Qwen2.5-Coder-0.5B-Instruct    (Qwen ChatML template)
          ibm-granite/granite-4.0-1b            (Granite 4.0 role template)
          meta-llama/Llama-3.2-1B-Instruct      (Llama-3 header template)
          google/gemma-3-1b-it
Method  : LoRA via Unsloth + TRL SFTTrainer
Dataset : FT_dataset/dataset.jsonl

Usage:
    # Fine-tune all three models sequentially
    python FT_model_creation.py

    # Fine-tune a specific model only
    python FT_model_creation.py --model qwen
    python FT_model_creation.py --model granite
    python FT_model_creation.py --model llama
"""

import os, json, random, argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from unsloth import FastLanguageModel
import torch
from datasets import Dataset
from trl import SFTTrainer, SFTConfig

# ── Model registry ─────────────────────────────────────────────────────────────
MODELS = {
    "qwen":    {"hf_id": "Qwen/Qwen2.5-Coder-0.5B-Instruct", "short_name": "Qwen2.5-Coder-0.5B", "chat_template": "qwen"},
    "granite": {"hf_id": "ibm-granite/granite-4.0-1b",        "short_name": "Granite-4.0-1B",     "chat_template": "granite4"},
    "llama":   {"hf_id": "meta-llama/Llama-3.2-1B-Instruct",  "short_name": "Llama-3.2-1B",       "chat_template": "llama3"},
    "gemma3":  {"hf_id": "google/gemma-3-1b-it",              "short_name": "Gemma-3-1B",          "chat_template": "gemma3"},
}

# ── Hyperparameters ─────────────────────────────────────────────────────────────
MAX_SEQ_LENGTH = 4096
LOAD_IN_4BIT   = True   # QLoRA

LORA_R, LORA_ALPHA, LORA_DROPOUT = 16, 16, 0
TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

BATCH_SIZE, GRADIENT_ACCUMULATION = 2, 4   # effective batch = 8
NUM_EPOCHS, LEARNING_RATE         = 3, 2e-4
WARMUP_STEPS, LOGGING_STEPS, SAVE_STEPS = 50, 10, 100
VAL_SPLIT    = 0.05
DATASET_PATH = "FT_dataset/dataset.jsonl"

# ── Chat template formatters ────────────────────────────────────────────────────
def format_qwen(ex):
    """Qwen ChatML format"""
    return {"text": (
        f"<|im_start|>system\n{ex['instruction']}<|im_end|>\n"
        f"<|im_start|>user\n{ex['input']}<|im_end|>\n"
        f"<|im_start|>assistant\n{ex['output']}<|im_end|>"
    )}

def format_granite4(ex):
    """Granite 4.0 role format"""
    return {"text": (
        f"<|start_of_role|>system<|end_of_role|>{ex['instruction']}<|end_of_text|>"
        f"<|start_of_role|>user<|end_of_role|>{ex['input']}<|end_of_text|>"
        f"<|start_of_role|>assistant<|end_of_role|>{ex['output']}<|end_of_text|>"
    )}

def format_llama3(ex):
    """Llama-3 header format"""
    return {"text": (
        "<|begin_of_text|>"
        f"<|start_header_id|>system<|end_header_id|>\n{ex['instruction']}<|eot_id|>"
        f"<|start_header_id|>user<|end_header_id|>\n{ex['input']}<|eot_id|>"
        f"<|start_header_id|>assistant<|end_header_id|>\n{ex['output']}<|eot_id|>"
    )}

def format_gemma3(ex):
    # Gemma 3 embeds the system prompt inside the first user turn (no standalone system role)
    return {"text": (
        f"<start_of_turn>user\n{ex['instruction']}\n{ex['input']}<end_of_turn>\n"
        f"<start_of_turn>model\n{ex['output']}<end_of_turn>"
    )}

FORMATTERS = {"qwen": format_qwen, "granite4": format_granite4, "llama3": format_llama3, "gemma3": format_gemma3}

# EOS token per template (must exist in the model's vocab)
EOS_TOKENS = {"qwen": "<|im_end|>", "granite4": "<|end_of_text|>", "llama3": "<|eot_id|>", "gemma3": "<end_of_turn>"}


# ── Data loading ─────────────────────────────────────────────────────────────
def load_dataset_split(path, formatter, val_split=VAL_SPLIT, seed=42) -> Tuple[Dataset, Optional[Dataset]]:
    print(f"[DATA] Loading {path} ...")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}\nRun create_finetuning_dataset.py first.")

    with open(path, "r", encoding="utf-8") as f:
        raw = [json.loads(line) for line in f if line.strip()]
    print(f"[DATA] {len(raw)} examples loaded")

    # Task distribution
    counts: Dict[str, int] = {}
    for ex in raw:
        t = ex.get("task_type", "unknown")
        counts[t] = counts.get(t, 0) + 1
    for t, n in sorted(counts.items()):
        print(f"  {t:30} {n:5d} ({n/len(raw)*100:.1f}%)")

    # Format and filter (~3 chars/token rough estimate)
    formatted = [formatter(ex) for ex in raw]
    char_limit = MAX_SEQ_LENGTH * 3
    before = len(formatted)
    formatted = [ex for ex in formatted if len(ex["text"]) <= char_limit]
    if before - len(formatted):
        print(f"[DATA] Dropped {before - len(formatted)} oversized examples")

    random.seed(seed)
    random.shuffle(formatted)

    if val_split > 0 and len(formatted) > 20:
        val_size = max(1, int(len(formatted) * val_split))
        train, val = formatted[val_size:], formatted[:val_size]
        print(f"[DATA] Train: {len(train)}  Val: {len(val)}\n")
        return Dataset.from_list(train), Dataset.from_list(val)

    print(f"[DATA] Train: {len(formatted)}  No val split\n")
    return Dataset.from_list(formatted), None


# ── Model loading ─────────────────────────────────────────────────────────────
def load_model(hf_id):
    print(f"[MODEL] Loading {hf_id} ...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=hf_id, max_seq_length=MAX_SEQ_LENGTH,
        dtype=None, load_in_4bit=LOAD_IN_4BIT,  # dtype=None: auto bf16/fp16
    )
    model = FastLanguageModel.get_peft_model(
        model, r=LORA_R, target_modules=TARGET_MODULES,
        lora_alpha=LORA_ALPHA, lora_dropout=LORA_DROPOUT,
        bias="none", use_gradient_checkpointing="unsloth", random_state=42,
    )
    total     = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"[MODEL] Trainable: {trainable:,}/{total:,} ({100*trainable/total:.2f}%)\n")
    return model, tokenizer


# ── Trainer ───────────────────────────────────────────────────────────────────
def build_trainer(model, tokenizer, train_ds, val_ds, checkpoint_dir, chat_template) -> SFTTrainer:
    use_bf16 = torch.cuda.is_bf16_supported()
    eos = EOS_TOKENS[chat_template]
    tokenizer.eos_token = tokenizer.pad_token = eos

    def tokenize(batch):
        out = tokenizer(batch["text"], truncation=True, max_length=MAX_SEQ_LENGTH, padding=False)
        out["labels"] = out["input_ids"].copy()
        return out

    train_ds = train_ds.map(tokenize, batched=True, remove_columns=["text"], desc="Tokenizing train")
    if val_ds is not None:
        val_ds = val_ds.map(tokenize, batched=True, remove_columns=["text"], desc="Tokenizing val")

    args = SFTConfig(
        output_dir=checkpoint_dir,
        run_name=f"sc-finetune-{datetime.now().strftime('%Y%m%d_%H%M')}",
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        num_train_epochs=NUM_EPOCHS,
        learning_rate=LEARNING_RATE,
        warmup_steps=WARMUP_STEPS,
        bf16=use_bf16, fp16=not use_bf16,
        logging_steps=LOGGING_STEPS,
        save_steps=SAVE_STEPS,
        save_total_limit=3,
        eval_strategy="steps" if val_ds else "no",
        eval_steps=SAVE_STEPS if val_ds else None,
        load_best_model_at_end=bool(val_ds),
        optim="adamw_8bit",
        lr_scheduler_type="cosine",
        report_to="none",
        seed=42,
        max_length=MAX_SEQ_LENGTH,
        packing=False,
        dataset_text_field="text",
        dataset_kwargs={"skip_prepare_dataset": True},
        eos_token=eos,
        remove_unused_columns=False,
    )
    return SFTTrainer(model=model, processing_class=tokenizer,
                      train_dataset=train_ds, eval_dataset=val_ds, args=args)


# ── Pipeline ──────────────────────────────────────────────────────────────────
def run_single_model(model_key, dataset_path, no_val=False):
    cfg        = MODELS[model_key]
    hf_id, short_name = cfg["hf_id"], cfg["short_name"]
    formatter  = FORMATTERS[cfg["chat_template"]]
    ckpt_dir   = f"checkpoints/FT-{short_name}"
    save_dir   = f"FT-models/FT-{short_name}"

    print(f"\n{'='*60}\n  {hf_id}  [{cfg['chat_template']}]\n{'='*60}\n")

    train_ds, val_ds = load_dataset_split(dataset_path, formatter, 0.0 if no_val else VAL_SPLIT)
    model, tokenizer = load_model(hf_id)
    trainer = build_trainer(model, tokenizer, train_ds, val_ds, ckpt_dir, cfg["chat_template"])

    print("[TRAIN] Starting ...\n")
    result = trainer.train()
    print(f"[TRAIN] Done. loss={result.training_loss:.4f}  steps={result.global_step}  "
          f"runtime={result.metrics.get('train_runtime', 0):.1f}s")

    print(f"[SAVE] {save_dir} ...")
    model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)
    print(f"[DONE] {short_name} → {save_dir}\n")

    del model, tokenizer, trainer
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


# ── Entry point ───────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(description="Fine-tune smart contract generation models")
    p.add_argument("--model",   choices=list(MODELS.keys()) + ["all"], default="all")
    p.add_argument("--dataset", default=DATASET_PATH)
    p.add_argument("--no-val",  action="store_true")
    return p.parse_args()

def main():
    args = parse_args()
    targets: List[str] = list(MODELS.keys()) if args.model == "all" else [args.model]
    print(f"[START] Models: {', '.join(targets)}  Dataset: {args.dataset}")
    for key in targets:
        run_single_model(key, args.dataset, args.no_val)
    print(f"[DONE] {len(targets)} model(s) fine-tuned.")

if __name__ == "__main__":
    main()