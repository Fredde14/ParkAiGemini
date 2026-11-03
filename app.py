import streamlit as st
from PIL import Image
import numpy as np
from models.parking_model import get_parking_assistant_model

# --- SEITEN-KONFIGURATION ---
st.set_page_config(
    page_title="KI Parkassistent",
    page_icon="🚗",
    layout="wide", # Nutzt die volle Breite, wie im Bild
)

# --- Initialisiere KI-Modell ---
@st.cache_resource
def load_ai():
    return get_parking_assistant_model()

ai_model = load_ai()

# --- HEADER BEREICH (wie im Bild) ---
with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("🔧 (icon)") # Platzhalter für das Icon
    with col2:
        st.title("🚗 KI Parkassistent")
    with col3:
        st.write("(User Image)") # Platzhalter für das User Image

st.write("---")

# --- HAUPTBEREICH (wie im Bild) ---
# Erstelle drei Hauptspalten: Einstellungen, Handy-Analyse, Anleitung/Simulation
col_settings, col_phone, col_guide = st.columns([2, 3, 3], gap="large")

# --- SPALTE 1: EINSTELLUNGEN ---
with col_settings:
    st.header("🔧 Einstellungen")
    
    st.subheader("Auto-Maße")
    car_length = st.number_input("Länge (m):", min_value=3.0, max_value=6.0, value=4.5, step=0.1)
    
    # Slider für Breite (wie im Bild)
    # Beachte: Streamlit slider zeigt die range anders an, aber wir passen sie an
    st.subheader("🔧 Breite (m)")
    car_width = st.slider("🔧 Breite (m)", min_value=1.5, max_value=2.8, value=1.8, step=0.1)
    
    # Park-Typ Auswahl (wie im Bild)
    st.subheader("Park-Typ:")
    parking_type = st.selectbox("Park-Typ:", ["Längseinparken (Parallel)", "Querseinparken (Senkrecht)"])
    
    # Die zwei nummerierten Buttons (wie im Bild)
    st.write("---")
    analysieren_btn = st.button("1. 📸 FOTO ANALYSIEREN", use_container_width=True)
    st.write("")
    starten_btn = st.button("2. 🚗 EINPARKHILFE STARTEN", use_container_width=True)

# --- SPALTE 2: HANDY-ANALYSE ---
with col_phone:
    # Füge einen Wrapper hinzu, um die Spalte wie ein Handy aussehen zu lassen (optional, aber cool für das Projekt)
    st.markdown('<div class="phone-frame">', unsafe_allow_html=True)
    st.header("Parklücke Analyse")
    
    uploaded_file = st.file_uploader("Lade ein Foto deiner Parklücke hoch...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Konvertiere Upload in PIL Image
        pil_image = Image.open(uploaded_file)
        
        with st.spinner("KI analysiert Parklücke..."):
            # Nutze das KI-Modell
            gap_size, annotated_image_np, cars_found = ai_model.analyze_image(pil_image)
            
            # Zeige das analysierte Bild (wie im Bild)
            # Annotiere das Bild, um Lücke und Maße anzuzeigen
            # Dies ist ein Platzhalter-Bild, das dem KI-Ergebnis nahe kommt
            annotated_image_pil = Image.fromarray(annotated_image_np.astype('uint8'), 'RGB')
            st.image(annotated_image_pil, caption=f"Analyse abgeschlossen. {cars_found} Autos erkannt.", use_container_width=True)
            
            # Simuliere die Maße und die Lücke (wie im Bild)
            st.success(f"Lücke erkannt: {gap_size:.1f}m")
            
            # Anzeige der Maße unter dem Bild (wie im Bild)
            st.write(f"Maße (m): {car_length:.1f} x {car_width:.1f}")
            st.write(f"Erkannte Lücke: {gap_size:.1f}m")
            
    st.markdown('</div>', unsafe_allow_html=True) # Ende Handy-Frame

# --- SPALTE 3: ANLEITUNG / SIMULATION ---
with col_guide:
    st.header("Workflow")
    # Zeige den Workflow-Text an (wie im Bild)
    workflow_steps = "[1. Foto hochladen] → [2. Maße eingeben] → [3. Analyse] → [4. Anleitung]"
    st.info(workflow_steps)
    st.write("---")

    st.header("🚗 Einpark-Simulation & Guide")
    
    # Simulation: Zeige eine Statusmeldung an (wie im Bild)
    # In einem fortgeschrittenen Schritt könntest du hier ein SVG/Bild des Einpark-Pfads generieren.
    if uploaded_file is not None and analysieren_btn:
        benoetigt = car_length + 0.8 # Simuliere benötigten Puffer
        if gap_size >= benoetigt:
            st.success(f"✅ PASST! (Lücke: {gap_size:.1f}m / Benötigt: {benoetigt:.1f}m + Puffer)")
        else:
            st.error(f"❌ ZU ENG! (Lücke: {gap_size:.1f}m / Benötigt: {benoetigt:.1f}m + Puffer)")
    
    st.write("---")
    
    # Der nummerierte Guide (wie im Bild)
    st.header("Einpark-Guide")
    st.markdown("1. ✅ Vorbeifahren und Ausrichten")
    st.markdown("2. ✅ Rückwärts einlenken (Voll nach rechts)")
    st.markdown("3. ✅ Gegenlenken (Voll nach links)")
    
    # Weitere Anleitung Button (wie im Bild)
    st.write("")
    st.button("WEITERE ANLEITUNG ANZEIGEN", use_container_width=True)

# --- Optionales Styling (Css) ---
# Du kannst dies nutzen, um die Spaltenhöhe anzugleichen oder den Handy-Look zu erzeugen.
st.markdown("""
<style>
.phone-frame {
    border: 10px solid #ddd;
    border-radius: 20px;
    padding: 20px;
    background-color: #f9f9f9;
}
</style>
""", unsafe_allow_html=True)
