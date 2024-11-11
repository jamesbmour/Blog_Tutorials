# Streamlit app to interact with the Ollama language model
# File Name: app.py
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import os

# Load environment variables from a .env file
load_dotenv()


# Function to configure the Streamlit page layout and settings
def configure_page():
    st.set_page_config(
        page_title="Ollama Chat App",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title(f"💬 Streamlit Chat App: {st.session_state.model}")
    with st.expander("Check State"):
        if st.button("Clear Chat"):
            st.session_state.messages = [
                SystemMessage(content="You are a helpful AI assistant.")
            ]
            st.rerun()
            
        
        if st.button("Clear Cache"):
            st.cache_data.clear()
            st.cache_resource.clear()
        
        st.write(st.session_state)




# Function to update the system prompt
def sidebar_model_config():
    with st.form("model_config"):
        st.session_state.model = st.selectbox("Select Model", ("llama3.2", "llama3.2:1b", "qwen2.5:0.5b", "gpt-3.5-turbo"))
        new_prompt = st.text_area(
            "Change System Prompt:",
            value=st.session_state.messages[0].content if "messages" in st.session_state else "You are a helpful AI assistant.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Max Tokens", value="2048", key="max_tokens") 
            st.text_input("Stop", value="", key="stop")
            st.slider("Top P", 0.0, 1.0, 0.5, key="top_p")
            
            
        with col2:
            st.slider("Frequency Penalty", 0.0, 2.0, 0.0, key="frequency_penalty")
            st.slider("Presence Penalty", 0.0, 2.0, 0.0, key="presence_penalty")
            st.slider("Stop Sequence", 0.0, 2.0, 1.0, key="stop_sequence")
        
        

        # Update the system prompt if the form is submitted
        if st.form_submit_button("Update Config"):
            if "messages" in st.session_state and len(st.session_state.messages) > 0:
                st.session_state.messages[0] = SystemMessage(content=new_prompt)
            else:
                st.session_state.messages = [SystemMessage(content=new_prompt)]
            st.success("System prompt updated.")
            st.rerun()

def handle_model_config():
    with st.expander("Model Config"):
        sidebar_model_config()
        
        
# Function to display and handle sidebar interactions
def handle_sidebar():
    
    
    st.sidebar.divider()
    
    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.rerun()
        
    
    if st.sidebar.button("Clear Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()


    st.sidebar.markdown("---")
    st.sidebar.markdown("### Model Information")
    st.sidebar.write(f"Current Model: {selected_model}")
    


@st.cache_resource
def get_chat_model(model_name):
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model_name,
            streaming=True,
        )
    return ChatOllama(model=model_name, streaming=True)


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
def handle_user_input(chat_model):
    if prompt := st.chat_input("What would you like to know?"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for chunk in chat_model.stream(st.session_state.messages):
                if chunk.content:  # Update the response content
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append(AIMessage(content=full_response))


###########################################################################
#########################  Main execution flow  ###########################
###########################################################################

configure_page()

# selected_model = handle_sidebar()
handle_model_config()
chat_model = get_chat_model(st.session_state.model)

# Initialize the chat history in the session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

display_chat_messages()

handle_user_input(chat_model)

