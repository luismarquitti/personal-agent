import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_ollama_connectivity():
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("PREFERRED_LOCAL_MODEL", "llama3")

    print(f"Testing Ollama connectivity at {base_url} using model '{model}'...")
    
    try:
        # Check if Ollama service is up
        response = requests.get(f"{base_url}/api/tags", timeout=5)
        if response.status_code != 200:
            print(f"Error: Ollama service returned status {response.status_code}")
            return
        
        # Check if model is pulled
        tags = response.json().get("models", [])
        model_names = [m["name"] for m in tags]
        
        if any(model in name for name in model_names):
            print(f"Success! Model '{model}' found locally.")
        else:
            print(f"Warning: Model '{model}' not found in local tags. Run 'ollama pull {model}'.")
            print(f"Available models: {', '.join(model_names) if model_names else 'None'}")

    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to Ollama service. Ensure it is running.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    test_ollama_connectivity()
