from fastapi import APIRouter, Query, HTTPException
from services.github_service import github_service

router = APIRouter(prefix="/github", tags=["github"])

@router.get("/trending")
async def get_trending_repos(
    topic: str = Query(default="blockchain", description="Web3 topic (e.g., blockchain, defi, nft)"),
    language: str = Query(default="all", description="Programming language (default: all)"),
    period: str = Query(default="weekly", description="Time period: daily, weekly, or monthly")
):
    """
    API endpoint to fetch trending GitHub repositories for Web3 topics.
    """
    return github_service.get_trending_repos(topic, language, period)

@router.get("/activity")
async def get_repo_activity(
    owner: str = Query(..., description="Repository owner (e.g., ethereum)"),
    repo: str = Query(..., description="Repository name (e.g., go-ethereum)")
):
    """
    API endpoint to fetch repository commit and contributor activity.
    """
    return github_service.get_repo_activity(owner, repo) 