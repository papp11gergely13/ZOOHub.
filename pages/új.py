import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Állat menhely",
    page_icon='🍆',
)

def main():
    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        with st.form(key='forml'):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("lastname")
            dob = st.date_input("Date of Birth")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Process the form data or perform any other desired actions
                st.write(f"First Name: {firstname}")
                st.write(f"Last Name: {lastname}")
                st.write(f"Date of Birth: {dob}")

    else:
        st.subheader("About")

main()

