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
<img src="./example outputs/2 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/3 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/4 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/5 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/6 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/7 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">
<img src="./example outputs/8 ex.jpg" alt="rq1" style="margin-top: 1rem; max-width: 100%; border-radius: 8px;">

---

## 🧠 How It Works
You upload any combination of PDFs, Excel files, and CSVs.

Each file is:

1. Parsed into row-wise text (CSV/Excel) or page-wise text (PDF)
2. Chunked using LangChain’s RecursiveCharacterTextSplitter
3. Embedded using HuggingFaceEmbeddings
4. Stored in a FAISS vector store
5. Questions are answered using ChatGroq with llama-3.3-70b-versatile, limited to the document context only.

