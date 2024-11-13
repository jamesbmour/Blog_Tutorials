# Streamlit app to chat with PDFs using LangChain and Chroma Vector DB
# File Name: app.py

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

# Load environment variables
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
        if "persist_directory" in st.session_state:
            try:
                shutil.rmtree(st.session_state.persist_directory)
            except:
                pass
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
    # Create a temporary file to save the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        tmp_file_path = tmp_file.name

    # Load and process the PDF
    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_documents(documents)

    # Create a persist directory for Chroma
    persist_directory = f"chroma_db_{pdf_file.name}"
    st.session_state.persist_directory = persist_directory

    # Create vector store using Chroma
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=persist_directory
    )

    # Clean up the temporary file
    os.unlink(tmp_file_path)

    return vectorstore


def initialize_conversation(vectorstore, chat_model):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    conversation = ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # Retrieve top 3 most relevant chunks
        ),
        memory=memory,
        verbose=True,
    )

    return conversation


def display_chat_messages():
    for message in st.session_state.messages:
        role = "user" if message["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.write(message["content"])


def handle_user_input(conversation):
    if prompt := st.chat_input("Ask questions about your PDF"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = conversation({"question": prompt})
            answer = response["answer"]

            # Display the response
            message_placeholder.markdown(answer)

            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})


def main():
    configure_page()
    selected_model = handle_sidebar()
    chat_model = get_chat_model(selected_model)

    # Initialize session state for messages and conversation
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # File uploader
    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if pdf_file:
        if (
            "pdf_processed" not in st.session_state
            or st.session_state.pdf_processed != pdf_file.name
        ):
            with st.spinner("Processing PDF..."):
                # Clean up old Chroma database if it exists
                if "persist_directory" in st.session_state:
                    try:
                        shutil.rmtree(st.session_state.persist_directory)
                    except:
                        pass

                vectorstore = process_pdf(pdf_file)
                st.session_state.conversation = initialize_conversation(
                    vectorstore, chat_model
                )
                st.session_state.pdf_processed = pdf_file.name
                st.session_state.messages = (
                    []
                )  # Clear messages when new PDF is uploaded
                st.success("PDF processed successfully!")

        # Display chat interface
        display_chat_messages()

        if st.session_state.conversation:
            handle_user_input(st.session_state.conversation)
    else:
        st.info("Please upload a PDF file to start chatting.")


if __name__ == "__main__":
    main()
