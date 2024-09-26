# Import necessary libraries and modules
import streamlit as st
from streamlit_option_menu import option_menu
import home, create, books, random_story, fan_fiction, analytics

# Set page configuration for the Streamlit app
st.set_page_config(
    page_title = "StoryForgeAI",  # Set the title of the app
    page_icon = "logo/favicon.ico",  # Set the page icon
    layout = "centered",  # Define the page layout
    menu_items = None  # No additional menu items
)

# Define a class to manage multiple app pages
class MultiApp:

    # Constructor to initialize an empty list of apps
    def __init__(self):
        self.apps = []

    # Method to add an app to the app list
    def add_app(self, title, func):
        self.apps.append({
            "title": title,  # Title of the app
            "function": func  # Function to run the app
        })

    # Method to run the selected app
    def run():
        # Sidebar menu with options to navigate between different pages
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',  # Title of the menu
                options=['Forge Hub','Start Your Tale', 'Story Vault', 'Fandom Forge', 'Forged by You', 'AI\'s Forge', 'Forge Insights'],  # App options
                default_index=0,  # Default selected option
                menu_icon="list",  # Icon for the menu
                icons=['house', 'pencil', 'collection', 'magic', 'shuffle', 'cpu', 'clipboard2-data']  # Icons for each option
                )

        # Logic to run the appropriate app based on user's choice
        if app == "Forge Hub":
            home.app()  # Run the home app
        if app == "Start Your Tale":
            create.app()  # Run the create story app
        if app == "Story Vault":
            books.app()  # Run the books app
        if app == "Fandom Forge":
            fan_fiction.app()  # Run the fan fiction app
        if app == "Forged by You":
            random_story.display_user_story()  # Display user-generated stories
        if app == "AI's Forge":
            random_story.display_ai_story()  # Display AI-generated stories
        if app == "Forge Insights":
            analytics.app()  # Run the analytics app
             
    # Execute the run method to launch the app
    run()            
