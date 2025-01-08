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
            .song-title {
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                margin-top: 5px;
            }
            .stImage > img {
                border-radius: 10px;
                object-fit: cover;
                width: 150px;
                height: 150px;
            }
            .stAudio {
                margin-top: 5px;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    persona_name = "vvv"
    st.markdown(f"<h1 style='text-align: center;'>Choose the Top 3 Songs that {persona_name} would love 🎵</h1>", unsafe_allow_html=True)

    # יצירת מולטי־סלקט לבחירת 3 שירים
    selected_songs = st.multiselect(
        "Select up to 3 songs:",
        songs_data["song"].tolist(),
        max_selections=3
    )

    # הצגת השירים ב-3 עמודות
    cols_per_row = 3
    cols = st.columns(cols_per_row)
    for i, row in songs_data.iterrows():
        col = cols[i % cols_per_row]  # מחזיר טור מתאים
        with col:
            song_name = row["song"]
            image_path = os.path.join(images_folder, f"{song_name}.jpg")
            audio_path = os.path.join(audio_folder, f"{song_name}.mp3")

            # הצגת תמונה, שם שיר, ואודיו
            st.image(image_path, caption=None, use_container_width=False)
            st.markdown(f"<div class='song-title'>{song_name}</div>", unsafe_allow_html=True)
            st.audio(audio_path, format="audio/mp3")

    # כפתור לאישור הבחירה
    if st.button("Confirm", key="confirm_button"):
        if len(selected_songs) != 3:
            st.error("You must select exactly 3 songs before continuing.")
        else:
            st.success(f"You have selected the following songs: {', '.join(selected_songs)}")

# קריאה לפונקציה
top_k_choose_page()
