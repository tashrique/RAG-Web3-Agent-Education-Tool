from gemini_embeddings import gemini_embeddings
from vector_store import pinecone_index
from bigquery_service import bigquery_service
from data_sources import bigquery_sources, trends_sources, github_sources
# from test_data_sources import bigquery_sources, trends_sources, github_sources
from trends_service import trends_service
from github_service import github_service
import uuid 
import time

class VectorPipeline:
    def __init__(self):
        self.gemini_embeddings = gemini_embeddings
        self.pinecone_index = pinecone_index

    def process_text(self):
        vectors = []

        # BigQuery BlockChain
        for source in bigquery_sources:
            blockchain_data = bigquery_service.fetch_blockchain_data(source)
            print(f"🔍 Processing blockchain data for: {source}")
            for row in blockchain_data:
                text = f"{source}: {row}"
                vectors.append({
                    "id": str(uuid.uuid4()),
                    "text": text,
                    "metadata": {"source": source}
                })

        # Google Trends
        for keyword in trends_sources:
            try:
                print(f"🔍 Fetching trends for: {keyword}")
                trends_data = trends_service.get_trends(keyword)
                
                if trends_data["status"] == "success" and trends_data["data"]["trend_data"]:
                    for row in trends_data["data"]["trend_data"]:
                        text = f"Google Trends: {keyword}: {row}"
                        vectors.append({
                            "id": str(uuid.uuid4()),
                            "text": text,
                            "metadata": {"source": "google_trends"}
                        })
                
                time.sleep(2)  # Shorter delay after a full keyword batch

            except Exception as e:
                print(f"❌ ERROR: Failed to fetch trends for {keyword}. Reason: {str(e)}")

        # GitHub
        for source in github_sources:
            print(f"🔍 Processing GitHub data for: {source}")
            github_data = github_service.get_trending_repos(source)
            if github_data["status"] == "success" and github_data["data"]:
                for repo in github_data["data"]:
                    text = f"GitHub: {source}: {repo['name']} {repo['description']} {repo['stars']}"
                    vectors.append({
                        "id": str(uuid.uuid4()),
                        "text": text,
                        "metadata": {"source": source}
                    })

        return vectors
    
    def store_vectors(self, vectors):
        processed_vectors = []

        for vector in vectors:
            text = vector["text"]
            embedding = self.gemini_embeddings.generate_embedding(text)
            time.sleep(1)
            

            if embedding:
                processed_vectors.append({
                    "id": vector["id"], 
                    "values": list(embedding),
                    "metadata": {
                        "content": text,
                        "source": vector["metadata"]["source"]
                    }

                })

        if processed_vectors:
            self.pinecone_index.upsert_vectors(processed_vectors)
            print(f"✅ Successfully stored {len(processed_vectors)} vectors in Pinecone.")
        else:
            print("⚠️ No valid embeddings were generated. Nothing stored.")

        return {"status": "success", "message": "Vectors stored successfully"}

    def generate_response(self, query):
        context = self.pinecone_index.query_vectors(query)
        prompt = f"""
        Using the following retrieved data, answer the question while citing sources:
    
        {context}

        Ensure the response includes verifiable sources. 
        Question: {query}

        Be concise and to the point. If google trends data shown, analyze the data and provide a summary.
        If github data shown, analyze the data and provide a summary.
        """

        response = self.gemini_embeddings.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt]
        )
        return response.text

if __name__ == "__main__":
    vector_pipeline = VectorPipeline()
    # print("🔄 Starting vector processing...")
    # vectors = vector_pipeline.process_text()
    # print(f"✅ Processed {len(vectors)} vectors")
    # print("🔄 Storing vectors in Pinecone...")
    # vector_pipeline.store_vectors(vectors)
    # print("✅ Vector storage complete")

    # Test query
    query = "how do i learn about blockchain?"
    print(f"🔍 Querying Pinecone with: {query}")
    results = vector_pipeline.pinecone_index.query_vectors(query)
    print("🔄 Generating response...")
    response = vector_pipeline.generate_response(query)
    print(f"✅ Response: {response}")
