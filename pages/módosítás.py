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
        selected_row = st.radio("Select a row to modify:", df['ID'].tolist())

        # A kiválasztott sor megjelenítése
        selected_data = df[df['ID'] == selected_row]
        st.dataframe(selected_data)

        if st.button("Modify Data"):
            # Módosítás logikája
            new_firstname = st.text_input("New Firstname", selected_data['Firstname'].iloc[0])
            new_lastname = st.text_input("New Lastname", selected_data['Lastname'].iloc[0])
            # ... Az összes többi módosítandó adatot itt adja meg

            # Adatok módosítása az SQLite adatbázisban
            conn = sqlite3.connect("allat_menhely.db")
            c = conn.cursor()

            c.execute("UPDATE allatok SET firstname=?, lastname=?, csipszam=?, ivar=?, fajta=?, egeszsegi_allapot=?, fogazat=?, kor=?, viselkedes=?, egyeb_jellemzok=? WHERE id=?",
                      (new_firstname, new_lastname, selected_data['Csipszam'].iloc[0], selected_data['Ivar'].iloc[0], selected_data['Fajta'].iloc[0], selected_data['Egeszsegi_allapot'].iloc[0], selected_data['Fogazat'].iloc[0], selected_data['Kor'].iloc[0], selected_data['Viselkedes'].iloc[0], selected_data['Egyeb_jellemzok'].iloc[0], selected_row))

            conn.commit()
            conn.close()
            st.success("Adatok sikeresen módosítva")

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
