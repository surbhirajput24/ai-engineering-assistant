import os
from dotenv import load_dotenv
from google import genai


# Load API key from .env file
load_dotenv()


# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(prompt):

    # Send prompt to Gemini model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Return Gemini response text
    return response.text