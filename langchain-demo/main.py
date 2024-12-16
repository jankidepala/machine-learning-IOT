import os
from dotenv import load_dotenv
import openai
import langchain

from langchain_openai import ChatOpenAI
from langchain_openai import ChatOpenAI

my_key = os.getenv("openKey")

print('My Key:'+ my_key)
llm = ChatOpenAI(api_key=my_key)
result = llm.invoke("What is AI?")

# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a world class technical documentation writer."),
#     ("user", "{input}")
# ])

print("Full result:")
# print(result)
print("Content only:")
print(result.content)
