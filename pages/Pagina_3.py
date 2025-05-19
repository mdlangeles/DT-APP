import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuración de página ---
st.set_page_config(page_title="Gráficos Avanzados", layout="wide")
st.title("Gráficos Avanzados - Gases y Variables Ambientales")

# --- Estilos CSS personalizados ---
st.markdown("""
    <style>
        /* Fondo general */
        .stApp {
            background: linear-gradient(135deg, #F4F6F7, #EAEDED);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Títulos */
        h1 {
            color: #1F618D;
            font-size: 2.5em;
        }

        h2, h3 {
            color: #2874A6;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #D6EAF8;
        }

        /* Expanders */
        .st-expanderHeader {
            font-weight: bold;
            color: #154360;
        }

        /* DataFrame background */
        .stDataFrame {
            background-color: #FBFCFC;
        }

        /* Plotly background */
        .js-plotly-plot .plotly {
            background-color: #FAFAFA !important;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #AAB7B8;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Cargar y procesar datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    return df.sort_values("Timestamp")

df = cargar_datos()

# --- Variables importantes ---
gases_cols = ["Acetone (ppm)", "CO2 (ppm)", "Ethanol (ppm)", "NH4 (ppm)", "Tolueno (ppm)"]
colores_personalizados = px.colors.qualitative.Set2

# --- Filtros dinámicos en sidebar ---
with st.sidebar:
    st.markdown("**Filtros avanzados**")
    meses = df["Mes"].unique().tolist()
    meses_sel = st.multiselect("Filtrar por mes:", meses, default=meses)
    fecha_ini, fecha_fin = st.date_input(
        "Rango de fechas:",
        (df["Timestamp"].min().date(), df["Timestamp"].max().date())
    )

# --- Aplicar filtros ---
df_filtrado = df[
    (df["Mes"].isin(meses_sel)) &
    (df["Timestamp"].dt.date >= fecha_ini) &
    (df["Timestamp"].dt.date <= fecha_fin)
]

if df_filtrado.empty:
    st.warning("No hay datos disponibles con los filtros seleccionados.")
    st.stop()

# --- 1. Tendencias de Humedad y Temperatura en el Tiempo ---
with st.expander("1. Humedad vs Temperatura en el Tiempo", expanded=True):
    fig1 = px.line(
        df_filtrado,
        x="Timestamp",
        y=["Humedad (%)", "Temperatura (°C)"],
        markers=True,
        color_discrete_sequence=colores_personalizados,
        labels={"value": "Valor", "variable": "Variable", "Timestamp": "Fecha"}
    )
    st.plotly_chart(fig1, use_container_width=True)

# --- 2. Porcentaje de Gases (Promedio) ---
with st.expander("2. Composición Promedio de Gases (Anillo)", expanded=True):
    prom_gases = df_filtrado[gases_cols].mean().round(2)
    fig2 = px.pie(
        values=prom_gases,
        names=prom_gases.index,
        hole=0.45,
        title="Proporción Promedio de Gases",
        color_discrete_sequence=colores_personalizados
    )
    fig2.update_traces(textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

# --- 3. Gases según Humedad ---
with st.expander("3. Gases en función de la Humedad", expanded=False):
    df_hum = df_filtrado.sort_values("Humedad (%)")
    fig3 = px.line(
        df_hum,
        x="Humedad (%)",
        y=gases_cols,
        labels={"value": "Concentración (ppm)", "variable": "Gas"},
        color_discrete_sequence=colores_personalizados
    )
    st.plotly_chart(fig3, use_container_width=True)

# --- 4. Gases según Temperatura ---
with st.expander("4. Gases en función de la Temperatura", expanded=False):
    df_temp = df_filtrado.sort_values("Temperatura (°C)")
    fig4 = px.line(
        df_temp,
        x="Temperatura (°C)",
        y=gases_cols,
        labels={"value": "Concentración (ppm)", "variable": "Gas"},
        color_discrete_sequence=colores_personalizados
    )
    st.plotly_chart(fig4, use_container_width=True)

# --- 5. Tabla resumen rápida ---
with st.expander("5. Tabla Resumen de Gases"):
    st.dataframe(
        df_filtrado[gases_cols + ["Humedad (%)", "Temperatura (°C)"]]
        .describe()
        .T
        .round(2)
        .rename(columns={
            "mean": "Media",
            "std": "Desviación",
            "min": "Mínimo",
            "max": "Máximo"
        })[["Media", "Desviación", "Mínimo", "Máximo"]]
    )
