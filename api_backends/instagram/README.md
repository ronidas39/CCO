# Instagram Ads API with FastAPI

This project integrates FastAPI with the Instagram Ads API, allowing you to schedule and automate ad management.

## Features

- **Create Instagram Ads** with images, captions, and call-to-actions.
- **Schedule Ads** for specific time slots.
- **Track Ad Performance** with impressions, clicks, and conversions.
- **Automate Budget Adjustments** to optimize ad spend.

## Prerequisites

- **Meta Developer Account**: [https://developers.facebook.com](https://developers.facebook.com/)
- **Instagram Business Account** linked to a Meta Business Account.
- **Facebook App** with `ads_management` permission.
- **Access Token** with required permissions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/instagram_ads_fastapi.git
   cd instagram_ads_fastapi
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

### **1. Create an Instagram Ad Creative**
```sh
curl -X POST "http://127.0.0.1:8000/create-ad-creative"      -H "Content-Type: application/json"      -d '{"image_url": "https://yourimageurl.com/image.jpg", "caption": "Best product ever!"}'
```

### **2. Create an Instagram Ad (Scheduled)**
```sh
curl -X POST "http://127.0.0.1:8000/create-instagram-ad"      -H "Content-Type: application/json"      -d '{"adset_id": "your_adset_id", "creative_id": "your_creative_id", "start_time": 1712345678, "end_time": 1712445678}'
```

### **3. Get Ad Performance Insights**
```sh
curl -X GET "http://127.0.0.1:8000/ads-insights?ad_id=your_ad_id"
```

### **4. Update Ad Budget**
```sh
curl -X POST "http://127.0.0.1:8000/update-ad-budget"      -H "Content-Type: application/json"      -d '{"adset_id": "your_adset_id", "new_budget": 2000}'
```

## Deployment

For production, deploy on AWS, GCP, or DigitalOcean.

## License

MIT
