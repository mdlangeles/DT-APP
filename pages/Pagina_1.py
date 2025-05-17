# pages/1_Pagina_1_Tendencias_Gases.py

import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- Configuración inicial ---
st.set_page_config(page_title="Página 1 - Tendencias de Gases", layout="wide")
st.title("Página 1 - Tendencias Temporales de Gases")

# --- Cargar datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    return df

df = cargar_datos()
df_sorted = df.sort_values("Timestamp")

# --- Gráfica 1: Acetona en el tiempo (modo streaming simulado) ---
st.subheader("Tendencia de Acetona (ppm) en el Tiempo - Streaming")

placeholder1 = st.empty()
n = len(df_sorted)

for i in range(10, n, 10):  # Cargar de 10 en 10 datos (simula llegada en tiempo real)
    fig_stream = px.line(df_sorted.iloc[:i], x="Timestamp", y="Acetone (ppm)",
                         color="Mes", markers=True)
    placeholder1.plotly_chart(fig_stream, use_container_width=True)
    time.sleep(0.9)  # Controla la velocidad de actualización

# --- Gráfica 2: Etanol en el tiempo ---
st.subheader("Tendencia de Etanol (ppm) en el Tiempo")
fig2 = px.line(df_sorted, x="Timestamp", y="Ethanol (ppm)", color="Mes", markers=True)
st.plotly_chart(fig2, use_container_width=True)

# --- Gráfica 3: CO en el tiempo ---
st.subheader("Tendencia de CO (ppm) en el Tiempo")
fig3 = px.line(df_sorted, x="Timestamp", y="CO (ppm)", color="Mes", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# --- Gráfica 4: CO2 en el tiempo ---
st.subheader("Tendencia de CO2 (ppm) en el Tiempo")
fig4 = px.line(df_sorted, x="Timestamp", y="CO2 (ppm)", color="Mes", markers=True)
st.plotly_chart(fig4, use_container_width=True)

# --- Tabla de promedios por mes ---
st.subheader("Promedio Mensual de Gases")
promedios = df.groupby("Mes")[["Acetone (ppm)", "Ethanol (ppm)", "CO (ppm)", "CO2 (ppm)"]].mean().round(2)
st.dataframe(promedios)
