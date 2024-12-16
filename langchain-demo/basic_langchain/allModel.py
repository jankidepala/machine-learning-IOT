import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
my_key = os.getenv("openKey")

# print('My Key:'+ my_key)
# llm = ChatOpenAI(model="gpt-4o")
# result = llm.invoke("What is AI?")

# ---- Anthropic Chat Model Example ----

# Create a Anthropic model
# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
# print(f"Answer from Anthropic: {result.content}")

# ---- Google Chat Model Example ----

# https://console.cloud.google.com/gen-app-builder/engines
# # https://ai.google.dev/gemini-api/docs/models/gemini
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# messages='asd'
# result = model.invoke(messages)
# print(f"Answer from Google: {result.content}")