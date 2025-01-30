# Perplexity API with FastAPI

This project integrates FastAPI with the Perplexity API, enabling AI-powered search and Q&A capabilities.

## Features

- **Query Perplexity AI** – Send messages and receive responses.
- **Customizable Model Parameters** – Control max tokens, temperature, etc.
- **Secure API Key Handling** – Uses environment variables for security.

## Prerequisites

- **Perplexity API Key**: Register at [Perplexity API](https://docs.perplexity.ai/guides/getting-started).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/perplexity_fastapi.git
   cd perplexity_fastapi
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env` file.

## Running the Server

Run FastAPI using Uvicorn:

```sh
uvicorn main:app --reload
```

## API Endpoints

### **1. Query Perplexity API**
```sh
curl -X POST "http://127.0.0.1:8000/query"      -H "Content-Type: application/json"      -d '{
           "model": "sonar-pro",
           "messages": [
             {"role": "system", "content": "Be precise and concise."},
             {"role": "user", "content": "What is the capital of France?"}
           ],
           "max_tokens": 50,
           "temperature": 0.7
         }'
```

Example Response:
```json
{
  "choices": [
    {
      "message": {
        "content": "The capital of France is Paris."
      }
    }
  ]
}
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
