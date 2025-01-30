# WhatsApp Business API with FastAPI

This project integrates FastAPI with WhatsApp Business API (Cloud API) to send and receive messages.

## Prerequisites

- **Meta Business Manager** account with WhatsApp Business API access.
- A registered **WhatsApp Business phone number**.
- A verified **Webhook URL**.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourrepo/whatsapp_fastapi.git
   cd whatsapp_fastapi
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

## Sending a Message

Make a `POST` request:

```sh
curl -X POST "http://127.0.0.1:8000/send-message/" -H "Content-Type: application/json" -d '{"to": "recipient_phone_number", "message": "Hello from FastAPI!"}'
```

## Webhook Setup

- Expose your local server using **ngrok**:
  ```sh
  ngrok http 8000
  ```
- Set the webhook URL in **Meta Business Manager**.

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
