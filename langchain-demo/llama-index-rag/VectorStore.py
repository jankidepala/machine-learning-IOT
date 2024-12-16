import os
from dotenv import load_dotenv
import openai
# concrete example
# from llama_index.core.llms import LLM
# from llama_index.llms.openai import OpenAI

my_key = os.getenv("OPENAI_API_KEY")
print(my_key)

# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document, Settings
# from llama_index.llms.openai import OpenAI

# documents = SimpleDirectoryReader("./assets").load_data()
# document = Document(text="\n\n".join([doc.text for doc in documents]))
# index = VectorStoreIndex.from_documents(documents)

# print('Document Details on Page 1:')
# print(document)
# print(len(documents), "\n")
# print(type(documents[1]))
# print(documents[1])


from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer

# set the LLM
llama2_7b_chat = "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e"
Settings.llm = Replicate(
    model=llama2_7b_chat,
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens": 300},
)

# set tokenizer to match LLM
Settings.tokenizer = AutoTokenizer.from_pretrained(
    "NousResearch/Llama-2-7b-chat-hf"
)

# set the embed model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5", max_length='200'
)

documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
index = VectorStoreIndex.from_documents(
    documents,
)