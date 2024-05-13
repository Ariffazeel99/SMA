import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the User Access Token from the environment variables
USER_ACCESS_TOKEN = os.getenv('USER_ACCESS_TOKEN')

if not USER_ACCESS_TOKEN:
    raise ValueError("Please ensure USER_ACCESS_TOKEN is set in the .env file.")

# Graph API endpoint to list pages managed by the user
url = f'https://graph.facebook.com/v17.0/me/accounts?access_token={USER_ACCESS_TOKEN}'

# Make the API request
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Print the pages and their access tokens
print("Pages Information:")
print(data)

# Save the first page's access token (if available)
if 'data' in data and len(data['data']) > 0:
    page_access_token = data['data'][0]['access_token']
    page_id = data['data'][0]['id']
    with open('page_access_token.json', 'w') as file:
        file.write(page_access_token)
    print(f"Page Access Token for Page ID {page_id} saved to page_access_token.json: {page_access_token}")
else:
    print("No pages found or the user does not have the necessary permissions.")
