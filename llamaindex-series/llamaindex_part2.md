## 2. Exploring Different Index Types
### 2.1 List Index


```python
from llama_index.core import ListIndex, SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv()

documents = SimpleDirectoryReader('data').load_data()
list_index = ListIndex.from_documents(documents)

query_engine = list_index.as_query_engine()
response = query_engine.query("What is the capital of France?")
print(response)
```

    LlamaIndex provides a simple interface to query your data using natural language.




### 2.2 Vector Store Index
The Vector Store Index uses embeddings to create a semantic representation of your documents.


```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.vector_stores import FaissVectorStore
documents = SimpleDirectoryReader('data').load_data()
vector_store = FaissVectorStore(dim=512)  # Adjust dimension based on your embedding modelindex = VectorStoreIndex.from_documents(documents, vector_store=vector_store)
query_engine = index.as_query_engine()
response = query_engine.query("What are the main themes in Shakespeare's plays?")
print(response)
```

## 2.3 Tree Index


```python
from llama_index.core import TreeIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
tree_index = TreeIndex.from_documents(documents)
query_engine = tree_index.as_query_engine()
response = query_engine.query("Explain the structure of the human respiratory system.")
print(response)
```

    LlamaIndex is a powerful data framework that provides tools and techniques to connect custom data sources to large language models (LLMs). It offers features such as data ingestion, data indexing, a query interface, LLM integration, customization options, and scalability. Use cases for LlamaIndex include question-answering systems, domain-specific chatbots, semantic search applications, and document analysis and summarization.


## 2.4 Keyword Table Index


```python
from llama_index.core import KeywordTableIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
keyword_index = KeywordTableIndex.from_documents(documents)
query_engine = keyword_index.as_query_engine()
response = query_engine.query("What are the symptoms of influenza?")
print(response)
```

    Empty Response


## 3. Customizing Index Settings

### 3.1 Chunking Strategies


```python
# from llama_index import SimpleDirectoryReader
# from llama_index.node_parser import SimpleNodeParser
# Fixed size chunksparser = SimpleNodeParser.from_defaults(chunk_size=1024)
# Sentence-based chunkingparser = SimpleNodeParser.from_defaults(chunk_size=None, chunk_overlap=0)
documents = SimpleDirectoryReader('data').load_data()
nodes = parser.get_nodes_from_documents(documents)
```

## 3.2 Embedding Models


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
response = query_engine.query("What are the main themes in Shakespeare's plays?")
print(response)
```

    LlamaIndex is a powerful data framework designed to help developers build AI applications with large language models (LLMs). It provides a set of tools and techniques to connect custom data sources to LLMs, enabling more accurate and context-aware responses. Key features of LlamaIndex include data ingestion, data indexing, query interface, LLM integration, customization, and scalability. Use cases for LlamaIndex include question-answering systems, chatbots with domain-specific knowledge, semantic search applications, and document analysis and summarization.


## 4. Handling Multiple Documents

### 4.1 Creating a Multi-Document Index


```python
# Load documents from different sourcespdf_docs = SimpleDirectoryReader('pdfs').load_data()
pdf_docs = SimpleDirectoryReader('pdfs').load_data()
csv_docs = SimpleDirectoryReader('csvs', file_extractor={".csv": "PandasCSVReader"}).load_data()
web_docs = SimpleDirectoryReader('web_pages', file_extractor={".html": "BeautifulSoupWebReader"}).load_data()
all_docs = pdf_docs + csv_docs + web_docs
index = VectorStoreIndex.from_documents(all_docs)
```

    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/pdfs/doc1.pdf with error: RetryError[<Future at 0x330933d90 state=finished raised EmptyFileError>]. Skipping...
    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/pdfs/doc2.pdf with error: RetryError[<Future at 0x16f818050 state=finished raised EmptyFileError>]. Skipping...
    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/csvs/doc1.csv with error: 'str' object has no attribute 'load_data'. Skipping...
    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/web_pages/doc1.html with error: 'str' object has no attribute 'load_data'. Skipping...
    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/web_pages/doc2.html with error: 'str' object has no attribute 'load_data'. Skipping...


## 4.2 Cross-Document Querying


```python
from llama_index.core import QueryBundle
from llama_index.core.query_engine import RetrieverQueryEngine

retriever = index.as_retriever(similarity_top_k=5)
query_engine = RetrieverQueryEngine.from_args(retriever, response_mode="compact")
query = QueryBundle("What are the common themes across all documents?")
response = query_engine.query(query)
print(response)
```

    Empty Response


# 5. Updating and Managing Indices
## 5.1 Adding New Documents to Existing Indices


```python
new_doc = SimpleDirectoryReader('new_data').load_data()[0]
index.insert(new_doc)
```

    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/pdfs/doc1.pdf with error: RetryError[<Future at 0x3324ed010 state=finished raised EmptyFileError>]. Skipping...
    Failed to load file /Users/james/GitHub/blog_tutorials/llamaindex-series/pdfs/doc2.pdf with error: RetryError[<Future at 0x3324f57d0 state=finished raised EmptyFileError>]. Skipping...



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[13], line 1
    ----> 1 new_doc = SimpleDirectoryReader('pdfs').load_data()[0]
          2 index.insert(new_doc)


    IndexError: list index out of range


## 5.3 Index Persistence and Serialization


```python
from llama_index.core import StorageContext, load_index_from_storage

