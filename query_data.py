import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

openai_api_key = os.environ['OPENAI_API_KEY']

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a book chatbot.
Answer the question based only on the following context:

{context}

or say "out of context or Sorry I cannot answer that" if there is no context provided

---

Answer the question based on the above context only: {question}
"""

def get_response(query_text):
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        return "Unable to find matching results.", []

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    
    return response_text.content, sources
