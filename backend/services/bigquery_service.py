from google.cloud import bigquery
import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from services.data_sources import bigquery_sources
class BigQueryService:
    def __init__(self):
        """Initialize BigQuery service with credentials"""
        load_dotenv()
        credentials_path = os.path.join(os.path.dirname(__file__), "google_credentials.json")
        
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(f"Please place google_credentials.json in the services directory")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        self.client = bigquery.Client(project=os.getenv("GOOGLE_CLOUD_PROJECT"),location="US" )

    def fetch_blockchain_data(self, source: str) -> List[Dict[str, Any]]:

        if source not in bigquery_sources:
            raise ValueError(f"Source {source} not found in bigquery_sources")

        query = bigquery_sources[source]["query"]
        query_job = self.client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]

# Create a singleton instance
bigquery_service = BigQueryService()
