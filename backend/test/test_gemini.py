from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Configure Gemini AI
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def test_generate_embedding():
    """Test Gemini text embedding API."""
    test_text = "Ethereum is the leading smart contract platform."
    
    try:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=[test_text]
        )
        print(result)
    except Exception as e:
        print(f"❌ ERROR: Failed to generate embedding. Reason: {str(e)}")

test_generate_embedding()