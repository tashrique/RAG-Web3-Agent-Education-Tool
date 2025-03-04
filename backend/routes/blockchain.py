from fastapi import APIRouter, Query, HTTPException
from services.bigquery_service import bigquery_service

router = APIRouter(prefix="/blockchain", tags=["blockchain"])

@router.get("/")
def search_blockchain_data(
    source: str = Query(..., description="Blockchain dataset (e.g., ethereum, bitcoin, polygon, avalanche)")):
    return bigquery_service.fetch_blockchain_data(source) 