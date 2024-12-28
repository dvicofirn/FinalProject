import streamlit as st

# הגדרת עמוד ברירת מחדל ב-Session State
if "page" not in st.session_state:
    st.session_state.page = "Home"  # עמוד ברירת מחדל

# ניווט בין עמודים
if st.session_state.page == "Home":
    st.title("Home")
    st.write("זהו העמוד הראשי שלך.")

    if st.button("מעבר לעמוד Test"):
        st.session_state.page = "Test"

    if st.button("מעבר לעמוד Test2"):
        st.session_state.page = "Test2"
elif st.session_state.page == "Test":
    from Test import test_page
    test_page()  # טעינת עמוד Test
elif st.session_state.page == "Test2":
    from Test2 import test2_page
    test2_page()  # טעינת עמוד Test2
