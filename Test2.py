import streamlit as st

def test2_page():
    st.title("Test2")
    st.write("ברוך הבא לעמוד Test2!")

    # הוספת תמונה אקראית
    st.image(
        "https://picsum.photos/800/600",
        caption="תמונה אקראית מאתר Picsum Photos",
        use_container_width=True,  # הפרמטר המעודכן
    )

    # כפתורי מעבר לעמודים אחרים
    if st.button("מעבר לעמוד Home"):
        st.session_state.page = "Home"

    if st.button("מעבר לעמוד Test"):
        st.session_state.page = "Test"
