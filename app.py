import streamlit as st
from dotenv import load_dotenv
import os
import base64



# Import the get_response function from your backend logic
from query_data import get_response  # Make sure to replace with the actual module name

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()


@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;

}}



[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}


</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


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
                break
    else:
        st.write("Please enter a question.")
