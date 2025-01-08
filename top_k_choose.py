import streamlit as st
import pandas as pd
import os

def top_k_choose_page():
    images_folder = "‏‏top_k_songs_images"
    audio_folder = "top_k_songs_audio"

    csv_file_path = "top_k_songs.csv"
    songs_data = pd.read_csv(csv_file_path)

    st.set_page_config(page_title="Select Your Songs", layout="wide")

    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
                color: #333333;
            }
            .song-card {
                background: #ffffff;
                border-radius: 20px;
                padding: 15px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s;
                margin: 10px;
            }
            .song-card:hover {
                transform: scale(1.05);
            }
            .song-title {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            .stAudio {
                margin-top: 10px;
            }
            img {
                border-radius: 15px;
                height: 120px;
                width: 120px;
                object-fit: cover;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    persona_name = st.session_state.persona
    st.markdown(f"<h1 style='text-align: center;'>Choose the Top 3 Songs that {persona_name} would love 🎵</h1>", unsafe_allow_html=True)

    selected_songs = st.multiselect(
        "",
        songs_data["song"].tolist(),
        max_selections=3
    )

    # יצירת גריד להצגת השירים
    cols = st.columns(3)  # יצירת 3 עמודות עבור כל שורה
    for i, row in songs_data.iterrows():
        song_name = row["song"]
        image_path = os.path.join(images_folder, f"{song_name}.jpg")
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

        with cols[i % 3]:  # סבב בין העמודות
            with st.container():
                st.image(image_path, caption=song_name, use_container_width=True)
                st.audio(audio_path, format="audio/mp3")
                st.markdown("<br>", unsafe_allow_html=True)

    # כפתור האישור
    if st.button("Confirm", key="confirm_button"):
        if len(selected_songs) != 3:
            st.error("You must select exactly 3 songs before continuing.")
        else:
            st.success(f"You have selected the following songs: {', '.join(selected_songs)}")

    st.markdown(
        """
        <style>
            .stButton > button {
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
