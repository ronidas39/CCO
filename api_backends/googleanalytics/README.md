# Google Analytics API with FastAPI

This project integrates FastAPI with the Google Analytics API, allowing users to fetch website analytics data programmatically.

## Features

- **Retrieve Analytics Reports** – Fetch session data, page views, and other metrics.
- **Custom Metrics & Dimensions** – Specify which metric and dimension to query.
- **Date Filtering** – Filter results by start and end dates.

## Prerequisites

- **Google Cloud Account**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- **Enable Google Analytics API**: [Google Analytics API](https://developers.google.com/analytics/devguides/reporting)
- **Google API Key** and **Google Analytics Property ID**.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/google_analytics_fastapi.git
   cd google_analytics_fastapi
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

### **1. Fetch Google Analytics Report**
```sh
curl -X GET "http://127.0.0.1:8000/analytics/report?metric=sessions&dimension=date&start_date=7daysAgo&end_date=today"
```

Example JSON Response:
```json
{
  "rows": [
    {
      "dimensionValues": [{"value": "2024-01-01"}],
      "metricValues": [{"value": "100"}]
    },
    {
      "dimensionValues": [{"value": "2024-01-02"}],
      "metricValues": [{"value": "120"}]
    }
  ]
}
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
