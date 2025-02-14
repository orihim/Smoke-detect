import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils import load_data, calculate_statistics, create_correlation_matrix
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="Smoke Detection Analysis",
    page_icon="🔥",
    layout="wide"
)

# Language selector
lang = st.sidebar.selectbox('Language / Langue', ['Français', 'English'])

# Translations dictionary
translations = {
    'Français': {
        'title': "🔥 Système d'Analyse de Détection de Fumée",
        'intro': """
## Introduction
Bienvenue dans l'application d'analyse des données de détection de fumée. Ce système utilise des capteurs IoT 
pour surveiller en temps réel différents paramètres environnementaux afin de détecter les risques d'incendie.

### Paramètres surveillés :
- Température et Humidité
- Composés organiques volatils (TVOC)
- Niveaux de CO2
- Particules fines (PM1.0, PM2.5)
- Pression atmosphérique
""",
        'key_viz': "🎯 Visualisations Clés",
        'correlation': "Matrice de Corrélation entre Variables",
        'temp_dist': "Distribution de la Température selon l'Alarme",
        'co2_dist': "Distribution du CO2 selon l'Alarme",
        'interactive_viz': "📈 Visualisations Interactives",
        'select_param': "Sélectionner un paramètre à visualiser",
        'evolution': "Évolution de",
        'created_by': "👩‍💻 Créé par Harras Houda",
        'footer': """
Cette application d'analyse de données de détection de fumée a été développée pour fournir 
une visualisation claire et interactive des données collectées par les capteurs IoT.
"""
    },
    'English': {
        'title': "🔥 Smoke Detection Analysis System",
        'intro': """
## Introduction
Welcome to the smoke detection data analysis application. This system uses IoT sensors 
to monitor various environmental parameters in real-time to detect fire risks.

### Monitored Parameters:
- Temperature and Humidity
- Volatile Organic Compounds (TVOC)
- CO2 Levels
- Fine Particles (PM1.0, PM2.5)
- Atmospheric Pressure
""",
        'key_viz': "🎯 Key Visualizations",
        'correlation': "Correlation Matrix between Variables",
        'temp_dist': "Temperature Distribution by Alarm",
        'co2_dist': "CO2 Distribution by Alarm",
        'interactive_viz': "📈 Interactive Visualizations",
        'select_param': "Select a parameter to visualize",
        'evolution': "Evolution of",
        'created_by': "👩‍💻 Created by Harras Houda",
        'footer': """
This smoke detection data analysis application was developed to provide 
clear and interactive visualization of data collected by IoT sensors.
"""
    }
}

# Get translations for current language
t = translations[lang]

# Title
st.title(t['title'])
st.markdown(t['intro'])

# Key Visualizations Section
st.header(t['key_viz'])

try:
    # Loading images
    st.subheader(t['correlation'])
    st.image('attached_assets/file-YCRkd6pDqgpS2cKkvKTJhS.webp', use_container_width=True)

    st.subheader(t['temp_dist'])
    st.image('attached_assets/file-CCx1Pq16t3EYdpHNmNTCNm.webp', use_container_width=True)

    st.subheader(t['co2_dist'])
    st.image('attached_assets/file-NDG28w88p4SPpFhWCDyrAm.webp', use_container_width=True)
except Exception as e:
    st.error(f"Error loading images: {str(e)}")

try:
    # Loading data
    data = load_data('attached_assets/smoke_detection_iot.csv')

    # Interactive visualizations
    st.header(t['interactive_viz'])

    params = ["Temperature[C]", "Humidity[%]", "TVOC[ppb]", "eCO2[ppm]",
              "Raw H2", "Raw Ethanol", "Pressure[hPa]", "PM1.0", "PM2.5"]

    param = st.selectbox(t['select_param'], params)

    fig = px.line(data, x='datetime', y=param, color='Fire Alarm',
                  title=f"{t['evolution']} {param}")
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error loading or processing data: {str(e)}")

# Footer with signature
st.markdown("---")
st.markdown(t['created_by'])
st.markdown(t['footer'])
