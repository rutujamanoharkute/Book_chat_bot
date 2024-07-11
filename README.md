# Book Chatbot Based on Prof. Nik Bear Brown's Book
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/011144f9-2e2c-4d6d-a0b2-2c2fcc53291e">



#### Overview
This project creates a chatbot that answers questions based on Prof. Nik Bear Brown's book. It leverages Langchain, ChromaDB, and OpenAI to provide accurate and contextual responses through a Streamlit interface.

#### Installation

1. **Install Dependencies**

   **MacOS Users:**
   - First, install the `onnxruntime` dependency for ChromaDB using Conda:
     ```sh
     conda install onnxruntime -c conda-forge
     ```
   - If you face any issues, refer to this thread for additional help.

   **Windows Users:**
   - Follow the guide [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to install the Microsoft C++ Build Tools. Ensure you follow through to the last step to set the environment variable path.

   Now, run this command to install the dependencies listed in the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

2. **Install Markdown Dependencies:**
   ```sh
   pip install "unstructured[md]"
   ```

#### Create Database

To create the Chroma DB:
```sh
python create_database.py
```

#### Running the Streamlit App

To start the Streamlit app, run:
```sh
streamlit run app.py
```

#### OpenAI Setup

You'll need to set up an OpenAI account and set the OpenAI API key in your environment variable for this to work. You can sign up [here](https://beta.openai.com/signup/).

Set the environment variable:
```sh
export OPENAI_API_KEY='your-openai-api-key'
```

#### Example Usage

1. **Creating the Database:**
   ```sh
   python create_database.py
   ```

2. **Running the Streamlit App:**
   ```sh
   streamlit run app.py
   ```

3. **Asking Questions**: 
   - Open the Streamlit app in your browser.
   - Ask questions like:
     - What is this book about?
     - Who wrote this book?
     - Explain Persona pattern.
     - Give me an example of gameplay pattern.

#### Tutorial Video
For a detailed walkthrough, watch the step-by-step tutorial video: [RAG+Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

---

This README provides a concise and clear guide to setting up and using the book chatbot project based on Prof. Nik Bear Brown's book through a Streamlit interface. Make sure to replace placeholder links and commands with actual ones as necessary.
