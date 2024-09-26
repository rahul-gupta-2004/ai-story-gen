import requests  # Importing requests library to handle HTTP requests
import json  # Importing json library to handle JSON data

# Airtable API base information
base_id = 'app0Kqdh73MydcvPy'  # The unique identifier for the Airtable base
table_id = 'tblVJjI2xOGgQpVQi'  # The unique identifier for the table within the base
personal_access_token = 'patPfJNPtzOHuF9Xw.a8b362f576229d42a88f8b99ed831b30656143ecd485c05d406c82dcf5a951b1'  # Personal access token for API authentication

# Create headers for the Airtable API
def create_headers():
    headers = {
        'Authorization': f'Bearer {personal_access_token}',  # Authorization header with the token
        'Content-Type': 'application/json',  # Content type header for JSON
    }
    return headers  # Return the headers for use in requests


# Base API URL for Airtable
base_table_api_url = f'https://api.airtable.com/v0/{base_id}/{table_id}'  # Constructing the API URL using base and table IDs

# Function to save a story to Airtable
def save_to_airtable(timestamp, title, author, image_prompt, story):
    headers = create_headers()  # Create headers for the API request
    # Data payload for Airtable API
    data = {
        'fields': {
            'timestamp': timestamp,  # Timestamp of when the story is saved
            'title': title,  # Title of the story
            'author': author,  # Author of the story
            'image_prompt': image_prompt,  # Image prompt for story illustration
            'story': story  # The actual story content
        }
    }
    # Send POST request to Airtable API to add a new record
    response = requests.post(
        base_table_api_url, headers=headers, data=json.dumps(data))  # Convert data to JSON format and send request
    # Return the response status for logging purposes
    return response.status_code, response.content  # Return the status code and response content
