# ============================================================
# app.py - Mini AI Aggregator (Main Application)
# ============================================================
# This is the MAIN file you run to start the app.
#
# What it does:
#   1. Shows a web page with a title and a text box
#   2. You type a prompt and click "Compare AI Responses"
#   3. It sends your prompt to Groq, Cohere, and HuggingFace
#   4. It displays all 3 responses side by side in columns
#   5. For each response, it shows: the answer, response time, word count
#
# How to run:
#   streamlit run app.py
#
# What is Streamlit?
#   Streamlit is a Python library that turns Python scripts into
#   web apps. You don't need to know HTML, CSS, or JavaScript!

# ---- Import the libraries we need ----
import streamlit as st  # For creating the web app interface
import time            # For measuring response times
import os              # For reading environment variables (API keys)
from dotenv import load_dotenv  # For loading the .env file

# ---- Import our API functions from their separate files ----
# These are the functions we created that actually call each AI provider
from groq_api import query_groq              # Function for Groq
from cohere_api import query_cohere          # Function for Cohere
from mistral_api import query_mistral          # Function for Mistral AI


# ============================================================
# STEP 1: Load API Keys from .env file
# ============================================================
# The .env file contains our secret API keys.
# python-dotenv reads the .env file and puts the keys into
# environment variables (like hidden notes that our code can read).
load_dotenv()

# Now we read each API key from the environment variables
# os.getenv("NAME") reads the value of an environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


# ============================================================
# Helper function: Count words in a text
# ============================================================
def count_words(text):
    """
    Count the number of words in a piece of text.

    How it works:
        text.split() splits the text into a list of words
        (it splits on spaces and newlines automatically).
        Then len() counts how many items are in that list.

    Example:
        count_words("Hello world!") → 2
        count_words("") → 0

    Parameters:
        text (str): The text to count words in

    Returns:
        int: The number of words
    """
    # If the text is empty, return 0 (avoid counting errors)
    if not text:
        return 0
    # Split the text by spaces and count the pieces
    return len(text.split())


# ============================================================
# STEP 2: Set up the Streamlit web page
# ============================================================

# st.set_page_config() configures the web page tab and layout
# This MUST be the first Streamlit command in the file
st.set_page_config(
    page_title="Mini AI Aggregator",  # Text that appears in the browser tab
    page_icon="🤖",                   # Emoji icon in the browser tab
    layout="wide",                    # "wide" = use the full width of the screen
)

# st.title() adds a big heading at the top of the page
st.title("Mini AI Aggregator")

# st.markdown() adds text with Markdown formatting (bold, italic, etc.)
st.markdown(
    "Compare responses from **Groq**, **Cohere**, and **Mistral AI** "
    "side by side!"
)

# Add a nice separator line
st.divider()


# ============================================================
# STEP 3: Check if API keys are available
# ============================================================

# If any of the API keys are missing, show a warning and stop
if not GROQ_API_KEY or not COHERE_API_KEY or not MISTRAL_API_KEY:
    st.error(
        " API keys not found! Please:\n\n"
        "1. Create a `.env` file in the project folder\n"
        "2. Add your API keys like this:\n\n"
        "   GROQ_API_KEY=gsk-your-key-here\n"
        "   COHERE_API_KEY=your-key-here\n"
        "   MISTRAL_API_KEY=your-key-here\n\n"
        "3. Restart the app"
    )
    # st.stop() prevents the rest of the app from running
    st.stop()


# ============================================================
# STEP 4: Create the input area
# ============================================================

# st.text_area() creates a multi-line text input box
# The user types their question/prompt here
prompt = st.text_area(
    "Enter your prompt:",          # Label shown above the text box
    placeholder="Type your question here... (e.g., What is machine learning?)",
    height=100,                    # Height of the text box in pixels
)

# st.button() creates a clickable button
# It returns True when clicked, False otherwise
compare_button = st.button(" Compare AI Responses", type="primary")


# ============================================================
# STEP 5: When the user clicks "Compare", call all 3 APIs
# ============================================================

# This code runs ONLY when the button is clicked AND there's a prompt
if compare_button and prompt:
    # Show a spinner while the APIs are being called
    # st.spinner() shows a loading animation
    with st.spinner("Calling AI providers... this may take a moment "):

        # ---- Call Groq ----
        # Our query_groq function sends the prompt to mixtral-8x7b-32768
        # It returns (response_text, response_time_seconds)
        groq_response, groq_time = query_groq(prompt, GROQ_API_KEY)

        # ---- Call Cohere ----
        # Our query_cohere function sends the prompt to Cohere's command model
        cohere_response, cohere_time = query_cohere(prompt, COHERE_API_KEY)

        # ---- Call Mistral AI ----
        # Our query_mistral function sends the prompt to Mistral Small
        mistral_response, mistral_time = query_mistral(
            prompt, MISTRAL_API_KEY
        )

    # ---- Add a small pause so the spinner is visible ----
    # This is just for visual polish
    time.sleep(0.3)

    # ============================================================
    # STEP 6: Display the results side by side in 3 columns
    # ============================================================

    st.divider()
    st.subheader("Results")

    # st.columns(3) creates 3 equal-width columns on the page
    # col1, col2, col3 are the three column objects we can write to
    col1, col2, col3 = st.columns(3)

    # ---- Column 1: Groq Results ----
    with col1:
        # st.info() creates a colored info box
        st.info(" Groq (Mixtral 8x7B)")

        # Count words in the response
        groq_words = count_words(groq_response)

        # Show the metrics (response time and word count)
        # st.metric() shows a big number with a label
        st.metric(" Response Time", f"{groq_time}s")
        st.metric(" Word Count", groq_words)

        # Show the actual AI response
        # st.write() can display text, numbers, and more
        st.write(groq_response)

    # ---- Column 2: Cohere Results ----
    with col2:
        st.info(" Cohere (Command R)")

        cohere_words = count_words(cohere_response)

        st.metric(" Response Time", f"{cohere_time}s")
        st.metric(" Word Count", cohere_words)

        st.write(cohere_response)

    # ---- Column 3: Mistral AI Results ----
    with col3:
        st.info(" Mistral AI (Mistral Small)")

        mistral_words = count_words(mistral_response)

        st.metric(" Response Time", f"{mistral_time}s")
        st.metric(" Word Count", mistral_words)

        st.write(mistral_response)

# If the button is clicked but no prompt was entered, show a warning
elif compare_button:
    st.warning("Please enter a prompt first!")


# ============================================================
# STEP 7: Footer with instructions
# ============================================================

st.divider()
st.markdown(
    " **Note:** The response time depends on the AI provider's servers "
    "and your internet connection. Free tiers may be slower than paid ones."
)