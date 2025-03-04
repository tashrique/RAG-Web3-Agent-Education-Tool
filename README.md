# RAG-based Web3 Knowledge System 🚀

A powerful Retrieval-Augmented Generation (RAG) system that provides real-time, accurate, and verifiable AI-generated responses for blockchain-related queries.

## 🌟 Features

- **Real-time Web3 Data Integration**: Pulls data from BigQuery, Google Trends, and GitHub Activity
- **Advanced RAG System**: Uses Gemini AI models for text embedding and generation
- **Source Verification**: Implements dynamic relevance scoring and source attribution
- **Modern UI**: Next.js-based interface for querying blockchain insights

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Next.js
- **Vector Database**: Pinecone (Free-tier)
- **AI Models**: Gemini 2.0 Flash, Gemini text-embedding-004
- **Data Sources**: BigQuery, Google Trends, GitHub API

## 📋 Prerequisites

1. Python 3.9+
2. Node.js 18+
3. Free-tier accounts on:
   - Pinecone
   - Google Cloud (for BigQuery & Gemini API)
   - GitHub (for API access)

## 🚀 Getting Started

### Backend Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. Run the FastAPI server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

## 🗂️ Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Core functionality
│   │   ├── models/         # Data models
│   │   └── services/       # Business logic
│   └── main.py            # Entry point
├── frontend/               # Next.js frontend
│   ├── app/               # Next.js 13+ app directory
│   ├── components/        # React components
│   └── lib/               # Utility functions
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Gemini AI for providing the AI models
- BigQuery for blockchain datasets
- The Web3 community for inspiration and support
