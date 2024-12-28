import streamlit as st

# Setting a default page in Session State
if "page" not in st.session_state:
    st.session_state.page = "Home"  # Default page

# Page navigation
if st.session_state.page == "Home":
    st.title("Home")
    st.write("This is your main page.")

    if st.button("Go to Test page"):
        st.session_state.page = "Test"

    if st.button("Go to Test2 page"):
        st.session_state.page = "Test2"
elif st.session_state.page == "Test":
    from Test import test_page
    test_page()  # Loading the Test page
elif st.session_state.page == "Test2":
    from Test2 import test2_page
    test2_page()  # Loading the Test2 page
