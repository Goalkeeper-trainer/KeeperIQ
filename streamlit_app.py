import streamlit as st
import google.generativeai as genai

# 1. API Verbindung & Modell-Definition
try:
    api_key = st.secrets["AIzaSyD08tKZBrvtmuB8VUjU4PeWfMxii2l9QTs"]
    genai.configure(api_key=api_key)
    
    # Das "Gehirn" der App definieren (Gemini 1.5 Flash für Speed)
    model = genai.GenerativeModel('gemini-1.5-flash') 
except Exception as e:
    st.error(f"API Fehler: {e}")

# 2. Design & Branding
st.set_page_config(page_title="KeeperIQ", page_icon="🧤")

# Dein Cyber-Logo
logo_url = "https://raw.githubusercontent.com/Torwart-Trainer/KeeperIQ/main/logo.png"
# Falls das Github-Logo noch nicht da ist, nutzen wir einen Platzhalter, damit es keine Fehler gibt
try:
    st.image(logo_url, width=250)
except:
    st.title("🧤 KeeperIQ")

st.title("KeeperIQ – Dein Profi-Coach")

# --- SEITENLEISTE (BUSINESS-CENTER) ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Gehe zu:", ["Training", "Über KeeperIQ", "PRO Upgrade 💎"])

if page == "Training":
    st.sidebar.markdown("---")
    version = st.sidebar.radio("Deine Mitgliedschaft:", ["Standard (Kostenlos)", "PRO (Premium 💎)"])
    
    if version == "PRO (Premium 💎)":
        st.success("💎 PRO-MODUS AKTIVIERT")
    else:
        st.info("💡 Tipp: Nutze PRO für 3x schnellere Entwicklung.")

    # --- HAUPTBEREICH: TRAINING ---
    name = st.text_input("Wie heißt du?", placeholder="z.B. Tyler")
    alter = st.number_input("Dein Alter", min_value=5, max_value=50, value=21)
    fokus = st.selectbox("Heutiger Schwerpunkt:", 
                         ["Reaktion", "Flanken", "1 gegen 1", "Strafraumbeherrschung", "Abschlag", "Stellungsspiel"])

    # PRO-FEATURES
    if version == "PRO (Premium 💎)":
        st.subheader("PRO-Analyse Parameter")
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
            with st.spinner('Coach analysiert die Daten...'):
                try:
                    # Der Auftrag an die KI (Prompt)
                    if version == "PRO (Premium 💎)":
                        prompt = (f"Du bist ein ELITE Torwart-Trainer. Erstelle einen hochpersonalisierten Plan für {name} ({alter}J). "
                                  f"Fokus: {fokus}. Energie: {fitness}. Boden: {untergrund}. Equipment: {equipment}. "
                                  f"Dauer: {dauer} Min. Zusatz: {notiz}. "
                                  f"Erstelle ein Warm-up, 3 Profi-Übungen und ein Cool-down. Sei motivierend!")
                    else:
                        prompt = f"Erstelle einen einfachen Torwart-Trainingsplan für {name}, {alter} Jahre. Fokus: {fokus}. Gib 3 kurze Übungen an."

                    # Hier wird die KI aufgerufen
                    response = model.generate_content(prompt)
                    st.success(f"Dein Plan ist bereit, {name}!")
                    st.markdown(response.text)
                    
                    if version == "Standard (Kostenlos)":
                        st.markdown("---")
                        st.write("🚀 **Willst du noch schnellere Fortschritte?** Upgrade auf PRO für Berücksichtigung von Equipment und Fitness!")
                except Exception as e:
                    st.error(f"Fehler bei der Erstellung: {e}")
        else:
            st.warning("Bitte gib deinen Namen ein!")

elif page == "Über KeeperIQ":
    st.header("Über KeeperIQ 🚀")
    st.write(f"""
    **Willkommen in der Zukunft des Torwartspiels!**
    
    KeeperIQ wurde von **Tyler** entwickelt, um jedem Torwart Zugang zu modernster KI-Technologie zu verschaffen. 
    """)

elif page == "PRO Upgrade 💎":
    st.header("Hol dir den PRO-Status 💎")
    st.write("""
    Schalte das volle Potenzial frei:
    - ✅ Berücksichtigung von Equipment & Untergrund
    - ✅ Fitness-gesteuerte Intensität
    - ✅ Unbegrenzte Trainingspläne
    """)
    
