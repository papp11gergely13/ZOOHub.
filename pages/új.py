import streamlit as st
import sqlite3
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(
    page_title="Állat menhely",
    page_icon='🍆',
)

# Function to create the database if it doesn't exist
def create_database():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect("example.db")
        c = conn.cursor()

        # Create the table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS example (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            csipszam TEXT,
            ivar TEXT,
            fajta TEXT,
            egeszsegi_allapot TEXT,
            fogazat TEXT,
            kor INTEGER,
            viselkedes TEXT,
            egyeb_jellemzok TEXT
        )''')

        # Commit changes and close connection
        conn.commit()
        conn.close()

        st.success("Database successfully created or connected to")
    except sqlite3.Error as e:
        st.error(f"Error creating or connecting to database: {e}")

# Call the function to create or connect to the database
create_database()

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
                try:
                    # Store data in SQLite database
                    conn = sqlite3.connect("example.db")
                    c = conn.cursor()

                    c.execute("INSERT INTO example (firstname, lastname, csipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                              (firstname, lastname, csipszam, ivar, fajta, egeszsegi_allapot, fogazat, kor, viselkedes, egyeb_jellemzok))

                    conn.commit()
                    conn.close()
                    st.success("Data successfully added to the database")
                except sqlite3.Error as e:
                    st.error(f"Error adding data to the database: {e}")

        # Display the list of entries with delete option
        st.subheader("Existing Entries")
        try:
            conn = sqlite3.connect("example.db")
            c = conn.cursor()
            c.execute("SELECT * FROM example")
            data = c.fetchall()
            conn.close()

            if data:
                df = pd.DataFrame(data, columns=['ID', 'Firstname', 'Lastname', 'Csipszám', 'Ivar', 'Fajta', 'Egészségi állapot', 'Fogazat', 'Kor', 'Viselkedés', 'Egyéb jellemzők'])
                st.write(df)

                # Add a delete button for each entry
                for index, row in df.iterrows():
                    if st.button(f"Delete entry {row['ID']}"):
                        try:
                            conn = sqlite3.connect("example.db")
                            c = conn.cursor()
                            c.execute("DELETE FROM example WHERE id=?", (row['ID'],))
                            conn.commit()
                            conn.close()
                            st.success(f"Entry {row['ID']} deleted successfully")
                        except sqlite3.Error as e:
                            st.error(f"Error deleting entry {row['ID']}: {e}")
            else:
                st.write("No entries found in the database")
        except sqlite3.Error as e:
            st.error(f"Error querying database: {e}")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
