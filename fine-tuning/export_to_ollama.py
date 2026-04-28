import os
import subprocess
from unsloth import FastLanguageModel

ADAPTER_DIR  = "./smart-contract-model"
GGUF_DIR     = "./smart-contract-model-gguf"
OLLAMA_NAME  = "smart-contract-model"
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

gguf_path = next(f for f in os.listdir(GGUF_DIR) if f.endswith(".gguf"))
gguf_path = os.path.abspath(os.path.join(GGUF_DIR, gguf_path))

with open("Modelfile", "w") as f:
    f.write(MODELFILE.format(gguf_path=gguf_path))

subprocess.run(["ollama", "create", OLLAMA_NAME, "-f", "Modelfile"], check=True)

print(f"\nDone. Run with: ollama run {OLLAMA_NAME}")
