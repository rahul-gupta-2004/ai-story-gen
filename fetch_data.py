import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd

load_dotenv()

# Airtable API base information
base_id = os.getenv("AIRTABLE_BASE_ID")  # Base ID for Airtable
table_id = os.getenv("AIRTABLE_TABLE_ID")  # Table ID for Airtable
personal_access_token = os.getenv("AIRTABLE_PERSONAL_ACCESS_TOKEN")  # Personal access token for authentication

# Create headers for the Airtable API
def create_headers():
    headers = {
        'Authorization': f'Bearer {personal_access_token}',  # Authorization using the personal access token
        'Content-Type': 'application/json',  # Setting the content type to JSON
    }
    return headers

# Base API URL for Airtable
base_table_api_url = f'https://api.airtable.com/v0/{base_id}/{table_id}'  # Construct the full API URL

# Function to fetch JSON data from Airtable
def fetch_json_data():
    headers = create_headers()  # Create the headers for the API request
    
    # Parameters to sort records by timestamp in descending order
    params = {
        'sort[0][field]': 'timestamp',
        'sort[0][direction]': 'desc'
    }
    
    # Send GET request to Airtable API
    response = requests.get(base_table_api_url, headers=headers, params=params)
    
    # Decode the response content to a string format
    decoded_content = response.content.decode('utf-8')
    
    # Parse the decoded string into JSON format
    json_data = json.loads(decoded_content)
    
    # Return the parsed JSON data
    return json_data

# Function to extract titles from JSON data
def get_titles(json_data):
    titles = []  # Initialize an empty list to store the titles

    # Loop through the records in the JSON data
    for record in json_data.get('records', []):
        # Extract the 'title' field and add to the list if it exists
        title = record['fields'].get('title', None)
        if title:
            titles.append(title)
    
    return titles

# Function to retrieve story details based on a given title
def get_story(json_data, title):
    # Loop through the records to find a story matching the title
    for record in json_data.get('records', []):
        if record['fields'].get('title', '') == title:
            # Extract fields such as author, image prompt, and story
            author = record['fields'].get('author', 'Unknown Author')
            image_prompt = record['fields'].get('image_prompt', 'No image prompt available')
            story = record['fields'].get('story', 'No story available')
            return author, image_prompt, story
    
    # Return a default message if no matching title is found
    return 'No story found with the given title.'

# Function to extract timestamps from JSON data
def get_timestamp(json_data):
    timestamps = []  # Initialize an empty list for timestamps

    # Loop through the records in the JSON data
    for record in json_data.get('records', []):
        # Extract the 'timestamp' field and add to the list if it exists
        timestamp = record['fields'].get('timestamp', None)
        if timestamp:
            timestamps.append(timestamp)
    
    return timestamps

# Function to get the length of each story
def get_story_len(json_data):
    story_len = []  # Initialize an empty list for story lengths

    # Loop through the records in the JSON data
    for record in json_data.get('records', []):
        # Extract the story content and calculate its length
        story = record['fields'].get('story', None)
        if story:
            story_len.append(len(story))
    
    return story_len
