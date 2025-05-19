import streamlit as st
import plotly.express as px
import pandas as pd

# --- Configuración general ---
st.set_page_config(page_title="Tendencias de Clima y Químicos", layout="wide")
st.title("Tendencias de NH4, Tolueno, Humedad y Temperatura")

# --- Función para cargar y preprocesar los datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    df = df.sort_values("Timestamp")
    return df

df = cargar_datos()

# --- Diccionario para iterar con elegancia y sentido de la estética ---
variables = {
    "NH4 (ppm)": " NH4",
    "Tolueno (ppm)": " Tolueno",
    "Humedad (%)": " Humedad",
    "Temperatura (°C)": " Temperatura"
}

# --- Filtros interactivos ---
with st.sidebar:
    st.markdown("**Filtros**")
    meses_unicos = df["Mes"].unique().tolist()
    meses_seleccionados = st.multiselect("Selecciona meses:", meses_unicos, default=meses_unicos)
    rango_fechas = st.date_input(
        "Selecciona el rango de fechas:",
        value=(df["Timestamp"].min().date(), df["Timestamp"].max().date())
    )

# --- Aplicar filtros al dataframe ---
df_filtrado = df[
    (df["Mes"].isin(meses_seleccionados)) &
    (df["Timestamp"].dt.date >= rango_fechas[0]) &
    (df["Timestamp"].dt.date <= rango_fechas[1])
]

# --- Mostrar advertencia si no hay datos ---
if df_filtrado.empty:
    st.warning(" No hay datos para los filtros seleccionados.")
    st.stop()

# --- Visualizaciones en layout responsivo ---
for i, (columna, nombre_variable) in enumerate(variables.items()):
    with st.expander(f"{nombre_variable} en el Tiempo", expanded=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            fig = px.line(
                df_filtrado,
                x="Timestamp",
                y=columna,
                color="Mes",
                markers=True,
                labels={columna: nombre_variable, "Timestamp": "Fecha"}
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.metric(
                label=f"Media {nombre_variable}",
                value=f"{df_filtrado[columna].mean():.2f}"
            )
            st.metric(
                label="Máximo",
                value=f"{df_filtrado[columna].max():.2f}"
            )
            st.metric(
                label="Mínimo",
                value=f"{df_filtrado[columna].min():.2f}"
            )

# --- Tabla resumen de promedios ---
with st.expander(" Promedios Mensuales Filtrados"):
    resumen = (
        df_filtrado.groupby("Mes")[list(variables.keys())]
        .mean()
        .round(2)
        .sort_index()
    )
    st.dataframe(resumen.style.format("{:.2f}"))
