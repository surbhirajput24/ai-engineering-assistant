from github_client import get_repository_info


repo_info = get_repository_info(
    "openai",
    "openai-python"
)

print(repo_info["name"])
print(repo_info["language"])
print(repo_info["stargazers_count"])