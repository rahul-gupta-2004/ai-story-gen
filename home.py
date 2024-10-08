import streamlit as st  # Importing Streamlit for building web applications
import json  # Importing JSON for handling JSON data
from streamlit_lottie import st_lottie  # Importing Lottie for animations in Streamlit

# Main application function
def app():
    col1, col2 = st.columns(2)  # Creating two columns for layout
    with col1:
        # Loading and displaying a Lottie animation from a JSON file
        with open('animation/book.json', 'r') as file:
            url_json = json.load(file)  # Load the animation JSON data
        st.lottie(url_json)  # Display the Lottie animation
    with col2:
        # Setting the title and subheader for the app
        st.title("Welcome to StoryForgeAI!")
        st.subheader("Where Stories are Forged from Code and Creativity!!")
    
    # Displaying the features of the application
    st.subheader("Features:")
    features_ul = """
            <ul style="list-style-type:circle; padding-left: 20px">
                <li> <b> Story Customization: </b> Allow users to input their own characters, settings, plot points, or themes for a personalized story. </li>
                <li> <b> Interactive Prompts: </b> Let users answer interactive questions to help guide the AI in creating the story plot. </li>
                <li> <b> Random Story Generator: </b> Provide a one-click option to generate random stories with pre-set themes or genres. </li>
                <li> <b> Genre Selection: </b> Offer different genres like adventure, romance, sci-fi, fantasy, mystery, etc., for users to choose from. </li>
                <li> <b> Story-Based Image Generation: </b> Automatically generate a unique AI-created image for each story, based on its plot, characters, or setting. This feature allows users to visualize their stories with custom illustrations that align with the narrative, enhancing the storytelling experience. </li>
            </ul>
            """
    st.markdown(features_ul, unsafe_allow_html=True)  # Display the features as HTML

    # Displaying the technology stack used in the application
    st.subheader("Tech Stack:")
    st.write('')  # Adding some spacing
    st.write('')  # Adding some spacing
    
    # Lists of technologies and their descriptions
    tech_list = [
        "Python", "Airtable", "Hugging Face", "Gemini API", "Lottie Animation"
    ]
    tech_list_desc = [
        '''Python
        \n<b> Streamlit </b>: A powerful and easy-to-use framework for creating data-driven web applications. It allows you to build and deploy interactive applications quickly using Python.
        \n<b> Backend </b> : Python is used for the backend logic, handling data processing, and integrating various APIs.''', 
        '''Airtable
        \n<b> Database </b> : Airtable is used to store and manage data in a flexible and user-friendly manner. It combines the simplicity of a spreadsheet with the power of a database.''', 
        '''Hugging Face Stable Diffusion API
        \n<b> Text-to-Image Generation </b>: This API is used to generate images from text descriptions, particularly for creating story cover pages. It leverages advanced machine learning models to produce high-quality images.''', 
        '''Gemini API
        \n<b>Image and Story Prompt Generation </b>: The Gemini API generates images and story prompts based on user inputs, enhancing the creative aspects of your application.''', 
        '''Lottie Animation
        \n<b>Home Page Animation </b>: A Lottie animation is used on the home page to create engaging and visually appealing animations. Lottie allows for high-quality animations that are lightweight and easy to implement.'''
    ]
    
    # Image URLs for the technologies
    tech_image_url = [
        'logo/python.png',
        'logo/airtable.png',
        'logo/hugging-face.png',
        'logo/gemini.png',
        'logo/lottie-files.webp'   
    ]
    
    # Creating a table to display technology information
    table_data = []  # List to hold table data
    for i in range(len(tech_list)):
        image = tech_image_url[i]  # Get image URL
        table_data.append([i + 1, image, tech_list[i], tech_list_desc[i]])  # Append row data
    
    # Displaying the technology information in a structured format
    for row in table_data:
        col1, col2, col3 = st.columns([1, 2, 4])  # Create three columns for each row
        with col1:
            st.markdown(f"**{row[0]}**")  # Display the index
        with col2:
            st.image(row[1], caption=row[2], width=125)  # Display the technology image
        with col3:
            st.markdown(row[3], unsafe_allow_html=True)  # Display the technology description
        
        st.divider()  # Add a divider between rows
