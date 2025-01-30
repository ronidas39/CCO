# Threads API Integration with FastAPI

This project integrates FastAPI with Meta's Threads API, allowing you to authenticate, create, and manage threads programmatically.

## Features

- **OAuth 2.0 Authentication** – Secure login to Meta Threads API.
- **Create Threads** – Post messages as Threads.
- **Handle Callbacks** – Exchange authorization code for an access token.

## Prerequisites

- **Meta Developer Account**: [https://developers.facebook.com](https://developers.facebook.com/)
- **Facebook App** configured for the Threads API.
- **Access Token** with required permissions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/threads_fastapi.git
   cd threads_fastapi
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

### **1. Login to Threads API**
```sh
curl -X GET "http://127.0.0.1:8000/login"
```

### **2. Handle OAuth Callback**
```sh
curl -X GET "http://127.0.0.1:8000/callback?code=your_auth_code"
```

### **3. Create a New Thread**
```sh
curl -X POST "http://127.0.0.1:8000/threads"      -H "Content-Type: application/json"      -d '{"message": "This is my first thread!"}'
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
