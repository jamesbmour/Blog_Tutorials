# Advanced Indexing Techniques with LlamaIndex and Ollama: Part 2

Welcome back to our deep dive into LlamaIndex and Ollama! In Part 1, we covered the essentials of setting up and using these powerful tools for efficient information retrieval. Now, it’s time to explore advanced indexing techniques that will elevate your document processing and querying capabilities to the next level.

## 1. Introduction

Before we proceed, let’s quickly recap the key takeaways from Part 1:

- Setting up LlamaIndex and Ollama
- Creating a basic index
- Performing simple queries

In this part, we’ll dive into different index types, learn how to customize index settings, manage multiple documents, and explore advanced querying techniques. By the end, you’ll have a robust understanding of how to leverage LlamaIndex and Ollama for complex information retrieval tasks.

If you haven’t set up your environment yet, make sure to refer back to Part 1 for detailed instructions on installing and configuring LlamaIndex and Ollama.

## 2. Exploring Different Index Types

LlamaIndex offers various index types, each tailored to different use cases. Let’s explore the four main types:

### 2.1 List Index

The List Index is the simplest form of indexing in LlamaIndex. It’s an ordered list of text chunks, ideal for straightforward use cases.


```python
from llama_index.core import ListIndex, SimpleDirectoryReader, VectorStoreIndex
from dotenv import load_dotenv
from llama_index.llms.ollama import  Ollama
from llama_index.core import Settings
from IPython.display import Markdown, display
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb
from IPython.display import HTML
# make markdown display text color green for all cells
# Apply green color to all Markdown output
def display_green_markdown(text):
    green_style = """
    <style>
    .green-output {
        color: green;
    }
    </style>
    """
    green_markdown = f'<div class="green-output">{text}</div>'
    display(HTML(green_style + green_markdown))


# set the llm to ollama
Settings.llm = Ollama(model='phi3', base_url='http://localhost:11434',temperature=0.1)

load_dotenv()

documents = SimpleDirectoryReader('data').load_data()
index = ListIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What is llama index used for?")

display_green_markdown(response)
```


**Pros:**

- Simple and quick to create
- Best suited for small document sets

**Cons:**

- Less efficient with large datasets
- Limited semantic understanding

### 2.2 Vector Store Index

The Vector Store Index leverages embeddings to create a semantic representation of your documents, enabling more sophisticated searches.


```python
# Create Chroma client
chroma_client = chromadb.EphemeralClient()

# Define collection name
collection_name = "quickstart"

# Check if the collection already exists
existing_collections = chroma_client.list_collections()

if collection_name in [collection.name for collection in existing_collections]:
    chroma_collection = chroma_client.get_collection(collection_name)
    print(f"Using existing collection '{collection_name}'.")
else:
    chroma_collection = chroma_client.create_collection(collection_name)
    print(f"Created new collection '{collection_name}'.")

# Set up embedding model
embed_model = OllamaEmbedding(
    model_name="snowflake-arctic-embed",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"prostatic": 0},
)

# Load documents
documents = SimpleDirectoryReader("./data/paul_graham/").load_data()

# Set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# Create query engine and perform query
query_engine = index.as_query_engine()
response = query_engine.query("What is llama index best suited for?")
display_green_markdown(response)

```


This index type excels in semantic search and scalability, making it ideal for large datasets.

### 2.3 Tree Index

The Tree Index organizes information hierarchically, which is beneficial for structured data.


```python
from llama_index.core import TreeIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
tree_index = TreeIndex.from_documents(documents)
query_engine = tree_index.as_query_engine()
response = query_engine.query("Explain the tree index structure.")
display_green_markdown(response)
```

Tree indices are particularly effective for data with natural hierarchies, such as organizational structures or taxonomies.

### 2.4 Keyword Table Index

The Keyword Table Index is optimized for efficient keyword-based retrieval.


```python
from llama_index.core import KeywordTableIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data/paul_graham').load_data()
keyword_index = KeywordTableIndex.from_documents(documents)
query_engine = keyword_index.as_query_engine()
response = query_engine.query("What is the keyword table index in llama index?")
display_green_markdown(response)
```

This index type is ideal for scenarios that require quick lookups based on specific keywords.

## 3. Customizing Index Settings

### 3.1 Chunking Strategies

Effective text chunking is crucial for index performance. LlamaIndex provides various chunking methods:


```python
from llama_index.core.node_parser import SimpleNodeParser

parser = SimpleNodeParser.from_defaults(chunk_size=1024)

documents = SimpleDirectoryReader('data').load_data()
nodes = parser.get_nodes_from_documents(documents)
print(nodes[0])
```

Experiment with different chunking strategies to find the optimal balance between context preservation and query performance.

### 3.2 Embedding Models

LlamaIndex supports various embedding models. Here’s how you can use Ollama for embeddings:


```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.ollama import OllamaEmbedding

embed_model = OllamaEmbedding(
    model_name="snowflake-arctic-embed",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0},
)
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = index.as_query_engine()
response = query_engine.query("What is an embedding model used for in LlamaIndex?")
display_green_markdown(response)
```

Experiment with different Ollama models and adjust parameters to optimize embedding quality for your specific use case.

## 4. Handling Multiple Documents

### 4.1 Creating a Multi-Document Index

LlamaIndex simplifies the process of creating indices from multiple documents of various types:



```python
txt_docs = SimpleDirectoryReader('data/paul_graham').load_data()
web_docs = SimpleDirectoryReader('web_pages').load_data()
data = txt_docs  + web_docs
all_docs = txt_docs  + web_docs
index = VectorStoreIndex.from_documents(all_docs)

query_engine = index.as_query_engine()
response = query_engine.query("How do you create a multi-document index in LlamaIndex?")
display_green_markdown(response)
```

### 4.2 Cross-Document Querying

To effectively query across multiple documents, you can implement relevance scoring and manage context boundaries:


```python
from llama_index.core import QueryBundle
from llama_index.core.query_engine import RetrieverQueryEngine

retriever = index.as_retriever(similarity_top_k=5)
query_engine = RetrieverQueryEngine.from_args(retriever, response_mode="compact")
query = QueryBundle("How do you query across multiple documents?")
response = query_engine.query(query)
display_green_markdown(response)
```

## 5. Conclusion and Next Steps

In this second part of our LlamaIndex and Ollama series, we explored advanced indexing techniques, including:

- Different index types and their use cases
- Customizing index settings for optimal performance
- Handling multiple documents and cross-document querying


