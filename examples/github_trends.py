import requests


url = "https://api.github.com/search/repositories?q=blockchain&sort=stars"

response = requests.get(url)

data = response.json()


repos = [
    {
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "last_updated": repo["updated_at"],
    }
    for repo in data["items"]
]

# Display results
for repo in repos[:5]:
    print(repo)