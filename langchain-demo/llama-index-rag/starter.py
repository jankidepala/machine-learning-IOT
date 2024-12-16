import os
from dotenv import load_dotenv
import openai
# concrete example
# from llama_index.core.llms import LLM
# from llama_index.llms.openai import OpenAI

my_key = os.getenv("OPENAI_API_KEY")
print('My Key present! ')

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./assets").load_data()
index = VectorStoreIndex.from_documents(documents)

print('Document Details on Page 1:')
print(type(documents), "\n")
print(len(documents), "\n")
print(type(documents[1]))


