def parse_github_url(repo_url):
    # Remove extra spaces
    repo_url = repo_url.strip()

    # Remove trailing slash if present
    repo_url = repo_url.rstrip("/")

    # Split URL by "/"
    parts = repo_url.split("/")

    # GitHub URL should look like:
    # https://github.com/owner/repo
    if len(parts) < 5 or "github.com" not in repo_url:
        raise ValueError("Invalid GitHub repository URL")

    # Owner is second last part
    owner = parts[-2]

    # Repo name is last part
    repo = parts[-1]

    return owner, repo