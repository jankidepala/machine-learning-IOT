import os
from dotenv import load_dotenv
import openai
# concrete example
# from llama_index.core.llms import LLM
# from llama_index.llms.openai import OpenAI

my_key = os.getenv("OPENAI_API_KEY")
print('My Key present! ')

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document

documents = SimpleDirectoryReader("./assets").load_data()
document = Document(text="\n\n".join([doc.text for doc in documents]))
index = VectorStoreIndex.from_documents(documents)

print('Document Details on Page 1:')
print(document)
# print(len(documents), "\n")
# print(type(documents[1]))
# print(documents[1])

