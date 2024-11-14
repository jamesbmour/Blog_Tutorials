# -------------- Imports --------------
import os
import shutil
import tempfile
import streamlit as st
from dotenv import load_dotenv
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
    """Configure the Streamlit page settings for the chat app."""
    # Set the page title, icon, layout, and initial sidebar state
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
    """Initialize the session state variables for the chat app."""
    # Initialize messages history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Initialize conversation chain
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    # Initialize PDF processing status
    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = None
    # Initialize vector store persistence directory
    if "persist_directory" not in st.session_state:
        st.session_state.persist_directory = None
    # Initialize default model
    if "model" not in st.session_state:
        st.session_state.model = "llama3.2"


# ----------------------- Model Setup -----------------------
@st.cache_resource
def get_chat_model(model_name):
    """Get the chat model based on the selected model name."""
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            streaming=True,
        )
    return ChatOllama(model=model_name, streaming=True)


@st.cache_resource
def get_embeddings():
    """Get the embeddings model for processing the PDF."""
    return OllamaEmbeddings(model="mxbai-embed-large")


# ----------------------- PDF Processing -----------------------
def process_pdf(pdf_file):
    """Process the uploaded PDF file and create a vector store."""
    # Save the uploaded PDF to a temporary file
    tmp_file_path = save_temp_pdf(pdf_file)
    # Load documents from the temporary PDF file
    documents = load_pdf(tmp_file_path)
    # Split the loaded documents into chunks
    chunks = split_pdf(documents)
    # Create a directory for persisting the vector store
    persist_directory = create_chroma_persist_directory()
    # Create a vector store from the document chunks
    vectorstore = create_vectorstore(chunks, persist_directory)
    # Remove the temporary PDF file after processing
    os.unlink(tmp_file_path)
    return vectorstore


def save_temp_pdf(pdf_file):
    """Save the uploaded PDF file to a temporary file and return the file path."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        return tmp_file.name


def load_pdf(tmp_file_path):
    """Load the PDF file using PyPDFLoader and return the documents."""
    loader = PyPDFLoader(tmp_file_path)
    return loader.load()


def split_pdf(documents):
    """Split the PDF documents into chunks for processing."""
    # ["\n\n", "\n", " ", ""]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_documents(documents)


def create_chroma_persist_directory():
    """Create a directory for persisting the Chroma vector store."""
    persist_directory = "db"
    # Store the directory name in session state
    st.session_state.persist_directory = persist_directory
    return persist_directory


def create_vectorstore(chunks, persist_directory):
    """Create a Chroma vector store from the document chunks."""
    embedding_model = get_embeddings()
    # Create a Chroma vector store from the documents and embeddings
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )


# ----------------------- Chat Interface -----------------------
def initialize_conversation(vectorstore, chat_model):
    """Initialize a conversational retrieval chain with the given vector store and chat model."""
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Initialize a conversational retrieval chain with given parameters
    return ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 5}
        ),
        memory=memory,
        verbose=True,
    )


def display_chat_messages():
    """Display the chat messages in the chat interface."""
    # Iterate through each message in the chat history
    for message in st.session_state.messages:
        # Check if the message is from the user
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        # Check if the message is from the assistant
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)
        # Check if the message is a system message
        elif isinstance(message, SystemMessage):
            with st.chat_message("system"):
                st.write(message.content)


def handle_user_input(conversation):
    """Handle user input and chat interactions with the assistant."""
    # Get user input from the chat input widget
    if prompt := st.chat_input("Ask questions about your PDF"):
        # Create a HumanMessage instance with the input prompt and append it to session state
        user_message = HumanMessage(content=prompt)
        st.session_state.messages.append(user_message)
        # Display the user message in the chat
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            # Wrap the conversation logic in a try-except block
            try:
                # Get the response from the conversation model
                response = conversation({"question": prompt})
                answer = response.get("answer", "I'm not sure how to respond to that.")
            except Exception as e:
                # Handle any exceptions and set answer to the error message
                answer = f"Error: {e}"
            message_placeholder.markdown(answer)
            # Create an AIMessage instance with the answer and append it to session state
            assistant_message = AIMessage(content=answer)
            st.session_state.messages.append(assistant_message)


# ----------------------- Sidebar Functions -----------------------
def handle_sidebar():
    """Handle the sidebar interactions and return the selected model."""
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
    """Clear the chat history and reset the conversation state."""
    st.session_state.messages = []
    st.session_state.conversation = None
    cleanup_chroma_db()
    st.rerun()


def clear_cache():
    """Clear the Streamlit cache to reset the application state."""
    st.cache_data.clear()
    st.cache_resource.clear()


def cleanup_chroma_db():
    """Clean up the Chroma database directory if it exists."""
    persist_directory = st.session_state.get("persist_directory")

    # Check if the directory exists and attempt to remove it
    if persist_directory and os.path.exists(persist_directory):
        try:
            shutil.rmtree(persist_directory)
            st.session_state.persist_directory = None
        except Exception as e:
            st.error(f"Error cleaning up Chroma DB: {e}")


# ----------------------- PDF Upload Handler -----------------------
def handle_pdf_upload(pdf_file, chat_model):
    """Handle the PDF upload and process the PDF to initialize the chat conversation."""
    # Check if the PDF has already been processed
    if st.session_state.pdf_processed != pdf_file.name:
        # Display a processing message while the PDF is being processed
        with st.spinner("Processing PDF..."):
            # Clean up the previous Chroma database if it exists
            cleanup_chroma_db()
            # Process the uploaded PDF to create a vector store
            vectorstore = process_pdf(pdf_file)
            # Initialize a new conversation with the vector store and chat model
            st.session_state.conversation = initialize_conversation(
                vectorstore, chat_model
            )
            # Mark the PDF as processed in the session state
            st.session_state.pdf_processed = pdf_file.name
            # Reset the messages in the session state
            st.session_state.messages = []
            st.success("PDF processed successfully!")
    # Display chat messages if available
    display_chat_messages()

    # Handle user input if a conversation is initialized
    if st.session_state.conversation:
        handle_user_input(st.session_state.conversation)

# ----------------------- Main Application -----------------------
def main():
    """Main function to run the Streamlit app."""
    configure_page()
    # Initialize the session state for maintaining chat state
    initialize_session_state()
    # Handle sidebar interactions and get the selected model
    selected_model = handle_sidebar()
    # Get the chat model based on the selected model from the sidebar
    chat_model = get_chat_model(selected_model)

    # File uploader for PDF files
    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

    # If a PDF file is uploaded, handle processing and chat initialization
    if pdf_file:
        handle_pdf_upload(pdf_file, chat_model)
    else:
        st.info("Please upload a PDF file to start chatting.")


if __name__ == "__main__":
    main()