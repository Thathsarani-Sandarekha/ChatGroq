import streamlit as st
import os
import time
import pandas as pd
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, UnstructuredExcelLoader
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

st.title("📄 ChatGroq - Multi-File Chatbot (PDF, CSV, Excel)")

uploaded_files = st.file_uploader(
    "Upload PDF, CSV, or Excel files", 
    type=["pdf", "csv", "xls", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files and "vectors" not in st.session_state:
    all_docs = []

    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        suffix = filename.split(".")[-1].lower()

        # Save temporarily
        with open(filename, "wb") as f:
            f.write(uploaded_file.read())

        # PDF
        if suffix == "pdf":
            loader = PyPDFLoader(filename)
            docs = loader.load()

        # Excel
        elif suffix in ["xls", "xlsx"]:
            df = pd.read_excel(filename)

            docs = []
            for i, row in df.iterrows():
                row_text = row.to_string()
                docs.append(Document(page_content=row_text, metadata={"source": filename}))

        # CSV
        elif suffix == "csv":
            df = pd.read_csv(filename)

            # Split into rows (optional: group multiple rows into a chunk)
            docs = []
            for i, row in df.iterrows():
                row_text = row.to_string()
                docs.append(Document(page_content=row_text, metadata={"source": filename}))


        # Add source metadata
        for doc in docs:
            doc.metadata["source"] = filename

        all_docs.extend(docs)

        # Clean up file
        os.remove(filename)

    # Split & embed
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_chunks = text_splitter.split_documents(all_docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectors = FAISS.from_documents(final_chunks, embeddings)

    # Save to session
    st.session_state.vectors = vectors
    st.session_state.embeddings = embeddings

# Retrieval logic
if "vectors" in st.session_state:
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

    prompt_template = ChatPromptTemplate.from_template(
        """
        Answer the question using only the context provided below.
        Be concise and accurate.

        <context>
        {context}
        <context>
        Question: {input}
        """
    )

    document_chain = create_stuff_documents_chain(llm, prompt_template)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    user_input = st.text_input("Ask a question:")

    if user_input:
        start = time.process_time()
        response = retrieval_chain.invoke({'input': user_input})
        st.write("**Answer:**", response['answer'])
        st.write("⏱️ Response Time:", round(time.process_time() - start, 2), "seconds")

        with st.expander("🔍 Retrieved Chunks (with file source)"):
            for i, doc in enumerate(response["context"]):
                st.markdown(f"📄 **Source**: `{doc.metadata.get('source', 'Unknown')}`")
                st.markdown(doc.page_content)
                st.markdown("---")
else:
    st.info("📤 Upload PDF, CSV, or Excel files to begin.")
