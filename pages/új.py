import sqlite3
import streamlit as st

# Function to connect to the existing database
def connect_to_database():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect("allat_menhely.db")
        st.success("Database connection successful")
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Call the function to connect to the database
conn = connect_to_database()

# Define the main function
def main():
    st.title("Streamlit Forms & Animal Shelter")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        # Display the form to add new entries
        with st.form(key='forml'):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            csipszam = st.text_input("Csipszám")
            ivar = st.selectbox("Ivar", ["Male", "Female"])
            if ivar == "Female":
                fajta = st.text_input("Fajta")
            else:
                fajta = st.text_input("Fajta vagy keverék típus")
            egeszsegi_allapot = st.text_input("Egészségi állapot")
            fogazat = st.text_input("Fogazat")
            kor = st.number_input("Kor", min_value=0, max_value=100)
            viselkedes = st.text_area("Viselkedés")
            egyeb_jellemzok = st.text_area("Egyéb jellemzők")

            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                if conn:
                    try:
                        c = conn.cursor()
                        c.execute("INSERT INTO allatok (firstname, lastname, csipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                  (firstname, lastname, csipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok))
                        conn.commit()
                        st.success("Data successfully added to the database")
                    except sqlite3.Error as e:
                        st.error(f"Error adding data to the database: {e}")
                else:
                    st.error("Database connection failed. Cannot add data.")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
