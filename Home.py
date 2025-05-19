# app.py (o main.py si prefieres)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

# --- Configuración general de la app ---
st.set_page_config(page_title="Dashboard Gases y Clima", layout="wide")
st.title("Dashboard Interactivo de Gases y Clima")

# --- Cargar datos con caché ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    return df

df = cargar_datos()
df_sorted = df.sort_values("Timestamp")
gases_cols = ["Acetone (ppm)", "CO2 (ppm)", "Ethanol (ppm)", "NH4 (ppm)", "Tolueno (ppm)"]

