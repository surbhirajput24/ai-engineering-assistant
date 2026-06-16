from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py",
    ".java",
    ".xml",
    ".gradle",
    ".txt"
}

def scan_project(project_path):

    files_found = []

    path = Path(project_path)

    for file in path.rglob("*"):

        if file.is_file() and file.suffix in SUPPORTED_EXTENSIONS:

            files_found.append(file)

    return files_found


def read_file_content(file_path):

    with open(file_path, "r") as file:

        content = file.read()

    return content