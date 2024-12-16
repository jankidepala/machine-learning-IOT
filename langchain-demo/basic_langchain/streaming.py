# API Reference:StrOutputParser | ChatPromptTemplate | ChatAnthropic

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-sonnet-20240229")

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
parser = StrOutputParser()
chain = prompt | model | parser

async for event in chain.astream_events({"topic": "parrot"}, version="v2"):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(event, end="|", flush=True)