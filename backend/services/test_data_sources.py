# services/data_sources.py

bigquery_sources = {
    "ethereum": {
        "query": """
            SELECT 
                TIMESTAMP_TRUNC(block_timestamp, DAY) as date,
                COUNT(*) as transaction_count,
                SUM(CAST(value AS FLOAT64))/1e18 as total_eth_transferred
            FROM `bigquery-public-data.crypto_ethereum.transactions`
            WHERE DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
            GROUP BY date
            ORDER BY date DESC
            LIMIT 10
        """,
        "description": "Ethereum transactions aggregated by day."
    },  
        
}

trends_sources = ["ethereum"]
github_sources = ["ethereum"]