import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_gemini(prompt, history=[]):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        messages = [{"role": "user", "parts": [{"text": prompt}]}]
        for msg in history:
            messages.append({"role": msg["role"], "parts": [{"text": msg["content"]}]})
        response = model.generate_content(messages)
        return response.text
    except Exception as e:
        return str(e)