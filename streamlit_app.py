import streamlit as st
import google.generativeai as genai

# 1. API Verbindung (Nutzt deinen hinterlegten Key)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("API Key Fehler! Bitte prüfe deine Streamlit-Secrets.")

# 2. Design & Branding
st.set_page_config(page_title="KeeperIQ", page_icon="🧤")

# Dein Logo (Option 2: Cyber-Glove)
logo_url = "http://googleusercontent.com/generated_image_content/0"
st.image(logo_url, width=250)

st.title("🧤 KeeperIQ – Dein Profi-Coach")

# --- SEITENLEISTE (BUSINESS-CENTER) ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Gehe zu:", ["Training", "Über KeeperIQ", "PRO Upgrade 💎"])

if page == "Training":
    st.sidebar.markdown("---")
    version = st.sidebar.radio("Deine Mitgliedschaft:", ["Standard (Kostenlos)", "PRO (Premium 💎)"])
    
    if version == "PRO (Premium 💎)":
        st.success("💎 PRO-MODUS: Aktive KI-Leistungsanalyse.")
    else:
        st.info("💡 Tipp: Nutze PRO für 3x schnellere Entwicklung.")

    # --- HAUPTBEREICH: TRAINING ---
    name = st.text_input("Wie heißt du?")
    alter = st.number_input("Dein Alter", min_value=5, max_value=50, value=21)
    fokus = st.selectbox("Heutiger Schwerpunkt:", 
                         ["Reaktion", "Flanken", "1 gegen 1", "Strafraumbeherrschung", "Abschlag", "Stellungsspiel"])

    # PRO-FEATURES
    if version == "PRO (Premium 💎)":
        st.subheader("PRO-Parameter für maximale Präzision")
        col1, col2 = st.columns(2)
        with col1:
            fitness = st.select_slider("Dein Energie-Level:", options=["Erschöpft", "Normal", "Topfit"])
            untergrund = st.selectbox("Untergrund:", ["Rasen", "Kunstrasen", "Hartplatz", "Halle"])
        with col2:
            equipment = st.multiselect("Equipment:", ["Hütchen", "Rebounder", "Koordinationsleiter", "Zweiter Keeper"])
            dauer = st.slider("Dauer (Minuten):", 20, 120, 45)
        notiz = st.text_area("Besondere Wünsche oder Zipperlein?")
    else:
        fitness, untergrund, equipment, dauer, notiz = "Normal", "Rasen", [], 30, "Keine"

    if st.button("Trainingsplan erstellen 🔥"):
        if name:
            with st.spinner('Dein Coach analysiert die Daten...'):
                try:
                    if version == "PRO (Premium 💎)":
                        prompt = (f"Du bist ein ELITE Torwart-Trainer. Erstelle einen hochpersonalisierten Plan für {name} ({alter}J). "
                                  f"Fokus: {fokus}. Energie: {fitness}. Boden: {untergrund}. Equipment: {equipment}. "
                                  f"Dauer: {dauer} Min. Zusatz: {notiz}. "
                                  f"Erstelle Warm-up, 3 Profi-Übungen und Cool-down. Sei motivierend!")
                    else:
                        prompt = f"Erstelle einen einfachen Torwart-Trainingsplan für {name}, {alter} Jahre. Fokus: {fokus}."

                    response = model.generate_content(prompt)
                    st.success(f"Dein Plan ist bereit, {name}!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Fehler: {e}")
        else:
            st.warning("Bitte gib deinen Namen ein!")

elif page == "Über KeeperIQ":
    st.header("Über KeeperIQ 🚀")
    st.write(f"""
    **Willkommen in der Zukunft des Torwartspiels!**
    
    KeeperIQ wurde von **Tyler** entwickelt, um jedem Torwart – egal ob Kreisliga oder Profi – 
    Zugang zu modernster KI-Technologie zu verschaffen. 
    
    Warum KeeperIQ?
    * **Intelligente Analyse:** Die KI versteht deine Schwächen.
    * **Anpassung:** Dein Training passt sich deinem Untergrund und deiner Fitness an.
    * **Schnellerer Fortschritt:** Gezielte Übungen statt Standard-Programm.
    """)

elif page == "PRO Upgrade 💎":
    st.header("Hol dir den PRO-Status 💎")
    st.write("""
    Schalte das volle Potenzial von KeeperIQ frei:
    - ✅ Berücksichtigung von Equipment & Untergrund
    - ✅ Fitness-gesteuerte Intensität
    - ✅ Unbegrenzte Trainingspläne
    - ✅ Schnellerer Muskelaufbau & Reaktionszeit
    
    **Interesse? Melde dich bei Tyler für deinen Zugangscode!**
    """)
                                                      
