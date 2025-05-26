import streamlit as st
import pandas as pd
import plotly.express as px
from styles import aplicar_estilos

st.set_page_config(page_title="Eco13 Dashboard", layout="wide")
aplicar_estilos()

st.title("Eco13 – Análisis de Variables Ambientales en la Comuna 13")

# --- Introducción general ---
st.markdown("""
<div style='text-align: center; font-size: 18px;'>
Durante abril de 2025 se registraron variables climáticas y gases contaminantes en la zona de <b>Fundautónoma, Comuna 13 de Cali</b>.  
Este dashboard te permite visualizar cómo varían estos factores a lo largo del tiempo y cómo se relacionan entre sí.
</div>
""", unsafe_allow_html=True)


# --- Cargar datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    return df.sort_values("Timestamp")

df = cargar_datos()

# --- Variables ---
gases_cols = ["Acetone (ppm)", "CO2 (ppm)", "Ethanol (ppm)", "NH4 (ppm)", "Tolueno (ppm)"]
colores_personalizados = px.colors.qualitative.Set2

# --- Fila 1: Temperatura y humedad (col1) / Promedio de gases (col2) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <h3 style='text-align: center; color: #000000;'>Humedad vs Temperatura en el Tiempo</h3>
    """, unsafe_allow_html=True)

    with st.expander(" Ver gráfico", expanded=True):
        fig1 = px.line(
            df,
            x="Timestamp",
            y=["Humedad (%)", "Temperatura (°C)"],
            markers=True,
            color_discrete_sequence=colores_personalizados,
            labels={"value": "Valor", "variable": "Variable", "Timestamp": "Fecha"}
        )
        st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Descripción", expanded=False):
        st.markdown("""
        - Las variaciones diarias muestran cómo la **temperatura sube durante el día** y la **humedad aumenta en la madrugada**.
        - Estos factores afectan la **concentración y dispersión de gases**, siendo claves para entender la calidad del aire.
        - En contextos con **alta densidad poblacional** como la Comuna 13, estas condiciones agravan los impactos en salud respiratoria, especialmente para niños y adultos mayores.

        """)


with col2:
    st.markdown("""
    <h3 style='text-align: center; color: #000000;'>Composición Promedio de Gases</h3>
    """, unsafe_allow_html=True)


    with st.expander(" Ver gráfico", expanded=True):
        prom_gases = df[gases_cols].mean().round(2)
        fig2 = px.pie(
            values=prom_gases,
            names=prom_gases.index,
            hole=0.45,
            title="Proporción Promedio de Gases",
            color_discrete_sequence=colores_personalizados
        )
        fig2.update_traces(textinfo='percent+label')
        st.plotly_chart(fig2, use_container_width=True)

    with st.expander("Descripción"):
        st.markdown("""
        - **CO2** es el gas predominante, lo cual es coherente con la alta **actividad humana, vehicular y comercial** en la zona.
        - **Tolueno, Acetona y Etanol** pueden asociarse a **quemas, talleres informales y residuos industriales**, frecuentes en zonas urbanas densamente habitadas.
        - La composición gaseosa refleja cómo el entorno construido y el modo de vida en la Comuna 13 influye directamente en la calidad del aire.

        """)



# --- Fila 2: Gases vs Humedad (col3) / Gases vs Temperatura (col4) ---
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <h3 style='text-align: center; color: #000000;'>Gases en función de la Humedad</h3>
    """, unsafe_allow_html=True)

    with st.expander(" Ver gráfico" , expanded=True):
        df_hum = df.sort_values("Humedad (%)")
        fig3 = px.line(
            df_hum,
            x="Humedad (%)",
            y=gases_cols,
            labels={"value": "Concentración (ppm)", "variable": "Gas"},
            color_discrete_sequence=colores_personalizados
        )
        st.plotly_chart(fig3, use_container_width=True)

    with st.expander("Descripción", expanded=False):
        st.markdown("""
        - Gases como el **NH4 (amoníaco)** tienden a aumentar cuando la **humedad relativa sube**, especialmente por procesos biológicos como la **descomposición de residuos orgánicos**.
        - Estos procesos son más comunes en entornos con **infraestructura sanitaria limitada**, como ocurre en algunos sectores de la comuna.
        - La relación entre humedad y gases resalta la necesidad de gestionar residuos y humedad en zonas de **vulnerabilidad socioambiental**.

        """)


with col4:
    st.markdown("""
    <h3 style='text-align: center; color: #000000;'>Gases en función de la Temperatura</h3>
    """, unsafe_allow_html=True)

    with st.expander(" Ver gráfico", expanded=True):
        df_temp = df.sort_values("Temperatura (°C)")
        fig4 = px.line(
            df_temp,
            x="Temperatura (°C)",
            y=gases_cols,
            labels={"value": "Concentración (ppm)", "variable": "Gas"},
            color_discrete_sequence=colores_personalizados
        )
        st.plotly_chart(fig4, use_container_width=True)

    with st.expander("Descripción", expanded=False):
        st.markdown("""
        - La **temperatura potencia la volatilización** de compuestos, lo que explica aumentos en gases como el **tolueno** durante el día.
        - Otros como el **CO2** mantienen niveles estables, reflejando **fuentes continuas como la respiración humana y el tránsito constante**.
        - En áreas con mucha población y urbanización acelerada, los picos de temperatura tienen un **efecto amplificador de la contaminación**.

        """)


# --- Tabla resumen ---
st.subheader("Tabla Resumen de Gases y Variables Ambientales")

with st.expander(" Ver tabla descriptiva", expanded=True):
    st.dataframe(
        df[gases_cols + ["Humedad (%)", "Temperatura (°C)"]]
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

with st.expander("Descripción", expanded=False):
    st.markdown("""
    - La **media** y **desviación estándar** permiten entender qué tan variables y persistentes son ciertos contaminantes.
    - El **CO2** muestra una alta media y fluctuaciones regulares, consistentes con una población activa y densa durante el día.
    - Gases como **Tolueno y Etanol** presentan **picos máximos que podrían estar ligados a actividades específicas**, como quemas o talleres, que son más frecuentes en zonas con **ocupación informal o comercio no regulado**.

    """)


