import streamlit as st
from dotenv import load_dotenv
import os

# Import the get_response function from your backend logic
from query_data import get_response  # Make sure to replace with the actual module name

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

st.title("Book Information Chatbot")

st.write("Ask a question about the books:")

query_text = st.text_input("Your Question")

if st.button("Submit"):
    if query_text:
        formatted_response, sources = get_response(query_text)
        # response_parts = formatted_response.split('\nSources: ')
        # response_text = response_parts[0].replace('Response: ', '')
        # content_start = formatted_response.find("content='") + len("content='")
        print(formatted_response)
        st.write("### Response")
        st.write(formatted_response)

        if sources:
            st.write("### Sources")
            for source in sources:
                st.write(f"- {source}")
    else:
        st.write("Please enter a question.")
