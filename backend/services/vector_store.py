import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Initialize Pinecone instance
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Define index name
INDEX_NAME = "web3-rag"

# Create index if it doesn't exist
existing_indexes = pc.list_indexes().names()

if INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,  # Gemini embeddings are 768-dimensional
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-west-2"
        )
    )

# Connect to the index
index = pc.Index(INDEX_NAME)

def upsert_vectors(vectors):
    """
    Store vectors in Pinecone.
    :param vectors: List of (id, vector, metadata) tuples
    """
    index.upsert(vectors)