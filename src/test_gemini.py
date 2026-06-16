from github_client import get_repository_contents


contents = get_repository_contents(
    "openai",
    "openai-python"
)

for item in contents:
    print(
        item["name"],
        item["type"]
    )