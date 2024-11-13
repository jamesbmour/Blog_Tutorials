import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
import tempfile
import shutil

load_dotenv()


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


def handle_sidebar():
    selected_model = st.sidebar.selectbox(
        "Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b", "gpt-3.5-turbo")
    )
    st.session_state.model = selected_model
    st.sidebar.divider()
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.conversation = None
        # Clean up Chroma database
        cleanup_chroma_db()
        st.rerun()
    if st.sidebar.button("Clear Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Model Information")
    st.sidebar.write(f"Current Model: {selected_model}")
    return selected_model


def cleanup_chroma_db():
    if "persist_directory" in st.session_state:
        try:
            shutil.rmtree(st.session_state.persist_directory)
        except:
            pass


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
        tmp_file_path = tmp_file.name
    return tmp_file_path


def load_pdf(tmp_file_path):
    loader = PyPDFLoader(tmp_file_path)
    return loader.load()


def split_pdf(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )
    return text_splitter.split_documents(documents)


def create_chroma_persist_directory():
    persist_directory = f"db"
    st.session_state.persist_directory = persist_directory
    return persist_directory


def create_vectorstore(chunks, persist_directory):
    embeddings = get_embeddings()
    return Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=persist_directory
    )


def initialize_conversation(vectorstore, chat_model):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # Retrieve top 3 most relevant chunks
        ),
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
            response = conversation({"question": prompt})
            answer = response["answer"]
            message_placeholder.markdown(answer)
            assistant_message = AIMessage(content=answer)
            st.session_state.messages.append(assistant_message)


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None


def handle_pdf_upload(pdf_file, chat_model):
    if (
        "pdf_processed" not in st.session_state
        or st.session_state.pdf_processed != pdf_file.name
    ):
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


def main():
    configure_page()
    selected_model = handle_sidebar()
    chat_model = get_chat_model(selected_model)

    initialize_session_state()

    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if pdf_file:
        handle_pdf_upload(pdf_file, chat_model)
    else:
        st.info("Please upload a PDF file to start chatting.")


if __name__ == "__main__":
    main()
