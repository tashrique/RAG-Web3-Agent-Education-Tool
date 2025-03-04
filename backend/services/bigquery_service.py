from google.cloud import bigquery
import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from pathlib import Path

class BigQueryService:
    def __init__(self):
        """Initialize BigQuery service with credentials"""
        # Load environment variables
        load_dotenv()
        
        # Set credentials path to be in the same directory as this file
        credentials_path = os.path.join(os.path.dirname(__file__), "google_credentials.json")
        
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(f"Please place google_credentials.json in the services directory")

        # Set the credentials environment variable
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        
        # Explicitly set project ID
        project_id = "rag-web3"  # Hardcoding for now to debug
        os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
        
        # Initialize client with explicit project ID
        self.client = bigquery.Client(
            project=project_id,
            location="US"  # Adding explicit location
        )

    def fetch_ethereum_data(self) -> List[Dict[str, Any]]:
        query = """
        SELECT 
            TIMESTAMP_TRUNC(block_timestamp, DAY) as date,
            COUNT(*) as transaction_count,
            SUM(CAST(value AS FLOAT64))/1e18 as total_eth_transferred
        FROM `bigquery-public-data.crypto_ethereum.transactions`
        WHERE DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
        GROUP BY date
        ORDER BY date DESC
        LIMIT 10
        """
        query_job = self.client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]

# Create a singleton instance
bigquery_service = BigQueryService()
