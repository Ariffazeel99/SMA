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

# Graph API URL with valid insights metrics
# Construct the API URL
base = 'https://graph.facebook.com/v19.0'
node = f'/{PAGE_ID}/insights/page_impressions'
url = base + node

# Set parameters (e.g., period: 'week')
parameters = {'period': 'week', 'access_token': PAGE_ACCESS_TOKEN}

# Make the API request
response = requests.get(url, params=parameters)
data = json.loads(response.text.encode('utf-8'))
# Make the API request


# Output the data to a JSON file
output_file = 'helpful_page_insights.json'
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

# Print a confirmation message
print(f"Page insights have been saved to {output_file}.")
