import streamlit as st
import random

def persona_choose_page():
    people = [
        {
            "name": "John",
            "image": "persona_A.jpg",
        },
        {
            "name": "Bob",
            "image": "persona_B.jpg",
        },
        {
            "name": "Alice",
            "image": "persona_C.jpg",
        },
    ]

    chosen_person = random.choice(people)
    if "persona" not in st.session_state:
        st.session_state.persona = chosen_person["name"]

    st.markdown(
        """
        <style>
        .container {
            background-color: #f0f0f5;
            border-radius: 50px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-family: Arial, sans-serif;
            width: 600px; /* קובע את הרוחב הקבוע */
            margin: 0 auto; /* ממרכז את הקונטיינר */
        }

        .title {
            font-size: 32px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }
        .description {
            font-size: 18px;
            color: #555;
            margin-bottom: 20px;
        }
        img {
        border-radius: 15px;
        width: 10px; /* קובע רוחב קבוע */
        height: 800px; /* קובע גובה קבוע */
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
            <div class="container">
                <div class="title">Meet {chosen_person['name']}!</div>
            </div>
            """,
        unsafe_allow_html=True,
    )

    

    st.markdown(
        f"""
            <div class="container">
                <div class="description">
                    You're seated next to this persona on your flight. Based on the song ratings you've given, it seems like you and this persona could be great friends! To get to know them better, here are some songs they love.
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    col_next = st.columns([1, 3])  # Adjust proportions for alignment
    with col_next[1]:  # Aligning to the right
        if st.button("Next", key="songs_persona_like"):
            st.session_state.page = "songs_persona_like"
            st.rerun()

