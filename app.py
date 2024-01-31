# app.py
import os

import streamlit as st
import openai
from dotenv import load_dotenv

# Set your OpenAI API key he
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

# Set your OpenAI API key here
# openai.api_key = 'your_api_key_here'

def get_openai_response(user_input):
    """
    This function sends the user input to OpenAI's Chat API and returns the model's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model for chat applications
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        # Extracting the text from the last response in the chat
        if response.choices:
            return response.choices[0].message['content'].strip()
        else:
            return "No response from the model."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app layout
st.title("Your Advanced Streamlit Chatbot")

user_input = st.text_input("What would you like to ask?")

if st.button("Submit"):
    if user_input:
        chatbot_response = get_openai_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")
    else:
        st.write("Please enter a question or message to get a response.")

