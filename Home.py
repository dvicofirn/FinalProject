import streamlit as st
from PIL import Image

# Home page function
def home_page():
    # Main title
    st.markdown(
        "<h1 style='text-align: center; color: blue; font-size: 30px;'>Welcome to the Demo<br>on Rank-Based Approaches<br>to Recommender Systems!</h1>",
        unsafe_allow_html=True,
    )
    
    try:
        image_path = "Music.jpeg"  # Replace with your image file name
        st.image(image_path, caption="Music Note!", use_container_width=True)
    except FileNotFoundError:
        st.error("Could not load the album cover image. Please check the file path.")

    # Text for name input
    st.markdown(
        "<h3 style='text-align: center; color: blue;'>Please enter your name to begin.</h3>",
        unsafe_allow_html=True,
    )

    # Name input field
    name = st.text_input("", placeholder="Enter your name here")

    # Action based on name input
    if st.button("Enter"):
        if name != None:
            st.success(f"Welcome, {name}!")



    # Divider line
    st.divider()

    # Layout with columns for alignment
    col1, col2 = st.columns([9, 1])  # Adjust proportions as needed
    with col2:
        if st.button("Next"):
            st.session_state.page = "Intro"
            st.rerun()

# Set default page to Home
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page navigation logic
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Intro":
    from Intro import Intro_page
    Intro_page()  # Loading the Intro page
elif st.session_state.page == "Song_1":
    from Song_1 import Song_1_page
    Song_1_page()
elif st.session_state.page == "Song_2":
    from Song_2 import Song_2_page
    Song_2_page()
elif st.session_state.page == "Song_3":
    from Song_3 import Song_3_page
    Song_3_page()
elif st.session_state.page == "Song_4":
    from Song_4 import Song_4_page
    Song_4_page()
elif st.session_state.page == "persona_choose":
    from persona_choose import persona_choose_page
    persona_choose_page()
elif st.session_state.page == "songs_persona_like":
    from songs_persona_like import songs_persona_like_page
    songs_persona_like_page()
