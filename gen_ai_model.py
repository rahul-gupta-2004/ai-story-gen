import google.generativeai as genai  # Importing the Google Generative AI library
import requests  # Importing the requests library for making HTTP requests

# Function to get a response from the Gemini AI model
def get_gemini_response(input_prompt):
    # Configure the API key for accessing the Google Generative AI services
    genai.configure(api_key='AIzaSyCN8rvxlb7fJ3IGmqMCxybxgBBwib6eBgo')

    # Create an instance of the GenerativeModel for the specified model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate content based on the input prompt
    response = model.generate_content(input_prompt)
    
    # Check if the response has a finish message and return it
    if hasattr(response, 'finish_message'):
        return response.finish_message
    # If not, check if the response has text and return it
    elif hasattr(response, 'text'):
        return response.text
    else:
        # Return a default message if no valid response is received
        return "No valid response received."

# Function to generate an image based on the input prompt
def generate_image(input_prompt):
    # API URL for the Stable Diffusion model
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    # Authorization header with Bearer token for accessing the API
    headers = {"Authorization": "Bearer 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"}
    
    # Send a POST request to the API with the input prompt
    response = requests.post(API_URL, headers=headers, json={"inputs": input_prompt})
    
    # Return the raw content of the response
    return response.content
