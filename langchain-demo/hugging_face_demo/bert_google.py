import requests
import os
from dotenv import load_dotenv
my_key = os.getenv("HUGGING_FACE_API_KEY")
bearer_key='Bearer '+my_key

API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-base-uncased"
headers = {"Authorization": bearer_key}

print(my_key)
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "The answer to the universe is [MASK].",
})

print(output[0]['sequence'])