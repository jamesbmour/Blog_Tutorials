import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding

#%%
# Set up Ollama
# ollama pull phi3
llm = Ollama(model="phi3")
Settings.llm = llm
# ollama pull snowflake-arctic-embed
embed_model = OllamaEmbedding(model_name="snowflake-arctic-embed")
Settings.embed_model = embed_model
# service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
#%%
# Define the path to your directory containing the sample.txt file
# directory_path = './data'
directory_path = 'llamaindex-series/data'

# Load documents
documents = SimpleDirectoryReader(directory_path).load_data()
#%%
# Create index
index = VectorStoreIndex.from_documents(documents, show_progress=True)
#%%
# Create query engine
query_engine = index.as_query_engine(llm=llm)
#%%
# Perform a query
response = query_engine.query("What is LlamaIndex?")
print(response)


