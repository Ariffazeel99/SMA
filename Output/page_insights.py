import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')

# Ensure both environment variables are set
if not PAGE_ACCESS_TOKEN or not PAGE_ID:
    raise ValueError("Please ensure PAGE_ACCESS_TOKEN and PAGE_ID are set in the .env file.")

# Graph API URL with the insights metrics you want to retrieve
url = f'https://graph.facebook.com/v17.0/{PAGE_ID}/insights'
params = {
    'metric': ','.join([
        'page_impressions',
        'page_engaged_users',
        'page_fans',
        'page_views_total',
        'page_posts_impressions',
    ]),
    'access_token': PAGE_ACCESS_TOKEN
}

# Make the API request
response = requests.get(url, params=params)

# Parse the response as JSON
data = response.json()

# Output the data to a JSON file
output_file = 'page_insights.json'
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

# Print a confirmation message
print(f"Page insights have been saved to {output_file}.")
