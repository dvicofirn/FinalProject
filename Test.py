import streamlit as st
from PIL import Image

def test_page():
    # Main title
    st.markdown(
        "<h1 style='text-align: center; color: blue;'>Welcome to the Demo<br>on Rank-Based Approaches<br>to Recommender Systems!</h1>",
        unsafe_allow_html=True,
    )

    # Loading an image from the computer
    try:
        image = Image.open("Music.jpeg")  # Replace with your file name or path
        st.image(image, caption="Music Note", use_container_width=True)
    except FileNotFoundError:
        st.error("Could not find the image. Please check the file path and name.")

    # Text for name input
    st.markdown(
        "<h3 style='text-align: center; color: blue;'>Please enter your name to begin.</h3>",
        unsafe_allow_html=True,
    )

    # Name input field
    name = st.text_input("", placeholder="Enter your name here")

    # Action based on name input
    if st.button("Start"):
        st.success(f"Welcome, {name}!")

    # Buttons for navigating to other pages
    st.divider()  # Divider line
    if st.button("Go to Home"):
        st.session_state.page = "Home"

    if st.button("Go to Test2"):
        st.session_state.page = "Test2"
