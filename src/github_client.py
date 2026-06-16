import requests
import base64

def get_repository_info(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"GitHub API Error: {response.status_code}"
        )

    return response.json()


def get_repository_contents(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(
        url,
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"GitHub API Error: {response.status_code}"
        )

    return response.json()




def get_file_content(file_url):

    response = requests.get(
        file_url,
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"GitHub File API Error: {response.status_code}"
        )

    file_data = response.json()

    encoded_content = file_data["content"]

    decoded_content = base64.b64decode(
        encoded_content
    ).decode("utf-8")

    return decoded_content