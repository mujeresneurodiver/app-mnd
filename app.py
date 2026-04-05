import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Mujeres Neurodivergentes - App de Informes", layout="wide")

# Colores y estilos
COLOR_PRIMARIO = "#4A148C"  # Violeta oscuro
COLOR_SECUNDARIO = "#CE93D8"  # Violeta claro
FONT_PRIMARIA = "Montserrat"
FONT_SECUNDARIA = "Lato"

# Sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: """ + COLOR_PRIMARIO + """;
        color: white;
    }
    .sidebar .sidebar-content a {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo en sidebar
logo_url = "https://i.ibb.co/KKtZG4G/logo-mnd.png"
st.sidebar.image(logo_url, use_column_width=True)

# Menú en sidebar
menu_items = [
    {"icon": "house", "label": "Inicio"},
    {"icon": "file-earmark-person", "label": "Datos"},
    {"icon": "grid-3x3-gap-fill", "label": "Técnicas"},
    {"icon": "diagram-3", "label": "Pruebas Cognitivas"},
    {"icon": "bezier2", "label": "Neuropsicológicas"},
]

for item in menu_items:
    st.sidebar.subheader(f"{item['icon']} {item['label']}")

# Pantalla central
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 100px;">
        <h1 style="font-family: {FONT_PRIMARIA}; font-size: 48px; color: {COLOR_PRIMARIO};">
            Bienvenida al Sistema de Informes
        </h1>
        <img src="https://i.ibb.co/SyJBKTK/cerebro.png" alt="Cerebro" width="200">
    </div>
    """,
    unsafe_allow_html=True,
)

# Botones de selección rápida
columns = st.columns(4)
button_data = [
    {"icon": "🧩", "label": "Autismo"},
    {"icon": "⚡", "label": "TDAH"},
    {"icon": "🌟", "label": "AACC"},
    {"icon": "🔍", "label": "Asesoría Pre-Dx"},
]

for idx, data in enumerate(button_data):
    with columns[idx]:
        st.markdown(
            f"""
            <div style="background-color: {COLOR_SECUNDARIO}; border-radius: 10px; padding: 20px; text-align: center; margin-top: 50px;">
                <div style="font-size: 48px;">{data['icon']}</div>
                <div style="font-family: {FONT_SECUNDARIA}; font-size: 24px; margin-top: 10px;">{data['label']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Lógica de procesamiento de archivos y cálculos
# (Mantengo la misma lógica del código anterior, solo que no la muestro aquí para mayor claridad)