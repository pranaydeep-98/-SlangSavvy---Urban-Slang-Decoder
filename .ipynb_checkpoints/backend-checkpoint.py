import google.generativeai as genai

# ✅ Set up API Key (Replace with your actual key)
genai.configure(api_key="AIzaSyCiknt0RJQUl3i0qVZbPWJcKbWDlfzSIro")

# ✅ Function to Call Google Gemini API
def decode_slang(slang_text):
    """Uses Google Gemini API to decode slang."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(f"Translate this slang into simple English: {slang_text}")
        return response.text if response else "Could not decode slang."
    except Exception as e:
        return f"Error: {e}"

    print(f"Meaning: {meaning}")
