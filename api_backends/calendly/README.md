# Calendly API with FastAPI

This project integrates FastAPI with Calendly API to manage meetings and automate scheduling.

## Features

- **Get User Information** – Retrieve details about the authenticated user.
- **Get Available Event Types** – Fetch event types a user offers.
- **List Scheduled Events** – Retrieve upcoming and past scheduled meetings.
- **Create Webhooks** – Get notified when meetings are scheduled or canceled.

## Prerequisites

- **Calendly Developer Account**: [https://developer.calendly.com/](https://developer.calendly.com/)
- **Generate an API Token** via Calendly's Developer Portal.
- **Add the token** to `.env` file.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourrepo/calendly_fastapi.git
   cd calendly_fastapi
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env` file.

## Running the Server

Run FastAPI using Uvicorn:

```sh
uvicorn main:app --reload
```

## API Endpoints

### **1. Get User Info**
```sh
curl -X GET "http://127.0.0.1:8000/user-info"
```

### **2. Get Event Types**
```sh
curl -X GET "http://127.0.0.1:8000/event-types"
```

### **3. Get Scheduled Events**
```sh
curl -X GET "http://127.0.0.1:8000/scheduled-events"
```

### **4. Create a Webhook**
```sh
curl -X POST "http://127.0.0.1:8000/create-webhook"      -H "Content-Type: application/json"      -d '{"url": "https://yourwebhook.com", "events": ["invitee.created", "invitee.canceled"]}'
```

## Webhook Event Types

| Event Type          | Description |
|---------------------|-------------|
| `invitee.created`  | Triggered when a new meeting is scheduled. |
| `invitee.canceled` | Triggered when a meeting is canceled. |

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
