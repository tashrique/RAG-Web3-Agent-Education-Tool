from fastapi import APIRouter, Query, HTTPException
from services.trends_service import trends_service

router = APIRouter(prefix="/trends", tags=["trends"])

@router.get("/")
async def get_trends(keyword: str = Query(default='ethereum', description="Keyword to get trends for")):
    response = trends_service.get_trends(keyword)
    if response["status"] == "error":
        raise HTTPException(status_code=400, detail=response["message"])
    return response["data"] 