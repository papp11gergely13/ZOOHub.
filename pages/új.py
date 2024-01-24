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
                # Process the form data or perform any other desired actions
                st.write(f"First Name: {firstname}")
                st.write(f"Last Name: {lastname}")
                st.write(f"Csipszám: {csipszam}")
                st.write(f"Ivar: {ivar}")
                st.write(f"Fajta vagy keverék típus: {fajta}")
                st.write(f"Egészségi állapot: {egeszsegi_allapot}")
                st.write(f"Fogazat: {fogazat}")
                st.write(f"Kor: {kor}")
                st.write(f"Viselkedés: {viselkedes}")
                st.write(f"Egyéb jellemzők: {egyeb_jellemzok}")

    else:
        st.subheader("About")

main()

#csipszám, ivar, ha egyértelmű, fajta, vagy fajtajellemzőkkel keverék tipus, egészségi állapot, fogazat, kor, viselkedés, egyéb jellemzők