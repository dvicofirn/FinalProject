import streamlit as st
from PIL import Image

def test_page():
    # כותרת ראשית
    st.markdown(
        "<h1 style='text-align: center; color: blue;'>Welcome to the Demo<br>on Rank-Based Approaches<br>to Recommender Systems!</h1>",
        unsafe_allow_html=True,
    )

    # טעינת תמונה מהמחשב
    try:
        image = Image.open("Music.jpeg")  # החלף בשם הקובץ או הנתיב לתמונה שלך
        st.image(image, caption="Music Note", use_container_width=True)
    except FileNotFoundError:
        st.error("Could not find the image. Please check the file path and name.")

    # טקסט להזנת שם
    st.markdown(
        "<h3 style='text-align: center; color: blue;'>Please enter your name to begin.</h3>",
        unsafe_allow_html=True,
    )

    # שדה קלט לשם
    name = st.text_input("", placeholder="Enter your name here")

    # פעולה על בסיס שם
    if st.button("Start"):
        st.success(f"Welcome, {name}!")

    # כפתורי מעבר לעמודים אחרים
    st.divider()  # קו הפרדה
    if st.button("Go to Home"):
        st.session_state.page = "Home"

    if st.button("Go to Test2"):
        st.session_state.page = "Test2"
