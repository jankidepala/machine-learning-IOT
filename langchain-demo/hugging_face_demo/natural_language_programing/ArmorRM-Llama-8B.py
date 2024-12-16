# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="RLHFlow/ArmoRM-Llama3-8B-v0.1", trust_remote_code=True)