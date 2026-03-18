import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def test_gemini_connectivity():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        return

    print(f"Testing Gemini API connectivity with key: {api_key[:5]}...{api_key[-5:]}")
    
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        response = llm.invoke("Hello, are you online?")
        print("\nSuccess! Gemini Response:")
        print(response.content)
    except Exception as e:
        print(f"\nFailed to connect to Gemini API: {e}")

if __name__ == "__main__":
    test_gemini_connectivity()
