import os
import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv()


def get_gemini_api_key():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY")


api_key = get_gemini_api_key()


def ask_gemini(prompt):
    if not api_key:
        return "Gemini API key not found. Please add GEMINI_API_KEY in Streamlit secrets or local .env file."

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:
        return f"""
# Gemini API Error

{str(error)}
"""