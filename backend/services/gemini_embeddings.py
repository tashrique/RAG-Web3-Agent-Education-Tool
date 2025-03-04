from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiEmbeddings:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def generate_embedding(self, text: str):
        """Test Gemini text embedding API."""
        
        try:
            result = self.client.models.embed_content(
                model="text-embedding-004",
                contents=[text]
            )
            return result
        except Exception as e:
            print(f"❌ ERROR: Failed to generate embedding. Reason: {str(e)}")

