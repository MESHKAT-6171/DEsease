import streamlit as st
from login import show_login_page
from signup import show_signup_page
from forgotpass import show_forgot_password_page
from home import show_home_page

def main():
    
    if "page" not in st.session_state:
        st.session_state.page = "login"

    
    if st.session_state.page == "login":
        show_login_page()
    elif st.session_state.page == "signup":
        show_signup_page()
    elif st.session_state.page == "forgot_password":
        show_forgot_password_page()
    elif st.session_state.page == "home":
        show_home_page()





if __name__ == "__main__":
    main()