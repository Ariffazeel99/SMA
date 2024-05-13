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
metrics = "page_impressions,page_engaged_users"
url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/insights"
params = {
    "metric": metrics,
    "access_token": PAGE_ACCESS_TOKEN
}

try:
    # Perform the API request
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Parse and save the JSON response
    data = response.json()
    output_file = 'facebook_insights.json'
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Insights data saved to {output_file}")

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Something went wrong: {err}")
