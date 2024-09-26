# Import necessary libraries and modules
import streamlit as st
import fetch_data  # Module to fetch story data from API
import gen_ai_model  # Module to generate images based on story prompts

# Define the app function that handles the Story Vault page
def app():
    # Fetch the JSON data from the API containing story information
    json_data = fetch_data.fetch_json_data()  # Get story data in JSON format
    titles = fetch_data.get_titles(json_data)  # Extract the list of story titles
    
    st.title("Story Vault")  # Set the title of the page
    
    # Show only the first 10 story titles
    limited_titles = titles[:10]  # Limit the number of titles to 10
    
    # Create two columns for layout (col1 for titles, col2 for story content)
    col1, col2 = st.columns([1, 3], gap="large")  # col1 is for buttons, col2 is for displaying content

    # Create placeholders in col2 to display story details dynamically
    title_placeholder = col2.empty()  # Placeholder for story title
    author_placeholder = col2.empty()  # Placeholder for author name
    image_placeholder = col2.empty()  # Placeholder for story image
    story_placeholder = col2.empty()  # Placeholder for story content
    
    # Flag to check if any story button has been clicked
    story_selected = False

    # Left column: Display buttons for each of the first 10 story titles
    with col1:
        for title in limited_titles:
            # Create a button for each title in the left column (col1)
            button = st.button(label=title, use_container_width=True)
            if button:
                # When a button is clicked, fetch and display the corresponding story in col2
                with st.spinner("Extracting story..."):  # Show a spinner while loading the story
                    author, image_prompt, story = fetch_data.get_story(json_data, title)  # Get story details
                    story_selected = True  # Set flag to true when a story is selected
                    
                    image = gen_ai_model.generate_image(image_prompt)  # Generate an image based on the story prompt
                    
                    # Update the placeholders in col2 with the selected story details
                    title_placeholder.title(title)  # Display the story title
                    author_placeholder.header(author)  # Display the author's name
                    image_placeholder.image(image)  # Display the generated image
                    story_placeholder.write(story)  # Display the story content
    
    # Default message in col2 before any story is selected
    if not story_selected:
        with col2:
            story_placeholder.header("Click a button from the title buttons to read a story")  # Default message

# Run the app if this file is executed directly
if __name__ == "__main__":
    app()  # Call the app function to run the Story Vault page
