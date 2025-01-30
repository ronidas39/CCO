# Google My Business API with FastAPI

This project integrates FastAPI with the Google My Business API, allowing businesses to manage locations, retrieve business information, and create posts.

## Features

- **Retrieve Business Information** – Get details about the business account.
- **Fetch Business Locations** – List all locations associated with the business.
- **Create Google Posts** – Publish updates, promotions, or events on Google.

## Prerequisites

- **Google Cloud Account**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- **Enable Google My Business API**: [Google My Business API](https://developers.google.com/my-business/)
- **Google API Key** and **Google My Business Account ID**.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/google_my_business_fastapi.git
   cd google_my_business_fastapi
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

### **1. Fetch Business Information**
```sh
curl -X GET "http://127.0.0.1:8000/business/info"
```

### **2. Fetch Business Locations**
```sh
curl -X GET "http://127.0.0.1:8000/locations"
```

### **3. Create a Google My Business Post**
```sh
curl -X POST "http://127.0.0.1:8000/posts"      -H "Content-Type: application/json"      -d '{"summary": "Exciting new offer available!", "action_url": "https://yourwebsite.com"}'
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
