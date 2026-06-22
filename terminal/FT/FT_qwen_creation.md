>> (.v-ft1) pc_unix@DESKTOP-Q1DUBFR:/mnt/c/sohel/LLM-SC-Generation/fine-tuning$ `python FT_model_creation.py --model qwen`
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so
W0622 21:07:18.458000 3585 torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
W0622 21:07:18.700000 3585 torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
🦥 Unsloth Zoo will now patch everything to make training faster!
<string>:1: FutureWarning: torch._dynamo.config.inline_inbuilt_nn_modules is deprecated and does not do anything, inline_inbuilt_nn_modules is always True. It will be removed in a future version of PyTorch.
======================================================================
            SMART CONTRACT MODEL FINE-TUNING
======================================================================
  Models to fine-tune : qwen
  Dataset             : FT_dataset/dataset.jsonl
======================================================================

======================================================================
  Model       : Qwen/Qwen2.5-Coder-0.5B-Instruct
  Short name  : Qwen2.5-Coder-0.5B
  Template    : qwen
  Dataset     : FT_dataset/dataset.jsonl
  Epochs      : 3
  LR          : 0.0002
  LoRA r / α  : 16 / 16
  4-bit QLoRA : True
  Checkpoints : checkpoints/FT-Qwen2.5-Coder-0.5B
  Output      : FT-models/FT-Qwen2.5-Coder-0.5B
======================================================================

[DATA] Loading dataset from FT_dataset/dataset.jsonl ...
[DATA] 312 total examples loaded
  compilation_repair                85 (27.2%)
  generation                       106 (34.0%)
  vulnerability_repair             121 (38.8%)
[DATA] Dropped 2 examples exceeding ~4096 tokens
[DATA] Train: 295  |  Validation: 15

[MODEL] Loading Qwen/Qwen2.5-Coder-0.5B-Instruct ...
==((====))==  Unsloth 2026.6.8: Fast Qwen2 patching. Transformers: 5.5.0.
   \\   /|    NVIDIA RTX 4000 Ada Generation. Num GPUs = 1. Max memory: 19.995 GB. Platform: Linux.
O^O/ \_/ \    Torch: 2.12.1+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.7.1
\        /    Bfloat16 = TRUE. FA [Xformers = None. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
Loading weights: 100%|███████████████████████████████████████████████████████████████████████████████████████████| 290/290 [00:00<00:00, 304.62it/s]
[MODEL] Attaching LoRA adapters ...
Unsloth 2026.6.8 patched 24 layers with 24 QKV layers, 24 O layers and 24 MLP layers.
[MODEL] Trainable params: 8,798,208 / 323,917,696 (2.72%)

Tokenizing train dataset: 100%|███████████████████████████████████████████████████████████████████████████| 295/295 [00:00<00:00, 906.93 examples/s]
Tokenizing val dataset: 100%|███████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 789.13 examples/s]
🦥 Unsloth: Padding-free auto-enabled, enabling faster training.
[TRAIN] Starting training ...

The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'bos_token_id': None, 'pad_token_id': 151645}.
==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
   \\   /|    Num examples = 295 | Num Epochs = 3 | Total steps = 111
O^O/ \_/ \    Batch size per device = 2 | Gradient accumulation steps = 4
\        /    Data Parallel GPUs = 1 | Total batch size (2 x 4 x 1) = 8
 "-____-"     Trainable parameters = 8,798,208 of 502,830,976 (1.75% trained)
  0%|                                                                                                                       | 0/111 [00:00<?, ?it/s]`use_return_dict` is deprecated! Use `return_dict` instead!
Unsloth: Double buffering enabled (parallel H2D + compute) for backward pass.
Unsloth: Will smartly offload gradients to save VRAM!
{'loss': '0.9446', 'grad_norm': '0.3593', 'learning_rate': '3.6e-05', 'epoch': '0.2703'}                                                            
{'loss': '0.8321', 'grad_norm': '0.2613', 'learning_rate': '7.6e-05', 'epoch': '0.5405'}                                                            
{'loss': '0.6894', 'grad_norm': '0.2949', 'learning_rate': '0.000116', 'epoch': '0.8108'}                                                           
{'loss': '0.5065', 'grad_norm': '0.2778', 'learning_rate': '0.000156', 'epoch': '1.081'}                                                            
{'loss': '0.3446', 'grad_norm': '0.3438', 'learning_rate': '0.000196', 'epoch': '1.351'}                                                            
{'loss': '0.2759', 'grad_norm': '0.2523', 'learning_rate': '0.0001894', 'epoch': '1.622'}                                                           
{'loss': '0.2308', 'grad_norm': '0.2369', 'learning_rate': '0.0001558', 'epoch': '1.892'}                                                           
{'loss': '0.2015', 'grad_norm': '0.3125', 'learning_rate': '0.0001077', 'epoch': '2.162'}                                                           
{'loss': '0.1584', 'grad_norm': '0.2156', 'learning_rate': '5.761e-05', 'epoch': '2.432'}                                                           
{'loss': '0.1601', 'grad_norm': '0.2679', 'learning_rate': '1.85e-05', 'epoch': '2.703'}                                                            
{'eval_loss': '0.1795', 'eval_runtime': '4.458', 'eval_samples_per_second': '3.365', 'eval_steps_per_second': '0.897', 'epoch': '2.703'}            
 90%|██████████████████████████████████████████████████████████████████████████████████████████████████▏          | 100/111 [05:47<00:36,  3.34s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Qwen2.5-Coder-0.5B/checkpoint-100/tokenizer_config.json.                           
{'loss': '0.1577', 'grad_norm': '0.2265', 'learning_rate': '5.3e-07', 'epoch': '2.973'}                                                             
{'eval_loss': '0.1781', 'eval_runtime': '3.721', 'eval_samples_per_second': '4.031', 'eval_steps_per_second': '1.075', 'epoch': '3'}                
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [06:41<00:00,  3.38s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Qwen2.5-Coder-0.5B/checkpoint-111/tokenizer_config.json.                           
{'train_runtime': '403', 'train_samples_per_second': '2.196', 'train_steps_per_second': '0.275', 'train_loss': '0.4069', 'epoch': '3'}              
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [06:43<00:00,  3.63s/it]

[TRAIN] Training complete.
  Training loss : 0.4069
  Total steps   : 111
  Runtime       : 403.0s

[SAVE] Saving model to FT-models/FT-Qwen2.5-Coder-0.5B ...
Unsloth: Restored added_tokens_decoder metadata in FT-models/FT-Qwen2.5-Coder-0.5B/tokenizer_config.json.
[SAVE] Done.

======================================================================
[SUCCESS] Qwen2.5-Coder-0.5B fine-tuning complete!
          Model saved to : FT-models/FT-Qwen2.5-Coder-0.5B/
          Checkpoints in : checkpoints/FT-Qwen2.5-Coder-0.5B/
======================================================================


======================================================================
[DONE] All 1 model(s) fine-tuned successfully.
======================================================================