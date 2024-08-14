from llama_index.core import ListIndex, SimpleDirectoryReader

#%%
documents = SimpleDirectoryReader('data').load_data()
list_index = ListIndex.from_documents(documents)

query_engine = list_index.as_query_engine()
response = query_engine.query("What is the capital of France?")
print(response)

#%%
