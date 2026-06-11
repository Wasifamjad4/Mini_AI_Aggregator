# 🤖 Mini AI Aggregator

A Streamlit application that aggregates responses from three AI providers side-by-side:

- **Groq** (model: llama-3.3-70b-versatile)
- **Cohere** (model: command-r-08-2024, v2 API)
- **Mistral AI** (model: mistral-small-latest)

## Features

- Query all three AI models simultaneously with a single prompt
- Displays response time and word count for each provider
- Clean, responsive three-column layout
- Graceful error handling

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API keys:**

   Edit the `.env` file with your API keys.

3. **Run the application:**

   ```bash
   python3 -m streamlit run main.py
   ```

## Project Structure

```
MiniAIAggregator/
├── main.py              # Main Streamlit application
├── apis/
│   ├── __init__.py      # Package initializer
│   ├── groq_api.py      # Groq API integration
│   ├── cohere_api.py    # Cohere API integration
│   └── mistral_api.py   # Mistral AI API integration
├── .env                 # API keys (not committed)
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## API Providers

| Provider | Model |
|----------|-------|
| Groq | llama-3.3-70b-versatile |
| Cohere | command-r-08-2024 |
| Mistral AI | mistral-small-latest |
