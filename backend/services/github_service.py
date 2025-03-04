import requests
from typing import List, Dict, Any
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

class GitHubService:
    def __init__(self):
        load_dotenv()
        self.base_url = "https://api.github.com"
        self.token = os.getenv("GITHUB_ACCESS_TOKEN")
        self.headers = {"Authorization": f"token {self.token}"} if self.token else {}

    def get_trending_repos(self, topic: str, language: str = "all", period: str = "weekly") -> Dict[str, Any]:
        time_filter = {
            "daily": datetime.utcnow() - timedelta(days=1),
            "weekly": datetime.utcnow() - timedelta(days=7),
            "monthly": datetime.utcnow() - timedelta(days=30),
        }

        if period not in time_filter:
            return {"status": "error", "message": "Invalid period. Use daily, weekly, or monthly."}

        date_since = time_filter[period].strftime("%Y-%m-%d")
        query = f"topic:{topic} created:>{date_since}"

        if language.lower() != "all":
            query += f" language:{language}"

        url = f"{self.base_url}/search/repositories?q={query}&sort=stars&order=desc&per_page=10"

        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            return {"status": "error", "message": f"GitHub API Error: {response.json()}"}

        data = response.json()["items"]
        return {
            "status": "success",
            "message": "Trending GitHub repositories retrieved successfully.",
            "data": [
                {
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "description": repo["description"],
                    "url": repo["html_url"],
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    "language": repo["language"],
                    "created_at": repo["created_at"],
                    "updated_at": repo["updated_at"],
                }
                for repo in data
            ],
        }

    def get_repo_activity(self, owner: str, repo: str) -> Dict[str, Any]:

        commits_url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        contributors_url = f"{self.base_url}/repos/{owner}/{repo}/contributors"

        commits_response = requests.get(commits_url, headers=self.headers)
        contributors_response = requests.get(contributors_url, headers=self.headers)

        if commits_response.status_code != 200 or contributors_response.status_code != 200:
            return {"status": "error", "message": "Failed to fetch repository activity."}

        commits = len(commits_response.json())  # Number of recent commits
        contributors = len(contributors_response.json())  # Number of contributors

        return {
            "status": "success",
            "message": f"Activity for {owner}/{repo} retrieved successfully.",
            "data": {
                "repo": repo,
                "owner": owner,
                "recent_commits": commits,
                "total_contributors": contributors,
            },
        }


github_service = GitHubService()