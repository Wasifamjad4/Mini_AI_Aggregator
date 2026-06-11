# ============================================================
# groq_api.py - Call Groq's Llama 3 70B Model
# ============================================================
# This file contains ONE function that sends a prompt to
# Groq and returns the response text + how long it took.
#
# How it works:
#   1. Takes your prompt text and API key
#   2. Calls Groq's chat completion API (mixtral-8x7b-32768)
#   3. Measures how many seconds the request took
#   4. Returns the response text and time
#
# API Docs: https://console.groq.com/docs/api-reference
# Free tier: Groq gives free API access with a rate limit (no credit card needed)

import time  # For measuring how long the API call takes


def query_groq(prompt, api_key):
    """
    Send a prompt to Groq's Llama 3 70B model and get a response.

    Parameters:
        prompt (str): The text you want to ask the AI
        api_key (str): Your Groq API key (starts with "gsk_")

    Returns:
        tuple: (response_text, response_time_in_seconds)
               If something goes wrong, response_text will be an error message
               and response_time will be 0.
    """
    try:
        # Import groq INSIDE the function so the app doesn't crash
        # if the groq package isn't installed
        from groq import Groq

        # Create a Groq client with your API key
        # The client object handles all communication with Groq's servers
        client = Groq(api_key=api_key)

        # ---- Record the START time (before we send the request) ----
        start_time = time.time()

        # ---- Send the prompt to Groq ----
        # The chat completions API uses a list of "messages"
        # Each message has a "role" (user = you, assistant = AI reply)
        # We're sending one message from the "user" role
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Groq's fast, free model (128K context!)
            messages=[
                {
                    "role": "user",  # "user" means this message is from the person using the app
                    "content": prompt,  # The actual text you typed
                }
            ],
            max_tokens=500,  # Maximum number of tokens in the reply (1 token ≈ 0.75 words)
            temperature=0.7,  # How creative the AI should be (0 = factual, 1 = very creative)
        )

        # ---- Record the END time (after we get the response) ----
        end_time = time.time()

        # Calculate how long the request took (in seconds)
        response_time = round(end_time - start_time, 2)

        # Extract the text from Groq's response
        # The response is a nested object:
        #   response.choices[0]          = the first (and usually only) reply
        #   .message.content             = the actual text the AI wrote
        response_text = response.choices[0].message.content

        # Return the response text and how long it took
        return response_text, response_time

    except Exception as error:
        # If ANYTHING goes wrong (wrong API key, no internet, etc.),
        # we catch the error and return a helpful message instead of crashing
        return f"❌ Error calling Groq API: {error}", 0