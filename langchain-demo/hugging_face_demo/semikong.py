# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("pentagoniac/SEMIKONG-8b-GPTQ")
model = AutoModelForCausalLM.from_pretrained("pentagoniac/SEMIKONG-8b-GPTQ")