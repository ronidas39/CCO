# Meta Ads API with FastAPI

This project integrates FastAPI with Meta Ads API to manage Facebook and Instagram ads programmatically.

## Features

- **Create Campaigns** with different objectives.
- **Manage Ad Sets**: Set targeting and budgets.
- **Create Ads** using pre-created ad creatives.
- **Fetch Campaigns, Ad Sets, and Ads** for analysis.

## Prerequisites

- **Meta Developer Account**: [https://developers.facebook.com](https://developers.facebook.com/)
- **Facebook App** with "ads_management" permission.
- **Business Manager Account** with admin access.
- **Access Token** with `ads_read` and `ads_management` permissions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourrepo/meta_ads_fastapi.git
   cd meta_ads_fastapi
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

### **1. Create a Campaign**
```sh
curl -X POST "http://127.0.0.1:8000/create-campaign"      -H "Content-Type: application/json"      -d '{"name": "New Campaign", "objective": "LINK_CLICKS", "status": "PAUSED"}'
```

### **2. Create an Ad Set**
```sh
curl -X POST "http://127.0.0.1:8000/create-adset"      -H "Content-Type: application/json"      -d '{"name": "Test Ad Set", "campaign_id": "123456", "daily_budget": 1000, "targeting": {"geo_locations": {"countries": ["US"]}}}'
```

### **3. Create an Ad**
```sh
curl -X POST "http://127.0.0.1:8000/create-ad"      -H "Content-Type: application/json"      -d '{"name": "Test Ad", "adset_id": "123456", "creative_id": "654321"}'
```

### **4. Get Campaigns**
```sh
curl -X GET "http://127.0.0.1:8000/get-campaigns"
```

### **5. Get Ad Sets**
```sh
curl -X GET "http://127.0.0.1:8000/get-adsets"
```

### **6. Get Ads**
```sh
curl -X GET "http://127.0.0.1:8000/get-ads"
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
