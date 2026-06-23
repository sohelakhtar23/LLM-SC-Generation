>> (.v-ft1) pc_unix@DESKTOP-Q1DUBFR:/mnt/c/sohel/LLM-SC-Generation/fine-tuning$ `python FT_model_creation.py --model gemma3`
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so
W0623 07:31:16.888000 639 torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
W0623 07:31:17.320000 639 torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
🦥 Unsloth Zoo will now patch everything to make training faster!
<string>:1: FutureWarning: torch._dynamo.config.inline_inbuilt_nn_modules is deprecated and does not do anything, inline_inbuilt_nn_modules is always True. It will be removed in a future version of PyTorch.
[START] Models: gemma3  Dataset: FT_dataset/dataset.jsonl

============================================================
  google/gemma-3-1b-it  [gemma3]
============================================================

[DATA] Loading FT_dataset/dataset.jsonl ...
[DATA] 312 examples loaded
  compilation_repair                85 (27.2%)
  generation                       106 (34.0%)
  vulnerability_repair             121 (38.8%)
[DATA] Dropped 2 oversized examples
[DATA] Train: 295  Val: 15

[MODEL] Loading google/gemma-3-1b-it ...
==((====))==  Unsloth 2026.6.8: Fast Gemma3 patching. Transformers: 5.5.0.
   \\   /|    NVIDIA RTX 4000 Ada Generation. Num GPUs = 1. Max memory: 19.995 GB. Platform: Linux.
O^O/ \_/ \    Torch: 2.12.1+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.7.1
\        /    Bfloat16 = TRUE. FA [Xformers = None. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
model.safetensors: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.00G/1.00G [00:14<00:00, 68.1MB/s]
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 340/340 [00:00<00:00, 620.95it/s]
generation_config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 233/233 [00:00<00:00, 1.39MB/s]
tokenizer_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.16M/1.16M [00:00<00:00, 262MB/s]
tokenizer.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 33.4M/33.4M [00:01<00:00, 18.8MB/s]
added_tokens.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 35.0/35.0 [00:00<00:00, 140kB/s]
special_tokens_map.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 670/670 [00:00<00:00, 7.74MB/s]
Unsloth: Explicit target_modules are constrained by the finetune_(vision|language|attention|mlp) filters; adapters attach only where both select.
[MODEL] Trainable: 13,045,760/675,994,752 (1.93%)

Tokenizing train: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 295/295 [00:00<00:00, 883.24 examples/s]
Tokenizing val: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 895.25 examples/s]
🦥 Unsloth: Padding-free auto-enabled, enabling faster training.
[TRAIN] Starting ...

The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'pad_token_id': 106}.
==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
   \\   /|    Num examples = 295 | Num Epochs = 3 | Total steps = 111
O^O/ \_/ \    Batch size per device = 2 | Gradient accumulation steps = 4
\        /    Data Parallel GPUs = 1 | Total batch size (2 x 4 x 1) = 8
 "-____-"     Trainable parameters = 13,045,760 of 1,012,931,712 (1.29% trained)
  0%|                                                                                                                                                        | 0/111 [00:00<?, ?

Unsloth: Double buffering enabled (parallel H2D + compute) for backward pass.
Unsloth: Will smartly offload gradients to save VRAM!
{'loss': '1.548', 'grad_norm': '1.973', 'learning_rate': '3.6e-05', 'epoch': '0.2703'}                                                                                                               
{'loss': '1.17', 'grad_norm': '0.692', 'learning_rate': '7.6e-05', 'epoch': '0.5405'}                                                                                                                
{'loss': '0.8798', 'grad_norm': '0.5424', 'learning_rate': '0.000116', 'epoch': '0.8108'}                                                                                                            
{'loss': '0.692', 'grad_norm': '0.4348', 'learning_rate': '0.000156', 'epoch': '1.081'}                                                                                                              
{'loss': '0.5179', 'grad_norm': '0.5119', 'learning_rate': '0.000196', 'epoch': '1.351'}                                                                                                             
{'loss': '0.4304', 'grad_norm': '0.377', 'learning_rate': '0.0001894', 'epoch': '1.622'}                                                                                                             
{'loss': '0.3408', 'grad_norm': '0.328', 'learning_rate': '0.0001558', 'epoch': '1.892'}                                                                                                             
{'loss': '0.2937', 'grad_norm': '0.4747', 'learning_rate': '0.0001077', 'epoch': '2.162'}                                                                                                            
{'loss': '0.2301', 'grad_norm': '0.2698', 'learning_rate': '5.761e-05', 'epoch': '2.432'}                                                                                                            
{'loss': '0.221', 'grad_norm': '0.3639', 'learning_rate': '1.85e-05', 'epoch': '2.703'}                                                                                                              
{'eval_loss': '0.2559', 'eval_runtime': '9.94', 'eval_samples_per_second': '1.509', 'eval_steps_per_second': '0.402', 'epoch': '2.703'}                                                              
 90%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎               | 100/111 [11:48<01:08,  6.21s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Gemma-3-1B/checkpoint-100/tokenizer_config.json.                                                                                    
tokenizer.model: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.69M/4.69M [00:01<00:00, 2.46MB/s]
Unsloth: Preserved sentencepiece asset `tokenizer.model` in checkpoints/FT-Gemma-3-1B/checkpoint-100.                                                                    | 0.00/4.69M [00:01<?, ?B/s]
{'loss': '0.2138', 'grad_norm': '0.275', 'learning_rate': '5.3e-07', 'epoch': '2.973'}                                                                                                               
{'eval_loss': '0.2535', 'eval_runtime': '5.39', 'eval_samples_per_second': '2.783', 'eval_steps_per_second': '0.742', 'epoch': '3'}                                                                  
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [13:16<00:00,  6.16s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Gemma-3-1B/checkpoint-111/tokenizer_config.json.                                                                                    
Unsloth: Preserved sentencepiece asset `tokenizer.model` in checkpoints/FT-Gemma-3-1B/checkpoint-111.
{'train_runtime': '797.7', 'train_samples_per_second': '1.109', 'train_steps_per_second': '0.139', 'train_loss': '0.5908', 'epoch': '3'}                                                             
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [13:18<00:00,  7.19s/it]
[TRAIN] Done. loss=0.5908  steps=111  runtime=797.7s
[SAVE] FT-models/FT-Gemma-3-1B ...
Unsloth: Restored added_tokens_decoder metadata in FT-models/FT-Gemma-3-1B/tokenizer_config.json.
Unsloth: Preserved sentencepiece asset `tokenizer.model` in FT-models/FT-Gemma-3-1B.
[DONE] Gemma-3-1B → FT-models/FT-Gemma-3-1B

[DONE] 1 model(s) fine-tuned.