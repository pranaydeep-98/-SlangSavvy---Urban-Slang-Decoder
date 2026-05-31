import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def decode_slang(slang_text):
    """Uses Google Gemini API to decode slang."""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            f"Translate this slang into simple English: {slang_text}"
        )
        return response.text if response else "Could not decode slang."

    except Exception as e:
        return f"Error: {e}"


# Example usage
meaning = decode_slang("brb")
print(f"Decoded Meaning: {meaning}")