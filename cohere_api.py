# ============================================================
# cohere_api.py - Call Cohere's Chat API (UPDATED for 2026)
# ============================================================

import time
import requests


def query_cohere(prompt, api_key):
    """
    Send a prompt to Cohere's Chat API and get a response.
    Uses Command R (active free model as of 2026).
    """
    try:
        # Cohere's v2 API endpoint (v1/generate is deprecated)
        API_URL = "https://api.cohere.com/v2/chat"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        
        payload = {
            "model": "command-r-08-2024",  # Active free model as of 2026
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
            # The response format for v2 API is different
            response_text = result.get("message", {}).get("content", [{}])[0].get("text", "No response")
            if not response_text:
                response_text = str(result)
            return response_text, response_time
        else:
            error_msg = response.json().get("message", "Unknown error")
            return f"❌ Cohere API error ({response.status_code}): {error_msg}", 0
            
    except Exception as error:
        return f"❌ Error calling Cohere API: {error}", 0