import streamlit as st

def Song_1_page():
    """
    Song 1 page: Plays a song, displays a small image, shows the song title,
    and provides buttons with emojis for user interaction.
    """
    # Styling for the page
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
            max-width: 400px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .song-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .song-image {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .stButton button {
            font-size: 16px;
            padding: 10px 40px; /* Adjust padding for better emoji display */
            border-radius: 8px;
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Song title
    st.markdown(
        """
        <div class="container">
            <div class="song-title">Now Playing: Smells Like Teen Spirit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centering the song image
    try:
        image_path = "song1_image.jpeg"  # Replace with your image file name
        st.image(image_path, caption="Album Cover", use_container_width=True)
    except FileNotFoundError:
        st.error("Could not load the album cover image. Please check the file path.")

    # Song audio
    st.audio("song1_audio.mp3", format="audio/mp3")  # Replace with your song file name

    # Feedback buttons with emojis
    col1, col2, col3 = st.columns([1, 3, 1])  # Adjust proportions for alignment
    with col1:
        if st.button("👍", key="like_song_1"):
            st.success("You liked this song!")
    with col3:
        if st.button("👎", key="dislike_song_1"):
            st.warning("You disliked this song!")

    # Navigation to the next song
    col_next = st.columns([1, 3])  # Adjust proportions for alignment
    with col_next[1]:  # Aligning to the right
        if st.button("Next Song", key="next_song_2"):
            st.session_state.page = "Song_2"
