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
            }
            .song-card:hover {
                transform: scale(1.05);
            }
            .song-title {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            .song-audio {
                margin-top: 10px;
            }
            .multiselect-container {
                margin-bottom: 20px;
            }
            .confirm-button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 20px;
                cursor: pointer;
                font-size: 16px;
            }
            .confirm-button:hover {
                background-color: #45a049;
            }
            img {
                object-fit: cover;
                width: 300px;  /* קביעת רוחב 300 */
                height: 300px; /* קביעת גובה 300 */
                border-radius: 25px; /* רדיוס לתמונה */
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

    cols = st.columns(3)
    for i, row in songs_data.iterrows():
        song_name = row["song"]
        image_path = os.path.join(images_folder, f"{song_name}.jpg")  # נתיב לתמונה
        audio_path = os.path.join(audio_folder, f"{song_name}.mp3")  # נתיב לקובץ mp3

        col = cols[i % 3]  # טורים מתחלפים
        with col:
            with st.container():
                st.image(image_path, use_container_width=300)
                st.audio(audio_path, format="audio/acc")
                st.markdown("<br>", unsafe_allow_html=True)

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
