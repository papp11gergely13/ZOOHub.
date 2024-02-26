import streamlit as st
import sqlite3
import pandas as pd

# Function to connect to the SQLite database
def connect_to_database():
    try:
        conn = sqlite3.connect("example.db")
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Define the main function
def main():
    st.title("Animal Shelter - Modify Data")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Modify Data")

        # Connect to SQLite database
        conn = connect_to_database()

        if conn:
            try:
                # Retrieve data from database
                c = conn.cursor()
                c.execute("SELECT * FROM allatok")
                data = c.fetchall()

                # Convert data to DataFrame
                df = pd.DataFrame(data, columns=["ID", "Firstname", "Lastname", "Csipszam", "Ivar", "Fajta", "Egeszsegi_allapot", "Fogazat", "Kor", "Viselkedes", "Egyeb_jellemzok"])

                # Display DataFrame
                st.dataframe(df)

                # Select row to modify
                selected_row = st.number_input("Select a row to modify:", min_value=1, max_value=len(df), value=1, step=1)

                # Modify data
                if st.button("Modify Data"):
                    new_firstname = st.text_input("New Firstname", df.loc[selected_row - 1, 'Firstname'])
                    new_lastname = st.text_input("New Lastname", df.loc[selected_row - 1, 'Lastname'])
                    # Add inputs for other columns here

                    # Update data in database
                    c.execute("UPDATE example SET Firstname=?, Lastname=? WHERE ID=?", (new_firstname, new_lastname, selected_row))
                    conn.commit()

                    st.success("Data successfully modified")

            except sqlite3.Error as e:
                st.error(f"Error querying database: {e}")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
