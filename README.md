# 📄 ChatGroq - Multi-File Conversational QA with PDF, CSV, Excel + LLaMA3

This project is a Streamlit-powered chatbot that uses **LangChain**, **FAISS**, and **Groq's LLaMA3 models** to enable intelligent Q&A over **multiple document formats** including:

- 📄 PDF documents  
- 📊 Excel spreadsheets (.xls, .xlsx)  
- 📈 CSV files  

It supports **semantic search**, **context-aware Q&A**, and displays **retrieved content sources**.

---

## 🧠 Features

✅ Upload **multiple documents at once**  
✅ Ask questions in natural language  
✅ Powered by **Groq + LLaMA3** via LangChain  
✅ Uses **HuggingFaceEmbeddings** and **FAISS**  
✅ Supports documents in **PDF, XLS/XLSX, CSV**  
✅ Shows **retrieved source text** for transparency  
✅ Prepares foundation for visual analytics (chart support coming soon)

---
## 🖼️ Example Outputs
[📁 Project Portfolio](https://thathsarani-sandarekha.github.io/thathsarani_zone/)
---

## 🧠 How It Works
You upload any combination of PDFs, Excel files, and CSVs.

Each file is:

1. Parsed into row-wise text (CSV/Excel) or page-wise text (PDF)
2. Chunked using LangChain’s RecursiveCharacterTextSplitter
3. Embedded using HuggingFaceEmbeddings
4. Stored in a FAISS vector store
5. Questions are answered using ChatGroq with llama-3.3-70b-versatile, limited to the document context only.

