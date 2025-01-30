# Flodesk API Integration with FastAPI

This project integrates FastAPI with the Flodesk API, allowing you to manage subscribers, segments, and webhooks programmatically.

## Features

- **Create or Update Subscribers**: Add new subscribers or update existing ones.
- **Retrieve Subscriber Information**: Fetch details of a specific subscriber.
- **List Segments**: Retrieve all segments in your Flodesk account.
- **Add Subscriber to Segments**: Assign subscribers to one or more segments.
- **Create Webhooks**: Set up webhooks to receive event notifications.

## Prerequisites

- **Flodesk Account**: Ensure you have an active Flodesk account.
- **API Key**: Generate an API key from your Flodesk account settings.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/flodesk_fastapi.git
   cd flodesk_fastapi
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Rename `.env.example` to `.env`.
   - Add your Flodesk API key to the `.env` file:
     ```
     FLODESK_API_KEY=your_flodesk_api_key
     ```

4. **Run the Application**:
   ```sh
   uvicorn main:app --reload
   ```

## Usage

- **Create or Update Subscriber**:
  - Endpoint: `POST /subscribers`
  - Payload:
    ```json
    {
      "email": "subscriber@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "custom_fields": {
        "field_key": "value"
      }
    }
    ```

- **Retrieve Subscriber**:
  - Endpoint: `GET /subscribers/{subscriber_id}`

- **List Segments**:
  - Endpoint: `GET /segments`

- **Add Subscriber to Segments**:
  - Endpoint: `POST /subscribers/{subscriber_id}/segments`
  - Payload:
    ```json
    {
      "segment_ids": ["segment_id_1", "segment_id_2"]
    }
    ```

- **Create Webhook**:
  - Endpoint: `POST /webhooks`
  - Payload:
    ```json
    {
      "url": "https://yourwebhookurl.com",
      "events": ["subscriber.created", "subscriber.updated"]
    }
    ```

## Notes

- Ensure your environment variables are set correctly.
- Replace placeholder values with actual data when making requests.

## License

This project is licensed under the MIT License.
