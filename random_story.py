import streamlit as st  # Importing Streamlit for building web applications
import fetch_data  # Importing custom module for fetching data
import random  # Importing random module for generating random numbers
import gen_ai_model  # Importing custom module for AI model interactions

# Function to display a story provided by a user from the database
def display_user_story():
    st.title("Read a Random User Input Story from the Database")  # Setting the title for the user story section
    with st.spinner("Generating Story"):  # Showing a spinner while the story is being generated
        json_data = fetch_data.fetch_json_data()  # Fetching JSON data from the database
        titles_list = fetch_data.get_titles(json_data)  # Extracting titles from the fetched data
        random_story = random.randint(0, len(titles_list))  # Generating a random index to select a story
        story_title = titles_list[random_story-1]  # Selecting a story title using the random index
        author, image_prompt, story = fetch_data.get_story(json_data, story_title)  # Fetching the story details
        image = gen_ai_model.generate_image(image_prompt)  # Generating an image based on the story prompt
        
        st.header(story_title.title())  # Displaying the story title
        try:
            st.image(image)  # Displaying the generated image
        except Exception as e:
            st.error(f"Failed to generate Image.\n\nError: {e}")  # Handling errors in image generation
        st.markdown(story)  # Displaying the story content
        
# Function to display a story generated entirely by AI
def display_ai_story():
    st.title("Read a Random AI Story generated completely by AI")  # Setting the title for the AI story section
    with st.spinner("Generating Story"):  # Showing a spinner while the story is being generated
        story_prompt = "Generate a medium length story of 3 paragraphs. Only write 3 paragraphs of story without bold or any other special characters. Write AI Generated Story completely on your own, make it human-like."
        
        ai_gen_story = gen_ai_model.get_gemini_response(story_prompt)  # Generating a story using the AI model
        
        print(ai_gen_story)  # Printing the AI-generated story for debugging purposes
        
        title_prompt = f"Generate a nice title for the story: {ai_gen_story}. Don't show in bold or add any other characters, only display the text.Just show 1 simple nice title for the story."
        ai_gen_title = gen_ai_model.get_gemini_response(title_prompt)  # Generating a title for the story using the AI model
        print(ai_gen_title)  # Printing the AI-generated title for debugging purposes
        
        image_prompt = f"Generate a nice image for the story: {ai_gen_story}."  # Preparing prompt for image generation
        image = gen_ai_model.generate_image(image_prompt)  # Generating an image based on the AI story
            
        st.header(ai_gen_title.title())  # Displaying the AI-generated story title
        try:
            st.image(image)  # Displaying the generated image
        except Exception as e:
            st.error(f"Failed to generate Image.\n\nError: {e}")  # Handling errors in image generation
        st.markdown(ai_gen_story)  # Displaying the AI-generated story content
