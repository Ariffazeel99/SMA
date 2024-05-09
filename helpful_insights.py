import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
PAGE_ID = os.getenv('PAGE_ID')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')

# Check if both variables were loaded
if not PAGE_ID or not PAGE_ACCESS_TOKEN:
    raise ValueError("Missing PAGE_ID or PAGE_ACCESS_TOKEN from environment variables")

# Define the metrics to query
metrics = "page_fan_adds,page_fan_removes,page_impressions,page_engaged_users"
url = f"https://graph.facebook.com/v16.0/{PAGE_ID}/insights"
params = {
    "metric": metrics,
    "access_token": PAGE_ACCESS_TOKEN
}

# Perform the API request
response = requests.get(url, params=params)

if response.status_code == 200:
    # Parse and save the JSON response
    data = response.json()
    output_file = 'facebook_insights.json'
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Insights data saved to {output_file}")
else:
    print(f"Error: {response.status_code} - {response.text}")