# Save indexindex.storage_context.persist("path/to/save")
# Load indexfrom llama_index import load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir="path/to/save")
loaded_index = load_index_from_storage(storage_context)
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[14], line 5
          1 from llama_index.core import StorageContext, load_index_from_storage
          3 # Save indexindex.storage_context.persist("path/to/save")
          4 # Load indexfrom llama_index import load_index_from_storage
    ----> 5 storage_context = StorageContext.from_defaults(persist_dir="path/to/save")
          6 loaded_index = load_index_from_storage(storage_context)


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/storage/storage_context.py:110, in StorageContext.from_defaults(cls, docstore, index_store, vector_store, image_store, vector_stores, graph_store, property_graph_store, persist_dir, fs)
        108         vector_stores[IMAGE_VECTOR_STORE_NAMESPACE] = image_store
        109 else:
    --> 110     docstore = docstore or SimpleDocumentStore.from_persist_dir(
        111         persist_dir, fs=fs
        112     )
        113     index_store = index_store or SimpleIndexStore.from_persist_dir(
        114         persist_dir, fs=fs
        115     )
        116     graph_store = graph_store or SimpleGraphStore.from_persist_dir(
        117         persist_dir, fs=fs
        118     )


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/storage/docstore/simple_docstore.py:57, in SimpleDocumentStore.from_persist_dir(cls, persist_dir, namespace, fs)
         55 else:
         56     persist_path = os.path.join(persist_dir, DEFAULT_PERSIST_FNAME)
    ---> 57 return cls.from_persist_path(persist_path, namespace=namespace, fs=fs)


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/storage/docstore/simple_docstore.py:74, in SimpleDocumentStore.from_persist_path(cls, persist_path, namespace, fs)
         59 @classmethod
         60 def from_persist_path(
         61     cls,
       (...)
         64     fs: Optional[fsspec.AbstractFileSystem] = None,
         65 ) -> "SimpleDocumentStore":
         66     """Create a SimpleDocumentStore from a persist path.
         67 
         68     Args:
       (...)
         72 
         73     """
    ---> 74     simple_kvstore = SimpleKVStore.from_persist_path(persist_path, fs=fs)
         75     return cls(simple_kvstore, namespace)


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/storage/kvstore/simple_kvstore.py:97, in SimpleKVStore.from_persist_path(cls, persist_path, fs)
         95 fs = fs or fsspec.filesystem("file")
         96 logger.debug(f"Loading {__name__} from {persist_path}.")
    ---> 97 with fs.open(persist_path, "rb") as f:
         98     data = json.load(f)
         99 return cls(data)


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/fsspec/spec.py:1298, in AbstractFileSystem.open(self, path, mode, block_size, cache_options, compression, **kwargs)
       1296 else:
       1297     ac = kwargs.pop("autocommit", not self._intrans)
    -> 1298     f = self._open(
       1299         path,
       1300         mode=mode,
       1301         block_size=block_size,
       1302         autocommit=ac,
       1303         cache_options=cache_options,
       1304         **kwargs,
       1305     )
       1306     if compression is not None:
       1307         from fsspec.compression import compr


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/fsspec/implementations/local.py:191, in LocalFileSystem._open(self, path, mode, block_size, **kwargs)
        189 if self.auto_mkdir and "w" in mode:
        190     self.makedirs(self._parent(path), exist_ok=True)
    --> 191 return LocalFileOpener(path, mode, fs=self, **kwargs)


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/fsspec/implementations/local.py:355, in LocalFileOpener.__init__(self, path, mode, autocommit, fs, compression, **kwargs)
        353 self.compression = get_compression(path, compression)
        354 self.blocksize = io.DEFAULT_BUFFER_SIZE
    --> 355 self._open()


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/fsspec/implementations/local.py:360, in LocalFileOpener._open(self)
        358 if self.f is None or self.f.closed:
        359     if self.autocommit or "w" not in self.mode:
    --> 360         self.f = open(self.path, mode=self.mode)
        361         if self.compression:
        362             compress = compr[self.compression]


    FileNotFoundError: [Errno 2] No such file or directory: '/Users/james/GitHub/blog_tutorials/llamaindex-series/path/to/save/docstore.json'


## 6. Advanced Querying Techniques

### 6.1 Query Preprocessing


