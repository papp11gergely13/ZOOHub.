import streamlit as st
import sqlite3
import pandas as pd

def main():
    st.title("Streamlit SQLite Example")

    # Connect to SQLite database
    conn = sqlite3.connect("example.db")
    c = conn.cursor()

    # Create the table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS my_table
                 (ID INTEGER PRIMARY KEY,
                  Name TEXT,
                  Age INTEGER)''')

    # Execute a query to fetch data from the table
    c.execute("SELECT * FROM my_table")
    data = c.fetchall()

    # Close the database connection
    conn.close()

    # Convert the fetched data to a DataFrame
    df = pd.DataFrame(data, columns=["ID", "Name", "Age"])

    # Display the DataFrame
    st.write(df)

    # Allow user to modify data if there are rows in the DataFrame
    if not df.empty:
        selected_id = st.number_input("Enter ID of the row to modify:", min_value=1, max_value=df.shape[0])
        if st.button("Modify Row"):
            new_name = st.text_input("Enter new name:")
            new_age = st.number_input("Enter new age:")

            # Connect to SQLite database
            conn = sqlite3.connect("example.db")
            c = conn.cursor()

            # Execute a query to update the selected row
            c.execute("UPDATE my_table SET Name=?, Age=? WHERE ID=?", (new_name, new_age, selected_id))

            # Commit changes and close the database connection
            conn.commit()
            conn.close()
            st.success("Row modified successfully!")
    else:
        st.write("No data to modify.")

if __name__ == "__main__":
    main()
