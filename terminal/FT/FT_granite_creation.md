>> (.v-ft1) pc_unix@DESKTOP-Q1DUBFR:/mnt/c/sohel/LLM-SC-Generation/fine-tuning$ `python FT_model_creation.py --model granite`
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so
W0622 21:16:07.489000 3821 torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
W0622 21:16:07.706000 3821 torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
🦥 Unsloth Zoo will now patch everything to make training faster!
<string>:1: FutureWarning: torch._dynamo.config.inline_inbuilt_nn_modules is deprecated and does not do anything, inline_inbuilt_nn_modules is always True. It will be removed in a future version of PyTorch.
======================================================================
            SMART CONTRACT MODEL FINE-TUNING
======================================================================
  Models to fine-tune : granite
  Dataset             : FT_dataset/dataset.jsonl
======================================================================

======================================================================
  Model       : ibm-granite/granite-4.0-1b
  Short name  : Granite-4.0-1B
  Template    : granite4
  Dataset     : FT_dataset/dataset.jsonl
  Epochs      : 3
  LR          : 0.0002
  LoRA r / α  : 16 / 16
  4-bit QLoRA : True
  Checkpoints : checkpoints/FT-Granite-4.0-1B
  Output      : FT-models/FT-Granite-4.0-1B
======================================================================

[DATA] Loading dataset from FT_dataset/dataset.jsonl ...
[DATA] 312 total examples loaded
  compilation_repair                85 (27.2%)
  generation                       106 (34.0%)
  vulnerability_repair             121 (38.8%)
[DATA] Dropped 2 examples exceeding ~4096 tokens
[DATA] Train: 295  |  Validation: 15

[MODEL] Loading ibm-granite/granite-4.0-1b ...
==((====))==  Unsloth 2026.6.8: Fast Granitemoehybrid patching. Transformers: 5.5.0.
   \\   /|    NVIDIA RTX 4000 Ada Generation. Num GPUs = 1. Max memory: 19.995 GB. Platform: Linux.
O^O/ \_/ \    Torch: 2.12.1+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.7.1
\        /    Bfloat16 = TRUE. FA [Xformers = None. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
Loading weights: 100%|████████████████████████████████████████████████████████████████| 322/322 [00:01<00:00, 173.28it/s]
[MODEL] Attaching LoRA adapters ...
Unsloth: Explicit target_modules are constrained by the finetune_(vision|language|attention|mlp) filters; adapters attach only where both select.
[MODEL] Trainable params: 8,519,680 / 977,569,792 (0.87%)

Tokenizing train dataset: 100%|████████████████████████████████████████████████| 295/295 [00:00<00:00, 922.34 examples/s]
Tokenizing val dataset: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 753.06 examples/s]
🦥 Unsloth: Padding-free auto-enabled, enabling faster training.
[TRAIN] Starting training ...

The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'pad_token_id': 100257}.
==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
   \\   /|    Num examples = 295 | Num Epochs = 3 | Total steps = 111
O^O/ \_/ \    Batch size per device = 2 | Gradient accumulation steps = 4
\        /    Data Parallel GPUs = 1 | Total batch size (2 x 4 x 1) = 8
 "-____-"     Trainable parameters = 8,519,680 of 1,640,269,824 (0.52% trained)
  0%|                                                                                                                                                                                         | 0/111 [00:00<?, ?it/s]Unsloth: Will smartly offload gradients to save VRAM!
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:239: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/bitsandbytes/_ops.py:186: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
Unsloth: Double buffering enabled (parallel H2D + compute) for backward pass.
{'loss': '4.94', 'grad_norm': '11.94', 'learning_rate': '3.6e-05', 'epoch': '0.2703'}                                                                                                                                 
{'loss': '2.63', 'grad_norm': '2.901', 'learning_rate': '7.6e-05', 'epoch': '0.5405'}                                                                                                                                 
{'loss': '1.081', 'grad_norm': '0.8385', 'learning_rate': '0.000116', 'epoch': '0.8108'}                                                                                                                              
{'loss': '0.7413', 'grad_norm': '0.4358', 'learning_rate': '0.000156', 'epoch': '1.081'}                                                                                                                              
{'loss': '0.5648', 'grad_norm': '0.3222', 'learning_rate': '0.000196', 'epoch': '1.351'}                                                                                                                              
{'loss': '0.4743', 'grad_norm': '0.3438', 'learning_rate': '0.0001894', 'epoch': '1.622'}                                                                                                                             
{'loss': '0.3999', 'grad_norm': '0.3101', 'learning_rate': '0.0001558', 'epoch': '1.892'}                                                                                                                             
{'loss': '0.3454', 'grad_norm': '0.4087', 'learning_rate': '0.0001077', 'epoch': '2.162'}                                                                                                                             
{'loss': '0.2711', 'grad_norm': '0.2936', 'learning_rate': '5.761e-05', 'epoch': '2.432'}                                                                                                                             
{'loss': '0.2602', 'grad_norm': '0.3653', 'learning_rate': '1.85e-05', 'epoch': '2.703'}                                                                                                                              
{'eval_loss': '0.3695', 'eval_runtime': '3.005', 'eval_samples_per_second': '4.992', 'eval_steps_per_second': '1.331', 'epoch': '2.703'}                                                                              
 90%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋                 | 100/111 [06:44<00:44,  4.08s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Granite-4.0-1B/checkpoint-100/tokenizer_config.json.                                                                                                 
{'loss': '0.2454', 'grad_norm': '0.2903', 'learning_rate': '5.3e-07', 'epoch': '2.973'}                                                                                                                               
{'eval_loss': '0.3656', 'eval_runtime': '2.589', 'eval_samples_per_second': '5.795', 'eval_steps_per_second': '1.545', 'epoch': '3'}                                                                                  
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [07:42<00:00,  3.74s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Granite-4.0-1B/checkpoint-111/tokenizer_config.json.                                                                                                 
{'train_runtime': '474.3', 'train_samples_per_second': '1.866', 'train_steps_per_second': '0.234', 'train_loss': '1.079', 'epoch': '3'}                                                                               
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [07:55<00:00,  4.28s/it]

[TRAIN] Training complete.
  Training loss : 1.0792
  Total steps   : 111
  Runtime       : 474.3s

[SAVE] Saving model to FT-models/FT-Granite-4.0-1B ...
Unsloth: Restored added_tokens_decoder metadata in FT-models/FT-Granite-4.0-1B/tokenizer_config.json.
[SAVE] Done.

======================================================================
[SUCCESS] Granite-4.0-1B fine-tuning complete!
          Model saved to : FT-models/FT-Granite-4.0-1B/
          Checkpoints in : checkpoints/FT-Granite-4.0-1B/
======================================================================


======================================================================
[DONE] All 1 model(s) fine-tuned successfully.
======================================================================