wsl --install
username: pc_unix
pwd: open

# run below if wsl(Linux) newly installed 
sudo apt update
sudo apt install python3-venv python3-pip -y


# create virutal env
python3 -m venv .venv
source .venv/bin/activate



# Installation steps for Fine-Tuning: (LabPC guide=> use WSL terminal in Windows)
1. Check CUDA version:
nvidia-smi

2. Install matching PyTorch version:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

Verify it worked:
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
[Should print: True  |  NVIDIA RTX 4000 Ada Generation] 

3. Install unsloth:
<!-- pip install "unsloth[cu124-torch260] @ git+https://github.com/unslothai/unsloth.git" -->
pip install unsloth

4. other dependencies: <== already satisfied
pip install trl transformers accelerate bitsandbytes datasets

5. Final Verification:
python - <<'EOF'
import torch
from unsloth import FastLanguageModel
from trl import SFTTrainer
from datasets import Dataset
print("✅ All imports successful")
print(f"   CUDA available : {torch.cuda.is_available()}")
print(f"   GPU            : {torch.cuda.get_device_name(0)}")
print(f"   PyTorch ver    : {torch.__version__}")
print(f"   bf16 support   : {torch.cuda.is_bf16_supported()}")
EOF


# uv package (for fast installation)
check uv version: `uv --version`

create vevn: `uv venv .venv`
            `source .venv/bin/activate`
1. Check CUDA version:
nvidia-smi
2. Install matching PyTorch version:
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124




# last worked
python3 -m venv .venv
source .venv/bin/activate

# Torch: cu126 build — matches your driver's CUDA ceiling, and is new enough
# to have register_constant (needs 2.8+; current cu126 stable is well past that)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# Unsloth: no version-pinned bracket — let it resolve transformers/trl/peft/
# torchao/xformers/bitsandbytes against whatever torch you just installed
pip install --upgrade --no-cache-dir unsloth unsloth_zoo