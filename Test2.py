import streamlit as st

def test2_page():
    st.title("Test2")
    st.write("Welcome to the Test2 page!")

    # Add a random image
    st.image(
        "https://picsum.photos/800/600",
        caption="Random image from Picsum Photos",
        use_container_width=True,  # Updated parameter
    )

    # Buttons for navigating to other pages
    if st.button("Go to Home"):
        st.session_state.page = "Home"

    if st.button("Go to Test"):
        st.session_state.page = "Test"
