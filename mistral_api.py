# ============================================================
# mistral_api.py - Call Mistral AI API
# ============================================================

import time
import requests


def query_mistral(prompt, api_key):
    """
    Send a prompt to Mistral AI and get a response.
    Uses mistral-small-latest model (free tier).
    """
    try:
        API_URL = "https://api.mistral.ai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        
        payload = {
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 500,
        }
        
        start_time = time.time()
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        end_time = time.time()
        response_time = round(end_time - start_time, 2)
        
        if response.status_code == 200:
            result = response.json()
            response_text = result["choices"][0]["message"]["content"]
            return response_text, response_time
        else:
            error_msg = response.json().get("error", {}).get("message", "Unknown error")
            return f"❌ Mistral API error ({response.status_code}): {error_msg}", 0
            
    except Exception as error:
        return f"❌ Error calling Mistral API: {error}", 0