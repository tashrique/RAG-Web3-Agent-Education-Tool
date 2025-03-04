import faiss
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini with API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

texts = ["Ethereum blockchain transactions", "DeFi is growing", "Bitcoin latest update"]

try:
    # Get embeddings for texts using Gemini's embedding model
    model = 'models/embedding-001'  # Gemini's embedding model
    embeddings = [genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_query"
    )['embedding'] for text in texts]
    
    # Convert embeddings to numpy array
    vector_data = np.array(embeddings)
    
    # Initialize FAISS index with correct dimensions
    dimension = len(vector_data[0])  # Get dimension from first embedding
    index = faiss.IndexFlatL2(dimension)
    
    # Add vectors to index
    index.add(vector_data.astype('float32'))  # Convert to float32 for FAISS
    
    print(f"Number of vectors in index: {index.ntotal}")
    
    # Process query
    query = "What's the latest news on Ethereum?"
    query_embedding = genai.embed_content(
        model=model,
        content=query,
        task_type="retrieval_query"
    )['embedding']
    
    # Convert query embedding to correct format
    query_vector = np.array([query_embedding]).astype('float32')
    
    # Perform similarity search
    k = 2  # Number of nearest neighbors to retrieve
    distances, indices = index.search(query_vector, k)
    
    # Print results
    print("\nSearch Results for query:", query)
    print("-" * 50)
    for i in range(len(indices[0])):
        idx = indices[0][i]
        distance = distances[0][i]
        print(f"Match {i+1}:")
        print(f"Text: {texts[idx]}")
        print(f"Distance: {distance:.4f}")  # Lower distance means more similar
        print()
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
