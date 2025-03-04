import requests
import os

class GithubService:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_github_repositories(self):
        url = f"{self.base_url}/search/repositories"
        params = {
            "q": "ethereum",
            "sort": "stars",
            "order": "desc",
            "per_page": 10,
            "page": 1
        }
        response = requests.get(url, params=params)
        return response.json()

github_service = GithubService()