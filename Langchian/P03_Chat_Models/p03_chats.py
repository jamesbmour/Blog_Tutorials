# %%
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_openai import OpenAI
import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


# %%
template = """Question: {question}

Answer: Let's think step by step."""
# %%
prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="qwen2.5:0.5b")

chain = prompt | model
# %%
print(chain.invoke({"question": "What is LangChain?"}))
# %%

OPENAI_ORGANIZATION = getpass()

os.environ["OPENAI_ORGANIZATION"] = OPENAI_ORGANIZATION


# %%
llm = OpenAI()

print(llm.invoke("What is LangChain?"))

# %%
