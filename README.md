# Mini AI Aggregator

A beginner-friendly Python web app that sends your prompt to **3 different AI providers** at once and shows you the responses side by side so you can compare them.

Inspired by [Eden AI](https://www.edenai.run/) — but simplified for learning!

---

##  What It Does

1. You type a question or prompt in a text box
2. Click **"Compare AI Responses"**
3. The app sends your prompt to **3 AI providers simultaneously**:
   - **Groq** (Llama 3 70B)
   - **Cohere** (Command R)
   - **Mistral AI** (Mistral Small)
4. You see all 3 responses in **side-by-side columns**
5. Each response shows:
   - The AI's answer
   - ⏱ Response time in seconds
   - 📝 Word count

---

## 📁 Project Structure

```
MiniAIAggregator/
├── app.py                  # Main app - run this to start!
├── groq_api.py             # Groq function (Llama 3 70B)
├── cohere_api.py           # Cohere function (Command R)
├── mistral_api.py          # Mistral AI function (Mistral Small)
├── .env                    #  Your API keys (keep this secret!)
├── .gitignore              # Tells Git to ignore .env
├── requirements.txt        # List of Python packages to install
└── README.md               # This file - instructions for you!
```

---

## 🛠️ What You Need Before Starting

### 1. Python 3.8 or higher
Check if you have Python installed:
```bash
python --version
```
If you don't have Python, download it from [python.org](https://www.python.org/downloads/).

### 2. Free API keys from 3 AI providers

You need to sign up for **free API keys** from each provider. None of them require a credit card for the free tier:

| Provider | Where to Sign Up | What You Get |
|---|---|---|
| **Groq** | [console.groq.com/keys](https://console.groq.com/keys) | Free API key (no credit card) |
| **Cohere** | [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys) | Free tier API key |
| **Mistral AI** | [console.mistral.ai/api-keys](https://console.mistral.ai/api-keys) | Free API key (1M tokens/day) |

**Quick steps for each:**

**Groq:**
1. Go to [console.groq.com](https://console.groq.com) and sign up
2. Go to [API Keys](https://console.groq.com/keys)
3. Click "Create API Key"
4. Copy the key (it starts with `gsk_...`)

**Cohere:**
1. Go to [cohere.com](https://cohere.com) and sign up
2. Go to [API Keys](https://dashboard.cohere.com/api-keys)
3. Copy your API key

**Mistral AI:**
1. Go to [console.mistral.ai](https://console.mistral.ai) and sign up
2. Go to [API Keys](https://console.mistral.ai/api-keys)
3. Click "Create new API key"
4. Copy the key

---

## How to Install and Run

### Step 1: Open your terminal

On Mac: Press `Cmd + Space`, type "Terminal", press Enter.

### Step 2: Navigate to the project folder

```bash
cd /Users/wasifamjad/MiniAIAggregator
```

### Step 3: Install the required packages

```bash
pip install -r requirements.txt
```

This installs:
- **streamlit** — creates the web interface
- **groq** — connects to Groq's API
- **cohere** — connects to Cohere's API
- **requests** — connects to Mistral AI's API
- **python-dotenv** — loads your API keys from the `.env` file

### Step 4: Add your API keys

1. Open the `.env` file in any text editor
2. Replace the placeholder values with your actual API keys:

```bash
GROQ_API_KEY=gsk-your_actual_groq_key_here
COHERE_API_KEY=your_actual_cohere_key_here
MISTRAL_API_KEY=your_actual_mistral_key_here
```

 **Important:** Never share your `.env` file or commit it to GitHub! The `.gitignore` file already prevents this.

### Step 5: Run the app!

```bash
streamlit run app.py
```

Your browser should automatically open at `http://localhost:8501`. If it doesn't, open your browser and go to that address.

---

## How to Use the App

1. Type a question in the text box (e.g., "What is machine learning?")
2. Click the **" Compare AI Responses"** button
3. Wait a few seconds while the app calls all 3 AI providers
4. See the responses displayed side by side in 3 columns
5. Compare the response times and word counts!

---

## How the Code Works (For Beginners)

### `app.py` — The Main File

This is the heart of the app. It:
1. Loads your API keys from `.env` using `python-dotenv`
2. Creates a web page with Streamlit (a library that turns Python into a web app)
3. When you click "Compare", it calls the 3 API functions
4. Displays the results in 3 columns using `st.columns(3)`

### `groq_api.py`, `cohere_api.py`, `mistral_api.py`

Each of these files contains **one function** that:
1. Takes your prompt text and an API key
2. Sends the prompt to the AI provider's server
3. Measures how long the request takes (in seconds)
4. Returns the response text and the time

The functions are in separate files to keep the code organized. Think of them like separate tools in a toolbox — `app.py` is the worker that uses all three tools.

### Error Handling

If an API call fails (wrong key, no internet, etc.), the app **doesn't crash**. Instead, it shows a friendly error message in that column, and the other two columns still work fine.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `pip install` fails | Make sure Python is installed: `python --version` |
| "API keys not found" | Check your `.env` file has the correct keys and is in the right folder |
| "Module not found" error | Run `pip install -r requirements.txt` again |
| Mistral AI is slow | Free tier has rate limits — responses may take a few seconds |
| App doesn't open in browser | Go to `http://localhost:8501` manually |

---

## What You'll Learn

This project teaches you:
- **How APIs work** — sending requests and getting responses over the internet
- **Environment variables** — storing secrets safely with `.env` files
- **Modular code** — splitting code into separate files for organization
- **Error handling** — making apps that fail gracefully instead of crashing
- **Streamlit** — building web apps with pure Python
- **AI comparison** — seeing how different AI models answer the same question

---

## Going Further (Ideas for Next Steps)

Once this works, try:
- Add more AI providers (Google Gemini, Anthropic Claude, etc.)
- Add a dark/light mode toggle
- Save results to a file or database
- Add a history feature to see past comparisons
- Deploy the app online with Streamlit Cloud

---

## License

This project is for learning purposes. Feel free to use, modify, and share it!
