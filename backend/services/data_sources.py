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
    "polygon": {
        "query": """
            SELECT 
                TIMESTAMP_TRUNC(block_timestamp, DAY) as date,
                COUNT(*) as transaction_count,
            FROM `bigquery-public-data.goog_blockchain_polygon_mainnet_us.transactions`
            WHERE DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
            GROUP BY date
            ORDER BY date DESC
            LIMIT 10
        """,
        "description": "Polygon transactions aggregated by day, including gas metrics, unique addresses, and EIP-1559 adoption."
    },
    "bitcoin": {

        "query": """
            SELECT 
                TIMESTAMP_TRUNC(block_timestamp, DAY) as date,
                COUNT(*) as transaction_count,
                AVG(fee) as avg_fee_satoshis,
                AVG(size) as avg_tx_size
            FROM `bigquery-public-data.crypto_bitcoin.transactions`
            WHERE DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
            GROUP BY date
            ORDER BY date DESC
            LIMIT 10
        """,
        "description": "Bitcoin transactions aggregated by day including fees, values, and transaction metrics."
    },
    "avalanche": {
        "query": """
            SELECT 
                TIMESTAMP_TRUNC(block_timestamp, DAY) as date,
                COUNT(*) as transaction_count
            FROM `bigquery-public-data.goog_blockchain_avalanche_contract_chain_us.transactions`
            WHERE DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
            GROUP BY date
            ORDER BY date DESC
            LIMIT 10
        """,
        "description": "Avalanche transactions aggregated by day."
    },
}

trends_sources = {
    "google_trends": {
        "description": "Google Trends data for blockchain-related topics."
    }
}

github_sources = {
    "github_repos": {
        "description": "Trending GitHub repositories for blockchain projects."
    }
}