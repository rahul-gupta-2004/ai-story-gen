import streamlit as st

import gen_ai_model

# Function to handle the fan fiction story generation
def app():
    st.title("Fandom Forge")  # Display the title of the app

    # Input field for story plot
    story_plot = st.text_area("Story Plot (required)")
    # Input field for author's name (optional)
    author = st.text_input("Author (optional)", value="Anonymous")
    # Multi-selection input for genres
    genre = st.multiselect("Genre (required)", options=["Fantasy", "Mystery", "Romance", "Sci-Fi", "Adventure", "Thriller", "Non-Fiction"], max_selections=3, placeholder="AI Choice")
    # Input field for main character
    main_char = st.text_input("Main Character (required)")
    # Multi-selection input for fandoms
    fandoms = st.multiselect("Select Fandoms (required)", options=["Harry Potter", "Star Wars", "Marvel Cinematic Universe", "Lord of the Rings", "Game of Thrones", "DC Comics", "Star Trek", "Percy Jackson", "The Witcher", "Avatar: The Last Airbender", "The Hunger Games", "Sherlock Holmes", "Supernatural", "Doctor Who", "Pokémon", "Naruto", "The Legend of Zelda", "The Matrix", "Stranger Things", "Disney/Pixar"], max_selections=6)
    
    # Button to submit the form
    submit = st.button("Submit")

    if submit:
        # Check if required fields are filled
        if story_plot == "" or main_char == "" or len(genre) == 0 or len(fandoms) == 0:
            st.error("Please fill in all **required** fields", icon="⚠️")  # Show error if required fields are missing
        else:
            # Spinner to indicate story generation in progress
            with st.spinner("Generating your story..."):
                # Construct the prompt for the AI model
                prompt = f"Generate a medium length story of 3 paragraphs based on the: {story_plot}. The story should be in the following genres: {genre}. The story should mainly focus on the {main_char}. The story should be based in these fandoms: {fandoms}. The story should cover the fandoms and make the story revolve around these fandoms: {fandoms}. Make the story as much imaginative and creative as much possible. Don't generate the story in bold or add any other characters, only display the text. Also don't display the title of the story, just display the text of the story."

                # Fetch the generated story from the AI model
                ai_story = gen_ai_model.get_gemini_response(prompt)

                # Create an image based on the generated story
                image_prompt = f"Generate a nice image for the story: {ai_story}."
                image = gen_ai_model.generate_image(image_prompt)

                # Generate a title for the story
                story_title_prompt = f"Generate a nice title for the story: {ai_story}. Don't show in bold or add any other characters, only display the text. Just show 1 simple nice title for the story."
                story_title = gen_ai_model.get_gemini_response(story_title_prompt)
            
                # Display the generated title, author, image, and story
                st.header(story_title.title())  # Display the story title
                st.subheader("By " + author.title())  # Display the author name
                st.image(image)  # Display the generated image
                st.markdown(ai_story)  # Display the generated story
                
                # Show success message after the story is generated
                st.success("Your story has been generated successfully!", icon="✅")
