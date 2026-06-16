from repository_analyzer import generate_repository_summary

summary = generate_repository_summary(
    "openai-python",
    [
        "README.md",
        "api.md"
    ],
    [
        "This file contains API documentation.",
        "This file contains setup instructions."
    ]
)

print(summary)