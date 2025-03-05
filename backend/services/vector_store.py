import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from gemini_embeddings import gemini_embeddings

class PineconeIndex:
    def __init__(self):
        load_dotenv()
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.INDEX_NAME = "web3-rag"
        
        # Check if index exists, create if it doesn't
        if self.INDEX_NAME not in self.pc.list_indexes().names():
            print(f"🔍 Creating new Pinecone index: {self.INDEX_NAME}")
            self.create_index()
        
        self.index = self.pc.Index(self.INDEX_NAME)
    
    def create_index(self):
        self.pc.create_index(
            name=self.INDEX_NAME,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-west-2"
            )
        )
        print(f"✅ Successfully created Pinecone index: {self.INDEX_NAME}")
    
    def upsert_vectors(self, vectors):
        self.index.upsert(vectors)

        
    def query_vectors(self, query_text: str, top_k: int = 10):
        """
        Query Pinecone with an embedding of `query_text`.
        
        Args:
        - query_text (str): The text query.
        - top_k (int): Number of closest results to retrieve.

        Returns:
        - List[Dict]: A list of matched documents with content.
        """
        # Generate embedding for the query text
        embedding_vector = gemini_embeddings.generate_embedding(query_text)

        if embedding_vector is None:
            print("❌ ERROR: Failed to generate embedding.")
            return None

        # Perform similarity search
        response = self.index.query(
            vector=embedding_vector,  
            top_k=top_k,
            include_metadata=True
        )

        # Format and extract relevant data
        results = []
        for match in response.get("matches", []):
            print(f"🔍 Match: {match}")
            results.append({
                "id": match["id"],
                "score": match["score"],
                "source": match["metadata"].get("source", "unknown"),
                "content": match["metadata"].get("text", "No content available")
            })

        return results
    
pinecone_index = PineconeIndex()