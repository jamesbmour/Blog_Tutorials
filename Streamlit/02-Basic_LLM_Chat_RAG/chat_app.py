# ----------------------- Imports -----------------------
# 1. Standard Library Imports
import os
import shutil
import tempfile

# 2. Third-Party Imports
import streamlit as st
from dotenv import load_dotenv

# 3. LangChain Imports
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()


# ----------------------- App Configuration -----------------------
def configure_page():
    st.set_page_config(
        page_title="PDF Chat App",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("💬 Chat with your PDF")
    with st.expander("Check State"):
        st.write(st.session_state)


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = None
    if "persist_directory" not in st.session_state:
        st.session_state.persist_directory = None
    if "model" not in st.session_state:
        st.session_state.model = "gpt-3.5-turbo"


# ----------------------- Model Setup -----------------------
@st.cache_resource
def get_chat_model(model_name):
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            streaming=True,
        )
    return ChatOllama(model=model_name, streaming=True)


@st.cache_resource
def get_embeddings():
    return OllamaEmbeddings(model="mxbai-embed-large")


# ----------------------- PDF Processing -----------------------
def process_pdf(pdf_file):
    tmp_file_path = save_temp_pdf(pdf_file)
    documents = load_pdf(tmp_file_path)
    chunks = split_pdf(documents)
    persist_directory = create_chroma_persist_directory()
    vectorstore = create_vectorstore(chunks, persist_directory)
    os.unlink(tmp_file_path)
    return vectorstore


def save_temp_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        return tmp_file.name


def load_pdf(tmp_file_path):
    loader = PyPDFLoader(tmp_file_path)
    return loader.load()


def split_pdf(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )
    return text_splitter.split_documents(documents)


def create_chroma_persist_directory():
    persist_directory = "db"
    st.session_state.persist_directory = persist_directory
    return persist_directory


def create_vectorstore(chunks, persist_directory):
    embeddings = get_embeddings()
    return Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=persist_directory
    )


# ----------------------- Chat Interface -----------------------
def initialize_conversation(vectorstore, chat_model):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        verbose=True,
    )


def display_chat_messages():
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)
        elif isinstance(message, SystemMessage):
            with st.chat_message("system"):
                st.write(message.content)


def handle_user_input(conversation):
    if prompt := st.chat_input("Ask questions about your PDF"):
        user_message = HumanMessage(content=prompt)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                response = conversation({"question": prompt})
                answer = response.get("answer", "I'm not sure how to respond to that.")
            except Exception as e:
                answer = f"Error: {e}"
            message_placeholder.markdown(answer)
            assistant_message = AIMessage(content=answer)
            st.session_state.messages.append(assistant_message)


# ----------------------- Sidebar Functions -----------------------
def handle_sidebar():
    selected_model = st.sidebar.selectbox(
        "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b", "gpt-3.5-turbo")
    )
    st.session_state.model = selected_model

    st.sidebar.divider()

    if st.sidebar.button("Clear Chat"):
        clear_chat()

    if st.sidebar.button("Clear Cache"):
        clear_cache()

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Model Information")
    st.sidebar.write(f"Current Model: {selected_model}")
    return selected_model


def clear_chat():
    st.session_state.messages = []
    st.session_state.conversation = None
    cleanup_chroma_db()
    st.rerun()


def clear_cache():
    st.cache_data.clear()
    st.cache_resource.clear()


def cleanup_chroma_db():
    persist_directory = st.session_state.get("persist_directory")
    if persist_directory and os.path.exists(persist_directory):
        try:
            shutil.rmtree(persist_directory)
            st.session_state.persist_directory = None
        except Exception as e:
            st.error(f"Error cleaning up Chroma DB: {e}")


# ----------------------- PDF Upload Handler -----------------------
def handle_pdf_upload(pdf_file, chat_model):
    if st.session_state.pdf_processed != pdf_file.name:
        with st.spinner("Processing PDF..."):
            cleanup_chroma_db()
            vectorstore = process_pdf(pdf_file)
            st.session_state.conversation = initialize_conversation(
                vectorstore, chat_model
            )
            st.session_state.pdf_processed = pdf_file.name
            st.session_state.messages = []
            st.success("PDF processed successfully!")
    display_chat_messages()
    if st.session_state.conversation:
        handle_user_input(st.session_state.conversation)


# ----------------------- Main Application -----------------------
def main():
    configure_page()
    initialize_session_state()
    selected_model = handle_sidebar()
    chat_model = get_chat_model(selected_model)

    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if pdf_file:
        handle_pdf_upload(pdf_file, chat_model)
    else:
        st.info("Please upload a PDF file to start chatting.")


if __name__ == "__main__":
    main()
