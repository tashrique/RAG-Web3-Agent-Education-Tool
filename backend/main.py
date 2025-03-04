from fastapi import FastAPI, Query, HTTPException
from services.bigquery_service import bigquery_service
from services.trends_service import trends_service
from services.github_service import github_service
from typing import List, Optional

app = FastAPI(
    title="Web3 Knowledge System API",
    description="API for accessing Web3 data and analytics",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "OK", "message": "Web3 Knowledge System API is running"}

@app.get("/ethereum")
async def get_ethereum_transactions():
    return bigquery_service.fetch_ethereum_data()

@app.get("/github")
async def get_github_repositories():
    return github_service.get_github_repositories()

@app.get("/trends")
async def get_trends(
    keywords: List[str] = Query(
        default=['ethereum'],
        description="List of keywords to get trends for (max 5 keywords)",
        max_length=5
    )
):
    response = trends_service.get_trends(keywords)
    if response["status"] == "error":
        raise HTTPException(status_code=400, detail=response["message"])
    return response["data"]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)