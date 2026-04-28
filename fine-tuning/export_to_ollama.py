import os
from unsloth import FastLanguageModel

ADAPTER_DIR  = "./smart-contract-model"
GGUF_DIR     = "./smart-contract-model"
OLLAMA_NAME  = "smart-contract-model-FT"
QUANT        = "q4_k_m"  # q4_k_m | q5_k_m | q8_0 | f16

MODELFILE = """\
FROM {gguf_path}

TEMPLATE \"\"\"<|im_start|>system
{{{{ .System }}}}<|im_end|>
<|im_start|>user
{{{{ .Prompt }}}}<|im_end|>
<|im_start|>assistant
\"\"\"

SYSTEM "You are an expert Solidity smart contract developer."

PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.2
PARAMETER num_ctx 4096
"""

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name     = ADAPTER_DIR,
    max_seq_length = 4096,
    load_in_4bit   = True,
)

model.save_pretrained_gguf(GGUF_DIR, tokenizer, quantization_method=QUANT)

with open("Modelfile", "w") as f:
    f.write(MODELFILE.format(gguf_path=f"{GGUF_DIR}/unsloth.{QUANT.upper()}.gguf"))

print("GGUF and Modelfile ready.")
print("Now run in PowerShell:")
print(f"  ollama create {OLLAMA_NAME} -f ./smart-contract-model_gguf/Modelfile")


# to download base model
# ollama pull qwen2.5-coder:1.5b-instruct