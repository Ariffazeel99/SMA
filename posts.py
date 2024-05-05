import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')

# Ensure both environment variables are set
if not PAGE_ACCESS_TOKEN or not PAGE_ID:
    raise ValueError("Please ensure PAGE_ACCESS_TOKEN and PAGE_ID are set in the .env file.")

# Graph API URL to fetch posts from the page
url = f'https://graph.facebook.com/v17.0/{PAGE_ID}/posts?access_token={PAGE_ACCESS_TOKEN}'

# Make the API request
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Output the posts data to a JSON file
output_file = 'page_posts.json'
with open(output_file, 'w') as file:
    file.write(response.text)

# Print a confirmation message and some posts information
print(f"Page posts have been saved to {output_file}.")
if 'data' in data:
    print(f"Number of posts retrieved: {len(data['data'])}")
else:
    print(f"Error retrieving posts: {data}")
