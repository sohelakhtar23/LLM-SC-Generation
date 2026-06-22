>> (.v-ft1) pc_unix@DESKTOP-Q1DUBFR:/mnt/c/sohel/LLM-SC-Generation/fine-tuning$ `python export_to_ollama.py --model qwen`
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_cutlass_90a.abi3.so
[torchao|WARNING]Failed to load /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so: Could not load this library: /mnt/c/sohel/LLM-SC-Generation/.v-ft1/lib/python3.12/site-packages/torchao/_C_mxfp8.cpython-310-x86_64-linux-gnu.so
W0622 21:55:30.960000 19505 torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
W0622 21:55:31.220000 19505 torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an error in a future release.
🦥 Unsloth Zoo will now patch everything to make training faster!
<string>:1: FutureWarning: torch._dynamo.config.inline_inbuilt_nn_modules is deprecated and does not do anything, inline_inbuilt_nn_modules is always True. It will be removed in a future version of PyTorch.

======================================================================
[EXPORT] Qwen2.5-Coder-0.5B
  Adapter source : FT-models/FT-Qwen2.5-Coder-0.5B
  GGUF output    : ollama-models/Qwen2.5-Coder-0.5B-GGUF
  Quantization   : q4_k_m
======================================================================
==((====))==  Unsloth 2026.6.8: Fast Qwen2 patching. Transformers: 5.5.0.
   \\   /|    NVIDIA RTX 4000 Ada Generation. Num GPUs = 1. Max memory: 19.995 GB. Platform: Linux.
O^O/ \_/ \    Torch: 2.12.1+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.7.1
\        /    Bfloat16 = TRUE. FA [Xformers = None. FA2 = False]
 "-____-"     Free license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 290/290 [00:00<00:00, 509.79it/s]
Unsloth 2026.6.8 patched 24 layers with 24 QKV layers, 24 O layers and 24 MLP layers.
Unsloth: Merging model weights to 16-bit format...
config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 764/764 [00:00<00:00, 2.97MB/s]
Unsloth: Restored added_tokens_decoder metadata in ollama-models/Qwen2.5-Coder-0.5B-GGUF/tokenizer_config.json.
Found HuggingFace hub cache directory: /home/pc_unix/.cache/huggingface/hub
Checking cache directory for required files...
Cache check failed: model.safetensors not found in local cache.
Not all required files found in cache. Will proceed with downloading.
Checking cache directory for required files...
Cache check failed: tokenizer.model not found in local cache.
Not all required files found in cache. Will proceed with downloading.
model.safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 988M/988M [00:13<00:00, 74.4MB/s]
Unsloth: Preparing safetensor model files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:13<00:00, 13.76s/it]
Note: tokenizer.model not found (this is OK for non-SentencePiece models)
Unsloth: Merging weights into 16bit: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:24<00:00, 24.51s/it]
Unsloth: Merge process complete. Saved to `/mnt/c/sohel/LLM-SC-Generation/fine-tuning/ollama-models/Qwen2.5-Coder-0.5B-GGUF`
Unsloth: Converting to GGUF format...
==((====))==  Unsloth: Conversion from HF to GGUF information
   \\   /|    [0] Installing llama.cpp might take 3 minutes.
O^O/ \_/ \    [1] Converting HF to GGUF bf16 might take 3 minutes.
\        /    [2] Converting GGUF bf16 to ['q4_k_m'] might take 10 minutes each.
 "-____-"     In total, you will have to wait at least 16 minutes.

Unsloth: llama.cpp found in the system. Skipping installation.
Unsloth: Preparing converter script...
Unsloth: [1] Converting model into bf16 GGUF format.
This might take 3 minutes...
Unsloth: Initial conversion completed! Files: ['ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/qwen2.5-coder-0.5b-instruct.BF16.gguf']
Unsloth: [2] Converting GGUF bf16 into q4_k_m. This might take 10 minutes...
Unsloth: Model files cleanup...
Unsloth: All GGUF conversions completed successfully!
Generated files: ['ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/qwen2.5-coder-0.5b-instruct.Q4_K_M.gguf']
Unsloth: example usage for text only LLMs: /home/pc_unix/.unsloth/llama.cpp/llama-cli --model ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/qwen2.5-coder-0.5b-instruct.Q4_K_M.gguf -p "why is the sky blue?"
Unsloth: Saved Ollama Modelfile to ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/Modelfile
Unsloth: convert model to ollama format by running - ollama create model_name -f ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/Modelfile
[OLLAMA] 'ollama' CLI not found on PATH. To finish manually, run:
    ollama create <sc-qwen> -f ollama-models/Qwen2.5-Coder-0.5B-GGUF_gguf/Modelfile