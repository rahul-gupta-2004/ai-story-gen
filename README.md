# Story Forge AI

**Transforming Ideas into Enchanting Tales!**

[View Live Demo](https://story-forge-ai.streamlit.app/)

## Introduction

**Background Information:**
Story Forge AI aims to revolutionize storytelling by using AI to generate unique narratives based on user inputs.

**Problem Being Addressed:**
Many aspiring writers face writer's block or lack inspiration. This project provides a solution by automating story generation and offering a seamless, creative experience.

**Target Audience:**
This platform is designed for writers, educators, students, and creative individuals looking for inspiration or a fun storytelling experience.

**Project Goals:**
To create an interactive platform where users can generate, customize, and visualize stories effortlessly.

## Objectives

1. **User Interface Development:** Create an intuitive Streamlit interface that allows users to easily interact with the story generation features.
2. **Random Story Generation:** Implement functionality to generate random user-input stories from a database using the `fetch_data` module.
3. **AI Story Generation:** Utilize the Google Gemini API to generate AI-assisted stories based on predefined prompts, allowing for creativity without user input.
4. **Image Generation Integration:** Integrate image generation capabilities using the `gen_ai_model` module to provide visual representations of the generated stories.
5. **User Interaction:**
   Enable users to read and visualize both user-generated and AI-generated stories, enhancing their overall experience with the platform.

## Technologies Used

### Programming Languages

- **Python:** Chosen for backend logic, integration of AI models, and development of the web application.

### Frameworks

- **Streamlit:** Selected for rapid web app development with minimal setup, allowing for an interactive user experience.

### Tools

- **Airtable:** Used for storing and managing user-generated stories, providing a user-friendly database solution.
- **Google Gemini API:** Utilized for generating AI-driven story content, enhancing creativity in storytelling.
- **Hugging Face API:** Employed for image generation capabilities to visualize the stories effectively.

## Setup and Installation

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up a `.env` file in the project's root directory. The `.env` file is meant to securely hold your sensitive keys and is excluded from source control via `.gitignore`. 

   Make sure to include the proper API keys in the `.env` file as shown below:
   ```env
   GEMINI_API_KEY="your_actual_gemini_api_key_here"
   HUGGINGFACE_API_KEY="your_actual_huggingface_api_key_here"
   AIRTABLE_BASE_ID="your_actual_airtable_base_id_here"
   AIRTABLE_TABLE_ID="your_actual_airtable_table_id_here"
   AIRTABLE_PERSONAL_ACCESS_TOKEN="your_actual_personal_access_token_here"
   ```
   
   *Note: The codebase uses `python-dotenv` to load these keys securely into `os.getenv()`. Ensure your keys are correct.*

## Features

- **Story Customization:** Users can input characters, settings, and themes to shape the story as desired.
- **Interactive Prompts:** Guided questions help users refine the story's elements.
- **Random Story Generation:** One-click option for generating random stories based on predefined prompts.
- **Genre Selection:** Users can choose from various genres like adventure, sci-fi, fantasy, and more.
- **AI-Generated Images:** Visual representation of stories through AI-generated images to complement the text.
- **Download/Share Options:** Users can download their stories as PDFs or share them on social media.

## Project Outcomes

- **Successfully created an engaging platform:**
  Users can generate and visualize stories using AI, enhancing creativity and overcoming writer’s block.

## Reflections

- The project provided insights into user engagement and the potential of AI in creative writing. The combination of text and visual storytelling adds a unique layer of interactivity.

## Future Work

- Explore additional features like voice narration, collaborative storytelling, and advanced customization options based on user feedback and needs.

## References

- [Google Cloud - Gemini API Documentation](https://aistudio.google.com/app/)
- [Hugging Face - Stable Diffusion API](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Airtable](https://airtable.com/)
- [Python](https://www.python.org/)

