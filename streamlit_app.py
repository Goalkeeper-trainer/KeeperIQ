import streamlit as st
import google.generativeai as genai

# --- 1. API & MODELL SETUP ---
# Hier greifen wir auf den GOOGLE_API_KEY zu, den du gerade in den Secrets gespeichert hast
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        # Das Modell definieren (der Motor deiner App)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Fehler: GOOGLE_API_KEY wurde in den Secrets nicht gefunden!")
except Exception as e:
    st.error(f"Ein Fehler ist beim Starten aufgetreten: {e}")

# --- 2. APP DESIGN ---
st.set_page_config(page_title="KeeperIQ", page_icon="🧤")

# Navigation in der Seitenleiste
st.sidebar.title("KeeperIQ Menü")
page = st.sidebar.radio("Navigation:", ["Training", "Über KeeperIQ", "PRO Upgrade 💎"])

# --- SEITE: TRAINING ---
if page == "Training":
    st.title("🧤 KeeperIQ – Dein Profi-Coach")
    
    # Auswahl der Version
    version = st.sidebar.radio("Mitgliedschaft:", ["Standard (Kostenlos)", "PRO (Premium 💎)"])
    
    if version == "PRO (Premium 💎)":
        st.success("💎 PRO-MODUS AKTIVIERT: Maximale Präzision.")
    else:
        st.info("💡 Tipp: Upgrade auf PRO für individuelles Equipment-Training.")

    # Eingabemaske
    name = st.text_input("Wie heißt du?", placeholder="Dein Name")
    alter = st.number_input("Dein Alter", min_value=5, max_value=60, value=21)
    fokus = st.selectbox("Heutiger Schwerpunkt:", 
                         ["Reaktion", "Flanken", "1 gegen 1", "Strafraumbeherrschung", "Abschlag", "Stellungsspiel"])

    # Logik für PRO-Features
    if version == "PRO (Premium 💎)":
        col1, col2 = st.columns(2)
        with col1:
            fitness = st.select_slider("Energie-Level:", options=["Erschöpft", "Normal", "Topfit"])
        with col2:
            untergrund = st.selectbox("Untergrund:", ["Rasen", "Kunstrasen", "Halle", "Hartplatz"])
        prompt_text = (f"Du bist ein Weltklasse-Torwarttrainer. Erstelle einen Plan für {name} ({alter} Jahre). "
                       f"Fokus: {fokus}. Fitness-Level: {fitness}. Boden: {untergrund}. "
                       f"Erstelle Warm-up, 3 Hauptübungen und ein Cool-down. Sei motivierend!")
    else:
        prompt_text = f"Erstelle einen einfachen Torwart-Trainingsplan für {name}, {alter} Jahre. Fokus: {fokus}."

    # DER BUTTON
    if st.button("Trainingsplan erstellen 🔥"):
        if name:
            with st.spinner('Dein Coach erstellt den Plan...'):
                try:
                    # Hier passiert die Magie
                    response = model.generate_content(prompt_text)
                    st.success(f"Fertig! Hier ist dein Plan, {name}:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"KI-Fehler: Bitte prüfe, ob dein API-Key im Google AI Studio aktiv ist. Details: {e}")
        else:
            st.warning("Bitte gib zuerst deinen Namen ein!")

# --- SEITE: ÜBER UNS ---
elif page == "Über KeeperIQ":
    st.title("Über KeeperIQ 🚀")
    st.write(f"""
    **KeeperIQ wurde von Tyler entwickelt**, um das Torwartspiel auf das nächste Level zu heben. 
    Durch den Einsatz von Künstlicher Intelligenz erhältst du Pläne, die normalerweise nur Profis bekommen.
    """)

# --- SEITE: UPGRADE ---
elif page == "PRO Upgrade 💎":
    st.title("Hol dir das PRO-Upgrade 💎")
    st.write("""
    - ✅ Berücksichtigung von Untergrund & Fitness
    - ✅ Spezielle Übungen für dein Equipment
    - ✅ Unlimitierte Anfragen
    
    **Interesse? Kontaktiere Tyler für deinen Freischalt-Code!**
    """)
    
