import streamlit as st
import pandas as pd


def get_songs_by_persona(persona_name):
    df = pd.read_csv('personas_songs.csv')
    songs = df[df['persona'] == persona_name]['song'].tolist()
    return songs

def songs_persona_like_page():

    songs_list = get_songs_by_persona(st.session_state.persona)

    if "song_index" not in st.session_state:
        st.session_state.song_index = 0

    if st.session_state.song_index >= len(songs_list):
        st.session_state.page = "top_k_choose"
        st.rerun()

    song_title = songs_list[st.session_state.song_index]

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

    st.markdown(
        f"""
        <div class="container">
            <div class="song-title">Now Playing: {song_title}!!!</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    try:
        image_path = f"‏‏personas_songs_images/{song_title}.jpg"
        st.image(image_path, caption="Album Cover", use_container_width=True)
    except FileNotFoundError:
        st.error(f"Could not load the album cover image for {song_title}. Please check the file path.")

    try:
        audio_path = f"personas_songs_audio/{song_title}.mp3"
        audio_file = open(audio_path, "rb").read()
        st.audio(audio_file, format="audio/aac")
    except FileNotFoundError:
        st.error(f"Could not load the audio file for {song_title}. Please check the file path.")

    col1, col2, col3 = st.columns([1, 3, 1])  # Adjust proportions for alignment
    with col1:
        if st.button("👍", key=f"like_song_{st.session_state.song_index}"):
            st.success("You liked this song!")

    with col3:
        if st.button("👎", key=f"dislike_song_{st.session_state.song_index}"):
            st.warning("You disliked this song!")

    col_next = st.columns([1, 3])  # Adjust proportions for alignment
    with col_next[1]:  # Aligning to the right
        if st.button("Next Song", key=f"next_song_{st.session_state.song_index}"):
            st.session_state.song_index += 1
            st.rerun()



