from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 1. High-speed tokenization via Rust core
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 2. Model configuration & weight loading abstraction
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)

# Execution flow: Raw Text -> Token IDs -> Tensor Forward Pass -> Output Text
inputs = tokenizer("Python architecture is", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=10)

print("Generated Text:", tokenizer.decode(outputs[0], skip_special_tokens=True))