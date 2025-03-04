# SPECIFICATION: RAG-Based Web3 Knowledge System

## 🏆 Project Overview
A Retrieval-Augmented Generation (RAG) system that uses **real-time Web3 data** to provide **accurate and verifiable AI-generated responses** for blockchain-related queries.

## 🎯 Goals
- Implement a **Knowledge Ingestion Pipeline** to pull Web3 data from **BigQuery, Google Trends, GitHub Activity**.
- Use **Gemini AI models** for **text embedding, retrieval, and attributed question answering**.
- Implement **Dynamic Relevance Scoring, Context Window Optimization, and Source Verification**.
- Build a **demonstration interface** to allow users to query the AI and receive **trusted, real-time blockchain insights**.

---

## 📌 Key Features

### **1️⃣ Knowledge Ingestion Pipeline**
✅ Fetch structured Web3 data from:
   - **BigQuery Public Datasets** (Ethereum, Solana, Uniswap, and also general data)
   - **GitHub API** (track blockchain project activity)
   - **Google Trends API** (monitor Web3 keyword trends)

✅ Store & process data:
   - Convert structured datasets into **vector embeddings**.
   - Store embeddings using **FAISS (local) or Pinecone (free-tier)**.
   - Perform **real-time updates** to ensure fresh Web3 insights.

---

### **2️⃣ Retrieval-Augmented Generation (RAG) System**
✅ Query the **vector database** to fetch the **most relevant** blockchain data.  
✅ Use **Gemini models** to generate fact-checked responses.  
✅ Implement:
   - **Dynamic Relevance Scoring** (prioritize high-trust sources).
   - **Context Window Optimization** (smart chunking & summarization).
   - **Source Verification** (display data provenance in answers).

---

### **3️⃣ AI Models Used**
| Task                        | AI Model                        |
|-----------------------------|--------------------------------|
| Text Embeddings             | `gemini/text-embedding-004`   |
| Attributed Question Answering | `gemini/aqa`                  |
| Response Generation         | `gemini-2.0-flash`            |

---

### **4️⃣ Demonstration Interface**
✅ A **Next.js-based frontend** where users can:
   - Ask **Web3-related questions**.
   - View **real-time, fact-checked responses**.
   - See **source verification (citations, timestamps, confidence scores)**.

✅ A **FastAPI backend** that:
   - Fetches Web3 data from the **vector database**.
   - Calls the **Gemini AI models** to generate responses.
   - Returns structured JSON data with **source verification**.

---

## 📦 Tech Stack

| Component                 | Technology |
|---------------------------|-----------|
| Backend API               | **FastAPI** (Python)
| Vector Database           | **Pinecone (Free-Tier)** |
| Frontend                  | **Next.js (React-based UI)** |
| LLM for Generation        | **Gemini 2.0 Flash** |
| Text Embeddings           | **Gemini text-embedding-004** |
| Source Verification Model | **Gemini AQA** |
| Data Sources              | **BigQuery, Google Trends, GitHub API** |

---

## 🔗 Data Sources & APIs

| Source            | Description |
|-------------------|-------------|
| **BigQuery**      | Free-tier blockchain datasets (Ethereum, Solana, Uniswap) |
| **Google Trends** | Monitor DeFi & Web3 keyword trends |
| **GitHub API**    | Track blockchain-related project activity |
| **Flare Data Feeds** | Real-time smart contract & FTSO data |

---

## 🚀 Deployment & Cost Considerations
✅ **No Paid Services** – Everything runs on **free-tier APIs & databases**.  
✅ **Avoiding TEE for Now** – Can be added later for security.  
✅ **Backend Hosting**:
   - **Free-tier Vercel** (for Next.js frontend)
   - **Railway.app / Render** (for FastAPI backend)
