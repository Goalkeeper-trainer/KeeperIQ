import streamlit as st
import google.generativeai as genai

# --- 1. SETUP & KI MODELL ---
# Wir definieren das Modell ganz am Anfang, damit der Fehler verschwindet
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # Hier definieren wir das 'model' - das ist das Herzstück!
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup-Fehler: {e}")

# --- 2. DESIGN & NAVIGATION ---
st.set_page_config(page_title="KeeperIQ", page_icon="🧤")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Gehe zu:", ["Training", "Über KeeperIQ", "PRO Upgrade 💎"])

if page == "Training":
    st.title("🧤 KeeperIQ – Dein Profi-Coach")
    version = st.sidebar.radio("Mitgliedschaft:", ["Standard (Kostenlos)", "PRO (Premium 💎)"])
    
    st.info("💡 Tipp: Nutze PRO für 3x schnellere Entwicklung.")

    # Eingabefelder
    name = st.text_input("Wie heißt du?")
    alter = st.number_input("Dein Alter", min_value=5, max_value=50, value=21)
    fokus = st.selectbox("Heutiger Schwerpunkt:", ["Reaktion", "Flanken", "1 gegen 1", "Stellungsspiel", "Abschlag"])

    # PRO-Logik
    if version == "PRO (Premium 💎)":
        fitness = st.select_slider("Energie-Level:", options=["Erschöpft", "Normal", "Topfit"])
        untergrund = st.selectbox("Untergrund:", ["Rasen", "Kunstrasen", "Halle"])
        prompt_text = f"Erstelle einen ELITE Plan für {name} ({alter}J). Fokus: {fokus}, Energie: {fitness}, Boden: {untergrund}."
    else:
        prompt_text = f"Erstelle einen einfachen Torwart-Plan für {name} ({alter}J). Fokus: {fokus}."

    # BUTTON ZUM STARTEN
    if st.button("Trainingsplan erstellen 🔥"):
        if name:
            with st.spinner('Coach erstellt den Plan...'):
                try:
                    # HIER wird das 'model' benutzt:
                    response = model.generate_content(prompt_text)
                    st.success("Plan fertig!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Fehler bei der Erstellung: {e}")
        else:
            st.warning("Bitte Namen eingeben!")

elif page == "Über KeeperIQ":
    st.title("Über KeeperIQ 🚀")
    st.write("Entwickelt von Tyler für die Torhüter der Zukunft.")

elif page == "PRO Upgrade 💎":
    st.title("PRO Upgrade 💎")
    st.write("Schalte alle Profi-Features frei! Melde dich bei Tyler.")
        
