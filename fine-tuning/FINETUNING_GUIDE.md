# Fine-Tuning Strategy Guide

## Overview

This guide explains how to create a high-quality fine-tuning dataset from your smart contract generation experiments and use it to train a small (~2B parameter) model.

## Table of Contents

1. [Fine-Tuning Dataset Strategy](#fine-tuning-dataset-strategy)
2. [Dataset Creation Pipeline](#dataset-creation-pipeline)
3. [Dataset Quality Filters](#dataset-quality-filters)
4. [Fine-Tuning Recommendations](#fine-tuning-recommendations)
5. [Evaluation Strategy](#evaluation-strategy)

---

## Fine-Tuning Dataset Strategy

### Three Task Types
The dataset will contain 3 types of instruction-response pairs:

#### 1. **Contract Generation** (from `generate_contracts.py`)
```
Instruction: Generate a Solidity contract
Input: Task + Specification
Output: Clean, secure contract

Quality Criteria:
✓ Compiled successfully
✓ High-quality code
```

#### 2. **Compilation Repair** (from `repair_compilation.py`)
```
Instruction: Fix compilation errors
Input: Task + Spec + Faulty Code + Error Messages
Output: Fixed, compiling contract

Quality Criteria:
✓ Repaired contract compiles
✓ Low vulnerability count
✓ Preserves functionality
```

#### 3. **Vulnerability Repair** (from `repair_vulnerability.py`)
```
Instruction: Fix security vulnerabilities
Input: Task + Vulnerable Code + Vulnerability List
Output: Secure contract

Quality Criteria:
✓ Repaired contract compiles
✓ Reduced vulnerability count (ideally to 0)
```

### Dataset Format
**JSONL** (recommended for most frameworks):
```jsonl
{"task_type": "generation", "instruction": "...", "input": "...", "output": "...", "metadata": {...}}
{"task_type": "compilation_repair", "instruction": "...", "input": "...", "output": "...", "metadata": {...}}
```

---

## Dataset Creation Pipeline

### Current Implementation

```bash
# Step 1: Run all experiments
python generate_contracts.py
python compile_and_analyze.py
python repair_compilation.py
python repair_vulnerability.py

# Step 2: Create fine-tuning dataset
python create_finetuning_dataset.py
```

### What the Script Does

1. **Loads all experiment results**:
   - `compilation_results.json` (required)
   - `generation_summary.json` (required)
   - `compilation_repair_results.json` (optional)
   - `vulnerability_repair_results.json` (optional)

2. **Applies quality filters**:
   - Generation: Must compile + have ≤0 malign vulnerabilities
   - Compilation repair: Must compile after repair + have ≤2 malign vulnerabilities
   - Vulnerability repair: Must compile + show improvement

3. **Selects best examples**:
   - For repair tasks, picks the best strategy (highest quality score)
   - Calculates quality scores based on vulnerability counts
   - Filters by minimum quality threshold (default: 0.7)

4. **Exports dataset**:
   - `dataset.jsonl` - Full dataset
   - `dataset_generation.jsonl` - Only generation examples
   - `dataset_compilation_repair.jsonl` - Only compilation repair
   - `dataset_vulnerability_repair.jsonl` - Only vulnerability repair
   - `dataset_statistics.json` - Quality metrics and distributions

### Output Directory Structure

```
finetuning_dataset/
├── dataset.jsonl                          # Full dataset (all tasks)
├── dataset_generation.jsonl               # Only generation examples
├── dataset_compilation_repair.jsonl       # Only compilation repair
├── dataset_vulnerability_repair.jsonl     # Only vulnerability repair
└── dataset_statistics.json                # Dataset statistics
```

---



## Dataset Quality Filters

### Configurable Thresholds

Edit these in `create_finetuning_dataset.py`:

```python
# Lines 10-13
MIN_QUALITY_SCORE = 0.7                    # 0.0 to 1.0 (higher = stricter)
MAX_VULNERABILITIES_ALLOWED = 0            # For generation task
MAX_VULNERABILITIES_AFTER_REPAIR = 2       # For repair tasks
```

### Quality Scoring Algorithm

```python
Quality Score = Vulnerability Score × Reduction Ratio (for repairs)

Vulnerability Score = max(0, 1.0 - (weighted_penalty / 10))

Where weighted_penalty:
- High severity:    1.0 per vulnerability
- Medium severity:  0.5 per vulnerability
- Low severity:     0.2 per vulnerability
- Informational:    0.0 (ignored)
- Optimization:     0.0 (ignored)
```

### Expected Dataset Size

Based on typical pipeline statistics:

```
Starting from:
- 2400 generated contracts
- ~470 compilation failures
- ~1400 vulnerable contracts

After quality filtering (estimates):
┌─────────────────────────────┬─────────┬──────────────┬──────────┐
│ Task Type                   │ Total   │ High Quality │ % Used   │
├─────────────────────────────┼─────────┼──────────────┼──────────┤
│ Generation                  │ 2400    │ 480          │ 20%      │
│ Compilation Repair          │ 470     │ 190          │ 40%      │
│ Vulnerability Repair        │ 1400    │ 420          │ 30%      │
├─────────────────────────────┼─────────┼──────────────┼──────────┤
│ TOTAL                       │ 4270    │ 1090         │ 25%      │
└─────────────────────────────┴─────────┴──────────────┴──────────┘

Final dataset: ~1000-1500 high-quality examples
```

### Adjusting Dataset Size

**Too few examples?** (< 500)
```python
MIN_QUALITY_SCORE = 0.5                    # Lower threshold
MAX_VULNERABILITIES_AFTER_REPAIR = 5       # More lenient
```

**Too many examples?** (> 3000)
```python
MIN_QUALITY_SCORE = 0.85                   # Higher threshold
MAX_VULNERABILITIES_AFTER_REPAIR = 1       # Stricter
```

**Want balanced dataset?**
```python
# Manually limit per task type after collection
max_per_task = 500
for task_type in ["generation", "compilation_repair", "vulnerability_repair"]:
    task_examples = [e for e in examples if e["task_type"] == task_type]
    task_examples = sorted(task_examples, 
                          key=lambda x: x["metadata"]["quality_score"], 
                          reverse=True)[:max_per_task]
```

---

## Fine-Tuning Recommendations

### Model Selection (~2B parameters)

Recommended base models:
1. **Qwen2.5-Coder-1.5B-Instruct** - Best for code
2. **Gemma-2B-IT** - Good general instruction following
3. **Phi-2 (2.7B)** - Strong reasoning capabilities
4. **StableLM-2-1.6B** - Open weights, good performance

### Fine-Tuning Framework

**Option 1: Unsloth** (Recommended - Fast & Memory Efficient)
```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Qwen/Qwen2.5-Coder-1.5B-Instruct",
    max_seq_length = 4096,
    dtype = None,
    load_in_4bit = True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_alpha = 16,
    lora_dropout = 0.05,
    use_gradient_checkpointing = True,
)
```

**Option 2: HuggingFace TRL**
```python
from trl import SFTTrainer

trainer = SFTTrainer(
    model = model,
    train_dataset = dataset,
    max_seq_length = 4096,
    dataset_text_field = "text",  # Combined instruction+input+output
    packing = True,
)
```

### Training Hyperparameters

```python
training_args = TrainingArguments(
    per_device_train_batch_size = 2,
    gradient_accumulation_steps = 4,
    warmup_steps = 50,
    num_train_epochs = 3,
    learning_rate = 2e-4,
    fp16 = True,
    logging_steps = 10,
    output_dir = "outputs",
    optim = "adamw_8bit",
)
```

### Data Preparation

Convert to training format:

```python
def format_prompt(example):
    """Convert example to training text."""
    return f"""<|im_start|>system
{example['instruction']}<|im_end|>
<|im_start|>user
{example['input']}<|im_end|>
<|im_start|>assistant
{example['output']}<|im_end|>"""

# Load dataset
import json
with open('finetuning_dataset/dataset.jsonl', 'r') as f:
    dataset = [json.loads(line) for line in f]

# Format for training
formatted_dataset = [{"text": format_prompt(ex)} for ex in dataset]
```

### Training Script Template

```python
# train.py
import json
from datasets import Dataset
from transformers import TrainingArguments
from trl import SFTTrainer
from unsloth import FastLanguageModel

# Load model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Qwen/Qwen2.5-Coder-1.5B-Instruct",
    max_seq_length=4096,
    load_in_4bit=True,
)

# Add LoRA adapters
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_alpha=16,
)

# Load and format dataset
with open('finetuning_dataset/dataset.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

def format_prompt(example):
    return {
        "text": f"""<|im_start|>system
{example['instruction']}<|im_end|>
<|im_start|>user
{example['input']}<|im_end|>
<|im_start|>assistant
{example['output']}<|im_end|>"""
    }

dataset = Dataset.from_list([format_prompt(ex) for ex in data])

# Train
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=4096,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        num_train_epochs=3,
        learning_rate=2e-4,
        fp16=True,
        output_dir="./outputs",
        logging_steps=10,
    ),
)

trainer.train()

# Save
model.save_pretrained("smart-contract-model")
tokenizer.save_pretrained("smart-contract-model")
```

---

## Evaluation Strategy

### 1. Quantitative Metrics

Compare fine-tuned model vs base model using **the same pipeline**:

```bash
# Modify generate_contracts.py to use fine-tuned model
MODELS = ["your-finetuned-model:latest"]

# Run full pipeline
python generate_contracts.py
python compile_and_analyze.py

# Compare results
```

**Metrics to Compare**:
1. **Compilation Success Rate**: % of generated contracts that compile
2. **Security Score**: % of compiled contracts with 0 malign vulnerabilities
3. **Vulnerability Reduction**: Average malign vulnerability count
4. **Generation Time**: Seconds per contract (smaller model should be faster)
5. **Overall Success Rate**: % that compile AND are secure

### 2. Ablation Studies

Test different training configurations:

**Dataset Composition**:
```python
# Train on only generation examples
dataset_generation_only = load_dataset('dataset_generation.jsonl')

# Train on only repair examples
dataset_repair_only = load_datasets([
    'dataset_compilation_repair.jsonl',
    'dataset_vulnerability_repair.jsonl'
])

# Compare: Which subset gives best results?
```

**Task-Specific Fine-Tuning**:
```python
# Option A: Multi-task (all 3 tasks together) ← Recommended
# Option B: Generation-only
# Option C: Repair-only

# Which performs best on your evaluation set?
```

### 3. Human Evaluation

For a subset of generated contracts (e.g., 50), manually check:
- **Correctness**: Does it match the specification?
- **Security**: Are there obvious vulnerabilities?
- **Code Quality**: Is it well-structured?
- **Readability**: Is it documented?

### 4. Expected Results

**Realistic expectations for a 2B fine-tuned model**:

```
Compared to base 7B model:
✓ 10-20% improvement in compilation rate
✓ 15-30% improvement in security (fewer vulnerabilities)
✓ 2-3x faster inference (smaller model)
✗ Might struggle with complex specifications
✗ Might have lower variety in solutions

Compared to base 2B model (same size):
✓ 30-50% improvement in compilation rate
✓ 40-60% improvement in security
✓ Much better at following Solidity conventions
✓ Better at applying security patterns

Sweet spot:
- For simple/medium contracts: Fine-tuned 2B ≈ Base 7B
- For complex contracts: Fine-tuned 2B < Base 7B
- For all tasks: Fine-tuned 2B ≫ Base 2B
```

---



## Research Questions You Can Answer

1. **Can small models match large models with task-specific training?**
   - Compare fine-tuned 2B vs base 7B

2. **What's the optimal dataset composition?**
   - Generation-only vs Multi-task vs Repair-only

3. **Is synthetic data from LLMs effective for training?**
   - Your entire dataset is LLM-generated!

4. **Do repair examples improve generation quality?**
   - Train with/without repair tasks and compare

5. **What's the minimum dataset size needed?**
   - Train with 100, 300, 500, 1000, 1500 examples


---

## Troubleshooting

### "No examples collected"
- Check quality thresholds (too strict?)
- Verify experiment results exist
- Lower MIN_QUALITY_SCORE to 0.5

### "Dataset too small" (< 300 examples)
- Lower quality threshold
- Include Informational vulnerabilities
- Use more iterations in generation

### "Dataset too large" (> 5000 examples)
- Increase quality threshold
- Sample randomly from each task type
- Use only best strategies for repair

### "Unbalanced task distribution"
- Manually balance by sampling from each task
- Weight loss during training
- Train task-specific models separately

### "Out of memory during fine-tuning"
- Use 4-bit quantization (`load_in_4bit=True`)
- Reduce batch size
- Use gradient checkpointing
- Reduce sequence length

---

## Tips for Success

1. **Start small**: Train on 500-1000 examples first
2. **Use LoRA**: Full fine-tuning is overkill for 2B models
3. **Monitor overfitting**: Validate on held-out prompts
4. **Save checkpoints**: You can resume training
5. **Test incrementally**: Evaluate after each epoch
6. **Document everything**: Track hyperparameters and results
7. **Compare fairly**: Use same prompts for evaluation

---

