import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import RateLimitError


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def ask_openai(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text

    except RateLimitError:
        return """
# OpenAI Error

OpenAI quota exceeded.

Please add billing credits to your OpenAI account or select Gemini.
"""