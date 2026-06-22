>> (.v-ft1) pc_unix@DESKTOP-Q1DUBFR:/mnt/c/sohel/LLM-SC-Generation/fine-tuning$ `python FT_model_creation.py --model llama`
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so
W0622 20:51:39.995000 3287 torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
W0622 20:51:40.232000 3287 torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
🦥 Unsloth Zoo will now patch everything to make training faster!
<string>:1: FutureWarning: torch._dynamo.config.inline_inbuilt_nn_modules is deprecated and does not do anything, inline_inbuilt_nn_modules is always True. It will be removed in a future version of PyTorch.
======================================================================
            SMART CONTRACT MODEL FINE-TUNING
======================================================================
  Models to fine-tune : llama
  Dataset             : FT_dataset/dataset.jsonl
======================================================================

======================================================================
  Model       : meta-llama/Llama-3.2-1B-Instruct
  Short name  : Llama-3.2-1B
  Template    : llama3
  Dataset     : FT_dataset/dataset.jsonl
  Epochs      : 3
  LR          : 0.0002
  LoRA r / α  : 16 / 16
  4-bit QLoRA : True
  Checkpoints : checkpoints/FT-Llama-3.2-1B
  Output      : FT-models/FT-Llama-3.2-1B
======================================================================

[DATA] Loading dataset from FT_dataset/dataset.jsonl ...
[DATA] 312 total examples loaded
  compilation_repair                85 (27.2%)
  generation                       106 (34.0%)
  vulnerability_repair             121 (38.8%)
[DATA] Dropped 2 examples exceeding ~4096 tokens
[DATA] Train: 295  |  Validation: 15

[MODEL] Loading meta-llama/Llama-3.2-1B-Instruct ...
==((====))==  Unsloth 2026.6.8: Fast Llama patching. Transformers: 5.5.0.
   \\   /|    NVIDIA RTX 4000 Ada Generation. Num GPUs = 1. Max memory: 19.995 GB. Platform: Linux.
O^O/ \_/ \    Torch: 2.12.1+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.7.1
\        /    Bfloat16 = TRUE. FA [Xformers = None. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 146/146 [00:02<00:00, 70.11it/s]
Unsloth: Will load unsloth/llama-3.2-1b-instruct-unsloth-bnb-4bit as a legacy tokenizer.
[MODEL] Attaching LoRA adapters ...
Unsloth 2026.6.8 patched 16 layers with 16 QKV layers, 16 O layers and 16 MLP layers.
[MODEL] Trainable params: 11,272,192 / 785,713,152 (1.43%)

Tokenizing train dataset: 100%|███████████████████████████████████████████████████████████████████████████| 295/295 [00:00<00:00, 903.17 examples/s]
Tokenizing val dataset: 100%|███████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 750.64 examples/s]
🦥 Unsloth: Padding-free auto-enabled, enabling faster training.
[TRAIN] Starting training ...

The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'pad_token_id': 128009}.
==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
   \\   /|    Num examples = 295 | Num Epochs = 3 | Total steps = 111
O^O/ \_/ \    Batch size per device = 2 | Gradient accumulation steps = 4
\        /    Data Parallel GPUs = 1 | Total batch size (2 x 4 x 1) = 8
 "-____-"     Trainable parameters = 11,272,192 of 1,247,086,592 (0.90% trained)
  0%|                                                                                                                       | 0/111 [00:00<?, ?it/s]`use_return_dict` is deprecated! Use `return_dict` instead!
Unsloth: Will smartly offload gradients to save VRAM!
Unsloth: Double buffering enabled (parallel H2D + compute) for backward pass.
{'loss': '1.065', 'grad_norm': '0.4988', 'learning_rate': '3.6e-05', 'epoch': '0.2703'}                                                             
{'loss': '0.9225', 'grad_norm': '0.3411', 'learning_rate': '7.6e-05', 'epoch': '0.5405'}                                                            
{'loss': '0.755', 'grad_norm': '0.3223', 'learning_rate': '0.000116', 'epoch': '0.8108'}                                                            
{'loss': '0.5576', 'grad_norm': '0.303', 'learning_rate': '0.000156', 'epoch': '1.081'}                                                             
{'loss': '0.3841', 'grad_norm': '0.3656', 'learning_rate': '0.000196', 'epoch': '1.351'}                                                            
{'loss': '0.3241', 'grad_norm': '0.3106', 'learning_rate': '0.0001894', 'epoch': '1.622'}                                                           
{'loss': '0.2817', 'grad_norm': '0.2551', 'learning_rate': '0.0001558', 'epoch': '1.892'}                                                           
{'loss': '0.2459', 'grad_norm': '0.3833', 'learning_rate': '0.0001077', 'epoch': '2.162'}                                                           
{'loss': '0.1948', 'grad_norm': '0.2423', 'learning_rate': '5.761e-05', 'epoch': '2.432'}                                                           
{'loss': '0.1945', 'grad_norm': '0.3136', 'learning_rate': '1.85e-05', 'epoch': '2.703'}                                                            
{'eval_loss': '0.2219', 'eval_runtime': '41.94', 'eval_samples_per_second': '0.358', 'eval_steps_per_second': '0.095', 'epoch': '2.703'}            
 90%|██████████████████████████████████████████████████████████████████████████████████████████████████▏          | 100/111 [10:18<00:54,  4.93s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Llama-3.2-1B/checkpoint-100/tokenizer_config.json.                                 
{'loss': '0.1907', 'grad_norm': '0.2588', 'learning_rate': '5.3e-07', 'epoch': '2.973'}                                                             
{'eval_loss': '0.2201', 'eval_runtime': '9.152', 'eval_samples_per_second': '1.639', 'eval_steps_per_second': '0.437', 'epoch': '3'}                
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [11:47<00:00,  6.43s/it]Unsloth: Restored added_tokens_decoder metadata in checkpoints/FT-Llama-3.2-1B/checkpoint-111/tokenizer_config.json.                                 
{'train_runtime': '719.5', 'train_samples_per_second': '1.23', 'train_steps_per_second': '0.154', 'train_loss': '0.4625', 'epoch': '3'}             
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 111/111 [12:00<00:00,  6.49s/it]

[TRAIN] Training complete.
  Training loss : 0.4625
  Total steps   : 111
  Runtime       : 719.5s

[SAVE] Saving model to FT-models/FT-Llama-3.2-1B ...
Unsloth: Restored added_tokens_decoder metadata in FT-models/FT-Llama-3.2-1B/tokenizer_config.json.
[SAVE] Done.

======================================================================
[SUCCESS] Llama-3.2-1B fine-tuning complete!
          Model saved to : FT-models/FT-Llama-3.2-1B/
          Checkpoints in : checkpoints/FT-Llama-3.2-1B/
======================================================================


======================================================================
[DONE] All 1 model(s) fine-tuned successfully.
======================================================================