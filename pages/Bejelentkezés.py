import streamlit as st
import sqlite3
import pandas as pd

# Function to authenticate user
def authenticate(username, password, tier):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM credentials WHERE username=? AND password=? AND tier=?', (username, password, tier))
    result = c.fetchone()
    conn.close()
    return result

# Create table to store credentials if not exists
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS credentials
                 (username TEXT PRIMARY KEY, password TEXT, tier TEXT)''')
    conn.commit()
    conn.close()

# Function to add user credentials
def add_user(username, password, tier):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO credentials (username, password, tier) VALUES (?, ?, ?)', (username, password, tier))
    conn.commit()
    conn.close()

# Main function for Landing Page
def landing_page():
    st.title("Welcome to our Application")
    st.write("Please select an option:")
    if st.button("Login", key="login_button"):
        login_page()
    if st.button("Register", key="register_button"):
        register_page()

# Login Page
def login_page():
    st.title("Login Page")
    # Check if table exists, if not create it
    create_table()
    # Login Form
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    tier_options = ['User', 'Worker', 'Developer']
    tier_key = st.empty().key
    tier = st.selectbox("Select Tier", tier_options, key=tier_key)

    if st.button("Login", key="login_submit_button"):
        if username and password:
            result = authenticate(username, password, tier.lower())
            if result:
                st.success("Logged In as {} in {} tier".format(username, tier))
            else:
                st.error("Invalid Username, Password, or Tier")
        else:
            st.warning("Please provide both username, password, and select tier")

# Registration Page
def register_page():
    st.title("Register Page")
    # Check if table exists, if not create it
    create_table()
    # Register Form
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    new_tier_key = st.empty().key
    new_tier = st.selectbox("Select Tier", ['User', 'Worker', 'Developer'], key=new_tier_key)

    if st.button("Register", key="register_submit_button"):
        if new_username and new_password and new_tier:
            add_user(new_username, new_password, new_tier.lower())
            st.success("Registered Successfully!")
        else:
            st.warning("Please provide username, password, and select tier for registration")

# Main function
def main():
    landing_page()

if __name__ == '__main__':
    main()
