import requests

# Replace with your actual Page Access Token and Page ID
PAGE_ACCESS_TOKEN = ''
PAGE_ID = '101569698587025'

# Graph API URL with the fields you want to retrieve
url = f'https://graph.facebook.com/v17.0/{PAGE_ID}?fields=id,name,about,fan_count&access_token={PAGE_ACCESS_TOKEN}'

# Make the API request
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Print the page information
print("Page Information:")
print(data)
