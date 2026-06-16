from src.ai_client import ask_gemini
from src.openai_client import ask_openai


def get_llm_response(provider, prompt):

    if provider == "Gemini":
        return ask_gemini(prompt)

    elif provider == "OpenAI":
        return ask_openai(prompt)

    elif provider == "Claude":
        return """
# Claude Analysis

Claude integration is not implemented yet.
Please select Gemini or OpenAI.
"""

    else:
        return f"Unknown provider: {provider}"