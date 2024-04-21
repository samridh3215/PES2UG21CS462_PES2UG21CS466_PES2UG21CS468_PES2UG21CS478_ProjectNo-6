import streamlit as st
import subprocess
import os
import time
import requests
from utils import get_service_port
# Define functions for sign-up and sign-in
def sign_up():
    st.title("Sign Up")
    # Add sign-up form fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        # Validate sign-up form
        if password != confirm_password:
            st.error("Passwords do not match.")
        else:
            # You can add code here to process the sign-up
            port = get_service_port('auth')
            userData = {}
            userData['email'] = username
            userData['password'] = password
            res = requests.post(url=f"http://{os.environ.get('MINIKUBE_IP')}:{port}/register/", json=userData)
            st.success(f"{res.text}")

def sign_in():
    st.title("Sign In")
    # Add sign-in form fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        # You can add code here to validate the sign-in credentials
        # For simplicity, let's just print the username and password
        port = get_service_port('auth')
        userData = {}
        userData['email'] = username
        userData['password'] = password
        res = requests.post(url=f"http://{os.environ.get('MINIKUBE_IP')}:{port}/login/", json=userData)
        if res.status_code == 200 and res.text == "SignedIN":
            st.success(f"{res.text}")
            time.sleep(2)
            st.switch_page(page="pages/order.py")
            
        else:
            st.error(f"{res.text}")
# Create the main navigation
def main():


    selection = st.radio("Go to", ["Sign Up", "Sign In"], key="navigation", horizontal=True)

    if selection == "Sign Up":
        sign_up()
    elif selection == "Sign In":
        sign_in()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    main()
