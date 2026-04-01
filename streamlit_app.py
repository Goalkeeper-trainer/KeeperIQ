import streamlit as st
import google.generativeai as genai

# 1. Verbindung zum Tresor herstellen
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("API Key Fehler: Bitte check deine Secrets in Streamlit!")

# 2. Das Design von KeeperIQ
st.set_page_config(page_title="KeeperIQ", page_icon="🧤")
st.title("🧤 KeeperIQ – Dein Profi-Coach")
st.write("Erhalte maßgeschneiderte Trainingspläne von deiner KI.")
st.markdown("---")

# 3. Die Eingabefelder für den User
name = st.text_input("Wie heißt du?")
alter = st.number_input("Dein Alter", min_value=5, max_value=50, value=18)
fokus = st.selectbox("Woran willst du heute arbeiten?", 
                     ["Reaktion", "Flanken", "1 gegen 1", "Strafraumbeherrschung", "Abschlag", "Stellungsspiel"])

# 4. Der Button, der die KI startet
if st.button("Erstelle meinen Plan 🔥"):
    if name:
        with st.spinner('Dein Coach analysiert deine Schwächen...'):
            try:
                prompt = f"Du bist ein erfahrener Torwart-Trainer. Erstelle einen motivierenden, professionellen Trainingsplan für {name}, {alter} Jahre alt. Fokus der Einheit: {fokus}. Gib 3 konkrete Übungen mit Wiederholungen an."
                response = model.generate_content(prompt)
                st.success(f"Hier ist dein Plan, {name}!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Ein Fehler ist aufgetreten: {e}")
    else:
        st.warning("Bitte gib erst deinen Namen ein!")
      
