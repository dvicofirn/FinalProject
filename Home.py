import streamlit as st
import base64


def set_background(image_file):
    """
    Set a background image for the Streamlit app using Base64 encoding.
    Parameters:
        image_file (str): The path to the image file.
    """
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
        page_background = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #FFFFFF;
        }}
        </style>
        """
        st.markdown(page_background, unsafe_allow_html=True)


# Home page function
def home_page():
    st.set_page_config(page_title="תמונות בשורה", layout="wide")  # עיצוב רחב לכל סוגי המכשירים
    set_background("Backround.jpeg")


        # הוספת CSS מותאם אישית
    st.markdown(
        """
        <style>
        /* עיצוב שורת התמונות */
        .image-row {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px; /* ריווח בין התמונות */
        }
        .image-row img {
            max-width: 30%; /* כל תמונה תהיה עד 30% מהרוחב הזמין */
            height: auto;
        }
        @media (max-width: 768px) {
            .image-row img {
                max-width: 30%; /* רוחב מותאם לטלפון */
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # יצירת שורה מותאמת אישית עם תמונות
    st.markdown('<div class="image-row">', unsafe_allow_html=True)
    
    # הוספת תמונות
    st.markdown('<img src="Music.png" alt="תמונה 1" />', unsafe_allow_html=True)
    st.markdown('<img src="Music.png" alt="תמונה 2" />', unsafe_allow_html=True)
    st.markdown('<img src="Music.png" alt="תמונה 3" />', unsafe_allow_html=True)
    
    # סגירת ה-DIV של השורה
    st.markdown('</div>', unsafe_allow_html=True)
    
    # הערה מתחת לתמונות
    st.markdown("התמונות נשארות בשורה אחת גם במחשב וגם בטלפון!")



    # Main title
    st.markdown(
        "<h1 style='text-align: center; color: blue; font-size: 30px;'>Welcome to the Demo<br>on Rank-Based Approaches<br>to Recommender Systems!</h1>",
        unsafe_allow_html=True,
    )

    # Replacing the music note icon with a transparent PNG file
    try:
        image_path = "Music.png"  # Replace with your transparent PNG file path
    except FileNotFoundError:
        st.error("Could not load the music note image. Please check the file path.")

    # Text for name input
    st.markdown(
        "<h3 style='text-align: center; color: blue;'>Please enter your name to begin.</h3>",
        unsafe_allow_html=True,
    )

    # Name input field
    name = st.text_input("", placeholder="Enter your name here")

    # Action based on name input
    if st.button("Enter"):
        if name:
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
elif st.session_state.page == "top_k_choose":
    from top_k_choose import top_k_choose_page
    top_k_choose_page()
