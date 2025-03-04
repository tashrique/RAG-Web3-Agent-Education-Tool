import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Pinecone instance
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Define index name
INDEX_NAME = "web3-rag"

# Check existing indexes
existing_indexes = pc.list_indexes().names()

if INDEX_NAME not in existing_indexes:
    print(f"⚠️ Index '{INDEX_NAME}' does not exist. Creating it now...")

    pc.create_index(
        name=INDEX_NAME,
        dimension=768,  # Gemini embeddings use 768 dimensions
        metric="cosine",
        spec=ServerlessSpec(
            cloud="gcp",
            region="gcp-starter"  # ✅ Pinecone Free Plan supports only `gcp-starter`
        )
    )

    print(f"✅ SUCCESS: Pinecone index '{INDEX_NAME}' has been created.")
else:
    print(f"✅ SUCCESS: Pinecone index '{INDEX_NAME}' already exists.")

# Connect to the index
index = pc.Index(INDEX_NAME)

# Verify index is accessible
if INDEX_NAME in pc.list_indexes().names():
    print(f"✅ SUCCESS: Pinecone index '{INDEX_NAME}' is ready.")
else:
    print(f"❌ ERROR: Pinecone index '{INDEX_NAME}' could not be found.")