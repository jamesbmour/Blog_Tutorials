# Streamlit app to interact with language models using LangChain, OllamaEmbeddings, and Chroma
# File Name: app.py

import streamlit as st
from dotenv import load_dotenv
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
import os
import tempfile

# Load environment variables from a .env file
load_dotenv()

# Function to configure the Streamlit page layout and settings
def configure_page():
    st.set_page_config(
        page_title="PDF Chat with LangChain, Ollama, and Chroma",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("📄🤖 Chat with Your PDF using LangChain, Ollama, and Chroma")
    with st.expander("Check State"):
        st.write(st.session_state)

# Function to display and handle sidebar interactions
def handle_sidebar():
    st.sidebar.header("Configuration")
    
    # Model Selection
    selected_model = st.sidebar.selectbox(
        "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b", "gpt-3.5-turbo")
    )
    st.session_state.model = selected_model
    
    st.sidebar.divider()
    
    # PDF Upload
    uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        if "vector_store" not in st.session_state:
            with st.spinner("Processing PDF..."):
                try:
                    documents = load_pdf(uploaded_file)
                    texts = split_text(documents)
                    embeddings = get_embeddings()
                    vector_store = create_vector_store(texts, embeddings)
                    st.session_state.vector_store = vector_store
                    st.success("PDF processed and indexed successfully!")
                except Exception as e:
                    st.error(f"Error processing PDF: {e}")
    
    st.sidebar.divider()
    
    # Chat Management
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.session_state.vector_store = None
        st.rerun()
    
    if st.sidebar.button("Clear Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Model Information")
    st.sidebar.write(f"Current Model: {selected_model}")
    return selected_model

@st.cache_resource
def get_chat_model(model_name):
    if model_name == "gpt-3.5-turbo":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            streaming=True,
        )
    return ChatOllama(model=model_name, streaming=True)

@st.cache_resource
def get_embeddings():
    return OllamaEmbeddings(
        model="mxbai-embed-large"
    )

def load_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name
    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()
    os.unlink(tmp_file_path)  # Clean up the temporary file
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_documents(documents)
    return texts

def create_vector_store(texts, embeddings):
    # Define the directory where Chroma will store its data
    chroma_persist_directory = os.path.join(tempfile.gettempdir(), "chroma_db")
    
    # Initialize Chroma vector store
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=chroma_persist_directory
    )
    # Persist the vector store to disk
    vector_store.persist()
    return vector_store

# Function to display the chat messages on the screen
def display_chat_messages():
    for message in st.session_state.messages[1:]:
        if isinstance(message, HumanMessage):  # Display user messages
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):  # Display AI responses
            with st.chat_message("assistant"):
                st.write(message.content)

# Function to handle user input and update the chat conversation
def handle_user_input(chat_model, retriever):
    if prompt := st.chat_input("Ask something about your PDF"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                # Use the RetrievalQA chain to get the response
                response = chat_model.run(prompt)
                full_response = response
                message_placeholder.markdown(full_response)
                st.session_state.messages.append(AIMessage(content=full_response))
            except Exception as e:
                message_placeholder.markdown("❌ An error occurred while generating the response.")
                st.error(f"Error: {e}")

def main():
    configure_page()
    selected_model = handle_sidebar()
    chat_model = get_chat_model(selected_model)
    
    # Initialize the chat history in the session state if not already present
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
    
    # Initialize vector store if PDF is uploaded
    if "vector_store" in st.session_state:
        retriever = st.session_state.vector_store.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=chat_model,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=False,
        )
        chat_model_with_retrieval = qa_chain
    else:
        chat_model_with_retrieval = chat_model
    
    display_chat_messages()
    handle_user_input(chat_model_with_retrieval, retriever=None if "vector_store" not in st.session_state else st.session_state.vector_store.as_retriever())

if __name__ == "__main__":
    main()