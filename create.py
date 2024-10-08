# Import necessary libraries and modules
import streamlit as st
import gen_ai_model  # Module to generate AI responses and images
import save_data  # Module to handle saving story data to the database
import display_timestamp  # Module to display and fetch timestamps

# Define the app function to create a new story
def app():
    st.title("Start Your Tale")  # Page title

    # Input fields for the story creation
    story_plot = st.text_area("Story Plot (required)", placeholder="E.g.: A librarian discovers a magical book that can bring stories to life.")
    author = st.text_input("Author (optional)", placeholder="Enter your name", value="Anonymous")
    creativity = st.select_slider("Creativity Level (1 being Realistic and 10 being Imaginary)", options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], value="5")
    narrative_style = st.selectbox("Narrative (optional)", options=["AI Choice", "First Person", "Second Person", "Third Person Limited", "Omniscient", "Epistolary", "Stream of Consciousness"])
    genre = st.multiselect("Genre (optional)", options=["Fantasy", "Mystery", "Romance", "Sci-Fi", "Adventure", "Thriller", "Non-Fiction"], max_selections=3, placeholder="AI Choice")
    tone = st.multiselect("Tone (optional)", options=["Formal", "Informal", "Humorous", "Serious", "Optimistic", "Pessimistic", "Joyful", "Melancholic", "Conversational"], max_selections=4, placeholder="AI Choice")
    mood = st.multiselect("Mood (optional)", options=["Angry", "Calm", "Excited", "Hopeful", "Melancholic", "Mysterious", "Surprised", "Tense", "Nostalgic"], max_selections=4, placeholder="AI Choice")
    main_char = st.text_input("Main Character (required)", placeholder="E.g.: John Doe")
    main_char_desc = st.text_area("Character Description (required)", placeholder="E.g.: Jane Doe is a timid 30-year-old librarian who has a pet lizard.")
    setting_desc = st.text_area("Setting Description (optional)", placeholder="E.g.: A library with a magical book that can bring stories to life.")
    conflict = st.text_input("Conflict (optional)", placeholder="E.g.: The library is attacked by a group of wizards.")
    language = st.selectbox("Language (optional)", options=["English", "Spanish", "French", "German", "Chinese (Simplified)", "Chinese (Traditional)", "Japanese", "Russian", "Arabic", "Hindi",  "Italian", "Korean", "Portuguese"])
    vocab = st.radio("Vocabulary (optional)", options=["Kindergarten (1-5 years old)", "Elementary (6-11 years old)", "High School (12-18 years old)", "College (18+ years old)"])

    submit = st.button("Submit")  # Button to submit the form

    # When the form is submitted
    if submit:
        # Check if all required fields are filled
        if not story_plot or not main_char or not main_char_desc:
            st.error("Please fill in all **required** fields", icon="⚠️")
        else:
            # Generate the story based on user inputs
            with st.spinner("Generating your story..."):
                # Create the prompt for the AI model
                prompt = f"Generate a medium-length story of 3 paragraphs based on the following plot: {story_plot}. "
                prompt += f"The story should have a creativity level of {creativity} from 1 to 10. "

                if narrative_style == "AI Choice":
                    prompt += "Choose a random narrative style from First Person, Second Person, Third Person Limited, Omniscient, Epistolary, and Stream of Consciousness. "
                else:
                    prompt += f"The narrative style should be {narrative_style}. "

                if len(genre) == 0:
                    prompt += "Choose a random genre from Fantasy, Mystery, Romance, Sci-Fi, Adventure, Thriller, and Non-Fiction. "
                else:
                    prompt += f"The genres should be {', '.join(genre)}. "

                if len(tone) == 0:
                    prompt += "Choose a random tone from Formal, Informal, Humorous, Serious, Optimistic, Pessimistic, Joyful, Melancholic, and Conversational. "
                else:
                    prompt += f"The tone should be {', '.join(tone)}. "

                if len(mood) == 0:
                    prompt += "Choose a random mood from Angry, Calm, Excited, Hopeful, Melancholic, Mysterious, Surprised, Tense, and Nostalgic. "
                else:
                    prompt += f"The mood should be {', '.join(mood)}. "

                prompt += f"The main character is {main_char}, and their description is: {main_char_desc}. "
                if setting_desc:
                    prompt += f"The setting is: {setting_desc}. "
                if conflict:
                    prompt += f"The conflict in the story is: {conflict}. "

                prompt += f"The story should be written in {language} using {vocab} vocabulary. Focus on the main character and the plot, without adding any additional characters."

                # Get the AI-generated story
                ai_story = gen_ai_model.get_gemini_response(prompt)

                # Generate the image for the story
                image_prompt = f"Generate an image for the story: {ai_story}. Don't generate a list of story titles. I want only 1 story title of 3 to 4 words."
                image = gen_ai_model.generate_image(image_prompt)

                # Generate a title for the story
                story_title_prompt = f"Generate a title for the story: {ai_story}."
                story_title = gen_ai_model.get_gemini_response(story_title_prompt).strip()

                # Display the generated story
                st.header(story_title.title())
                st.subheader(f"By {author.title()}")
                st.image(image)
                st.markdown(ai_story)

            # Save the story details to the database
            with st.spinner("Saving your story..."):
                timestamp = display_timestamp.fetch_timestamp()  # Get the current timestamp

                # Save the data using the save_to_airtable function
                status_code, response_content = save_data.save_to_airtable(
                    timestamp=timestamp, title=story_title, author=author, image_prompt=image_prompt, story=ai_story)

                # Check if the story was saved successfully
                if status_code == 200:
                    st.success("Your story has been saved to the database!", icon="✅")
                else:
                    st.error("Something went wrong. Please try again later.", icon="🚨")

# Run the app if this file is executed directly
if __name__ == "__main__":
    app()
