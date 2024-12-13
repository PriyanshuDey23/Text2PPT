import streamlit as st
from Text2PPT.helper import *
import time

# Streamlit app main function

# Streamlit UI setup
st.set_page_config(layout="wide")

# Set page title and icon
st.title("PowerPoint Presentation Generator")


# Create a sidebar for input fields
topic = st.text_input("Enter the topic for your presentation:")
language = st.text_input("Enter the Language for your presentation:")
tone = st.text_input("Enter the Tone for your presentation:")
number_of_slides = st.text_input("Enter the Number of Slides for your presentation:")

# Create a submit button
submit_button = st.button("Generate Presentation")

# Create a loading animation
def loading_animation():
    with st.spinner("Generating presentation... Please wait."):
        time.sleep(2)  # Simulate processing time

# Create a success animation
def success_animation():
    with st.snow():
        time.sleep(2)  # Simulate processing time

if submit_button:
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        loading_animation()
        with st.spinner("Generating presentation... Please wait."):

            # Generate slide titles and contents
            slide_titles = generate_slide_titles(topic, tone, language, number_of_slides)
            slide_contents = [generate_slide_content(title, tone, language) for title in slide_titles]

            if not slide_titles or not slide_contents:
                st.error("Failed to generate presentation. Please try again.")

            # Create and save the presentation
            presentation_path = create_presentation(topic, slide_titles, slide_contents)
            if presentation_path:
                success_animation()
                st.success("Presentation generated successfully!")
                st.markdown(get_ppt_download_link(presentation_path), unsafe_allow_html=True)
            else:
                st.error("Error occurred while saving the presentation.")