```python
import re
def preprocess_query(query):
    # Normalize text    query = query.lower()
    # Remove special characters    query = re.sub(r'[^\w\s]', '', query)
    # Expand common abbreviations    query = query.replace("ai", "artificial intelligence")
    return query
preprocessed_query = preprocess_query("What's the latest in AI?")
response = query_engine.query(preprocessed_query)
```

### 6.2 Hybrid Search Strategies


```python

keyword_retriever = index.as_retriever(mode="keyword")
vector_retriever = index.as_retriever(mode="embedding")
def hybrid_retriever(query_bundle: QueryBundle):
    keyword_nodes = keyword_retriever.retrieve(query_bundle)
    vector_nodes = vector_retriever.retrieve(query_bundle)
    return list(set(keyword_nodes + vector_nodes))
query_engine = RetrieverQueryEngine.from_args(hybrid_retriever)
response = query_engine.query("What are the environmental impacts of renewable energy?")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[16], line 8
          6     return list(set(keyword_nodes + vector_nodes))
          7 query_engine = RetrieverQueryEngine.from_args(hybrid_retriever)
    ----> 8 response = query_engine.query("What are the environmental impacts of renewable energy?")


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/instrumentation/dispatcher.py:260, in Dispatcher.span.<locals>.wrapper(func, instance, args, kwargs)
        252 self.span_enter(
        253     id_=id_,
        254     bound_args=bound_args,
       (...)
        257     tags=tags,
        258 )
        259 try:
    --> 260     result = func(*args, **kwargs)
        261 except BaseException as e:
        262     self.event(SpanDropEvent(span_id=id_, err_str=str(e)))


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/base/base_query_engine.py:52, in BaseQueryEngine.query(self, str_or_query_bundle)
         50     if isinstance(str_or_query_bundle, str):
         51         str_or_query_bundle = QueryBundle(str_or_query_bundle)
    ---> 52     query_result = self._query(str_or_query_bundle)
         53 dispatcher.event(
         54     QueryEndEvent(query=str_or_query_bundle, response=query_result)
         55 )
         56 return query_result


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/instrumentation/dispatcher.py:260, in Dispatcher.span.<locals>.wrapper(func, instance, args, kwargs)
        252 self.span_enter(
        253     id_=id_,
        254     bound_args=bound_args,
       (...)
        257     tags=tags,
        258 )
        259 try:
    --> 260     result = func(*args, **kwargs)
        261 except BaseException as e:
        262     self.event(SpanDropEvent(span_id=id_, err_str=str(e)))


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/query_engine/retriever_query_engine.py:189, in RetrieverQueryEngine._query(self, query_bundle)
        185 """Answer a query."""
        186 with self.callback_manager.event(
        187     CBEventType.QUERY, payload={EventPayload.QUERY_STR: query_bundle.query_str}
        188 ) as query_event:
    --> 189     nodes = self.retrieve(query_bundle)
        190     response = self._response_synthesizer.synthesize(
        191         query=query_bundle,
        192         nodes=nodes,
        193     )
        194     query_event.on_end(payload={EventPayload.RESPONSE: response})


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/llama_index/core/query_engine/retriever_query_engine.py:144, in RetrieverQueryEngine.retrieve(self, query_bundle)
        143 def retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
    --> 144     nodes = self._retriever.retrieve(query_bundle)
        145     return self._apply_node_postprocessors(nodes, query_bundle=query_bundle)


    AttributeError: 'function' object has no attribute 'retrieve'



```python
import timeit
def benchmark_query(query_engine, query):
    return timeit.timeit(lambda: query_engine.query(query), number=100)
list_index_time = benchmark_query(list_index.as_query_engine(), "Sample query")
vector_index_time = benchmark_query(vector_index.as_query_engine(), "Sample query")
print(f"List Index: {list_index_time:.4f} seconds")
print(f"Vector Index: {vector_index_time:.4f} seconds")
```


```python
from llama_index.core.postprocessor import SimilarityPostprocessor

docs = SimpleDirectoryReader('web_pages').load_data()
index = VectorStoreIndex.from_documents(docs)
processingretriever = index.as_retriever(similarity_top_k=5)
query_engine = RetrieverQueryEngine.from_args(
    retriever,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)]
)
queryresponse = query_engine.query("What are the main causes of global warming?")
print(response)
```

    Empty Response



```python
from llama_index.core.query_engine import RouterQueryEngine

documents = SimpleDirectoryReader('data').load_data()
vector_index = VectorStoreIndex.from_documents(documents)
keyword_index = KeywordTableIndex.from_documents(documents)
vector_query_engine = vector_index.as_query_engine()
keyword_query_engine = keyword_index.as_query_engine()
# Create a router query enginerouter_query_engine = RouterQueryEngine.from_defaults(
query_engine_tools=[
    ("vector", vector_query_engine),
    ("keyword", keyword_query_engine),
]

# Example queryresponse = router_query_engine.query("What are the effects of climate change on biodiversity?")
print(response)
```

    Empty Response



```python

```
