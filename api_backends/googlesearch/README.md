# Google Search API with FastAPI

This project integrates FastAPI with the Google Custom Search API, allowing users to fetch search results programmatically with pagination.

## Features

- **Google Search Query** – Fetches search results from Google.
- **Pagination Support** – Supports page navigation for more results.
- **Custom Number of Results** – Allows users to specify how many results to retrieve.

## Prerequisites

- **Google Cloud Account**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- **Enable Custom Search JSON API**: [Google Custom Search API](https://developers.google.com/custom-search/v1/overview)
- **Google API Key** and **Search Engine ID (cx)**.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/google_search_fastapi.git
   cd google_search_fastapi
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

### **1. Search Google (with Pagination)**
```sh
curl -X GET "http://127.0.0.1:8000/search?query=fastapi&num_results=5&page=1"
```

Example JSON Response:
```json
{
  "query": "fastapi",
  "page": 1,
  "num_results": 5,
  "results": [
    {
      "title": "FastAPI - The Next Big Thing",
      "link": "https://fastapi.tiangolo.com/",
      "snippet": "FastAPI is a modern, high-performance web framework..."
    }
  ]
}
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
