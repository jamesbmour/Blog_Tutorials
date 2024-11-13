# VIDEO_TITLE:
# FILE_NAME: 01_LLM.py
# %%
from langchain_ollama.chat_models import ChatOllama
import getpass
import os
from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv

# pip install langchain-ollama langchain-openai
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter OpenAI API key: ")
# %%
# SECTION 1: ChatOllama
llm = ChatOllama(model="qwen2.5:0.5b", temperature=0.5)
r = llm.invoke("Hello, how are you today?")
print(r)
print(r.content)

# %%
# SECTION 2: ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=52)
r = llm.invoke("Hello, how are you today?")
print(r.content)

# %%
# SECTION 3: OpenRouter
llm = ChatOpenAI(
    openai_api_key=getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.2-3b-instruct:free",
    temperature=0.5,
    max_tokens=100,
)

result = llm.invoke("Hello, how are you today?")
print(result.content)
