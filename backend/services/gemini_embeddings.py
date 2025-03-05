from google import genai
import os
from dotenv import load_dotenv
import sqlite3
import hashlib
import json
import pathlib


class GeminiEmbeddings:
    def __init__(self):
        load_dotenv()
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # Create cache directory if it doesn't exist
        cache_dir = pathlib.Path("cache")
        cache_dir.mkdir(exist_ok=True)
        
        self.db = sqlite3.connect(cache_dir / "gemini_embeddings.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS embeddings (hash TEXT PRIMARY KEY, text TEXT, embedding TEXT)")

    def generate_embedding(self, text: str):
        """Generate text embedding using Gemini API with caching."""
        try:
            # cached_embedding = self.get_cached_embedding(text)
            # if cached_embedding is not None:  # Explicit None check
            #     print("📦 Using cached embedding")
            #     return cached_embedding
            
            print("🔄 Generating new embedding")
            result = self.client.models.embed_content(
                model="text-embedding-004",
                contents=[text]
            )
            embedding = result.embeddings[0].values
            self.cache_embedding(text, embedding)
            return embedding    
        except Exception as e:
            print(f"❌ ERROR: Failed to generate embedding. Reason: {str(e)}")
            return None

    def get_cached_embedding(self, text: str):
        try:
            query_hash = hashlib.sha256(text.encode()).hexdigest()
            cursor = self.db.cursor()
            cursor.execute("SELECT embedding FROM embeddings WHERE hash = ?", (query_hash,))
            result = cursor.fetchone()
            if result:
                return json.loads(result[0])  # Deserialize the embedding
            return None
        except Exception as e:
            print(f"⚠️ Cache read error: {str(e)}")
            return None
    
    def cache_embedding(self, text: str, embedding: list):
        try:
            query_hash = hashlib.sha256(text.encode()).hexdigest()
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO embeddings (hash, text, embedding) VALUES (?, ?, ?)", 
                (query_hash, text, json.dumps(embedding))  # Serialize the embedding
            )
            self.db.commit()
        except Exception as e:
            print(f"⚠️ Cache write error: {str(e)}")


gemini_embeddings = GeminiEmbeddings()