import streamlit as st

def Intro_page():
    # Apply CSS styling for the mobile-like design and button
    st.markdown(
        """
        <style>
        .container {
            background-color: black;
            color: white;
            border-radius: 25px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 350px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .description {
            font-size: 16px;
            margin-bottom: 20px;
        }
        .spotify-logo {
            margin: 20px auto;
            width: 120px;
            height: 120px;
            background-color: #1DB954;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .spotify-logo img {
            width: 80px;
            height: 80px;
        }
        .footer {
            font-size: 14px;
            margin-top: 20px;
        }
        .wide-button {
            background-color: #1DB954;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
            width: 100%;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            text-align: center;
            margin-top: 20px;
        }
        .wide-button:hover {
            background-color: #17a743;
        }
        </style>
        <div class="container">
            <div class="header">Here’s a list of songs!</div>
            <div class="spotify-logo">
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg" alt="Spotify Logo">
            </div>
            <div class="description">Listen and select the emoji that best reflects your feelings about each song.</div>
            <div class="footer">You can skip, move on, or continue at any time.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Divider for separating the content from buttons
    st.divider()

    # Button for navigating to the next page
    col1, col2 = st.columns([9, 1])  # Adjust proportions as needed
    with col2:
        if st.button("Let's Start", key="next_song_1"):
            st.session_state.page = "Song_1"



