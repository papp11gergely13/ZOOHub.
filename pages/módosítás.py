import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Állat menhely",
    page_icon='🍆',
)

def main():
    st.title("Animal Shelter - Modify Data")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Modify Data")

        # Adatok lekérdezése az adatbázisból
        conn = sqlite3.connect("allat_menhely.db")
        c = conn.cursor()
        c.execute("SELECT * FROM allatok")
        data = c.fetchall()
        conn.close()

        # Adatok DataFrame konvertálása
        df = pd.DataFrame(data, columns=["ID", "Firstname", "Lastname", "Csipszam", "Ivar", "Fajta", "Egeszsegi_allapot", "Fogazat", "Kor", "Viselkedes", "Egyeb_jellemzok"])

        # Táblázat megjelenítése
        st.dataframe(df)

        selected_row = st.number_input("Select a row to modify:", min_value=1, max_value=len(df), value=1, step=1)

        # A kiválasztott sor megjelenítése
        selected_data = df.iloc[selected_row - 1]
        st.subheader("Selected Row:")
        st.write(selected_data)

        if st.button("Modify Data"):
            # Módosítás logikája
            new_firstname = st.text_input("New Firstname", selected_data['Firstname'])
            new_lastname = st.text_input("New Lastname", selected_data['Lastname'])
            # ... Az összes többi módosítandó adatot itt adja meg

            # Adatok módosítása a DataFrame-ben
            df.loc[selected_row - 1, 'Firstname'] = new_firstname
            df.loc[selected_row - 1, 'Lastname'] = new_lastname
            # ... Az összes többi módosítandó adatot itt adja meg

            # Adatok módosítása az SQLite adatbázisban
            conn = sqlite3.connect("allat_menhely.db")
            c = conn.cursor()

            c.execute("UPDATE allatok SET firstname=?, lastname=?, csipszam=?, ivar=?, fajta=?, egeszsegi_allapot=?, fogazat=?, kor=?, viselkedes=?, egyeb_jellemzok=? WHERE id=?",
                      (new_firstname, new_lastname, selected_data['Csipszam'], selected_data['Ivar'], selected_data['Fajta'], selected_data['Egeszsegi_allapot'], selected_data['Fogazat'], selected_data['Kor'], selected_data['Viselkedes'], selected_data['Egyeb_jellemzok'], selected_row))

            conn.commit()
            conn.close()

            # Táblázat frissítése
            st.dataframe(df)

            st.success("Adatok sikeresen módosítva")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
 



 