import streamlit as st
import pandas as pd
import plotly.express as px

from styles import aplicar_estilos

st.set_page_config(page_title="Eco13 Dashboard", layout="wide")
aplicar_estilos()

# --- Cargar y procesar datos ---
@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    return df.sort_values("Timestamp")

df = cargar_datos()

gases_cols = ["Acetone (ppm)", "CO2 (ppm)", "Ethanol (ppm)", "NH4 (ppm)", "Tolueno (ppm)"]
colores_personalizados = px.colors.qualitative.Set2

# --- Encabezado principal con estilo ---
st.title("🌿 Eco13 Dashboard 🌿")
st.subheader("Monitoreo ambiental desde la comuna 13 del Oriente de Cali")

# --- Descripción general con layout organizado ---
st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <style>
    @keyframes swing {
        0%   { transform: translateX(0); }
        50%  { transform: translateX(8px); }
        100% { transform: translateX(0); }
    }

    .full-width {
        width: 100%;
    }

    .animated-box {
        background-color: #f7f9f9;
        padding: 50px 60px;  /* Más espacio interno */
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        font-size: 18px;
        color: #2C3E50;
        line-height: 1.8;
        animation: swing 4s ease-in-out infinite;
        width: 100%;
        margin: 0 auto;
        box-sizing: border-box;
    }

    /* Eliminar margen interno del bloque de Streamlit */
    .element-container:has(.animated-box) {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    </style>

    <div class="full-width">
      <div class="animated-box">
      Bienvenid@ a <b>Eco13 Dashboard</b>, una plataforma donde los datos ambientales cobran vida.
      <br><br>
      <b>Sobre la Comuna 13 - Oriente de Cali:</b><br>
      La población actual de la Comuna 13 es de <b>171.646 habitantes</b>, según datos del <i>Observatorio de Cali</i>. Esta comuna se caracteriza por ser una zona densamente habitada, con una mezcla de sectores residenciales, actividades comerciales e industriales livianas. Además, enfrenta desafíos ambientales relacionados con el tráfico, el manejo de residuos y la calidad del aire.
      <br><br>
      Aquí podrás:
      <ul>
          <li>Explorar niveles de <b>gases contaminantes</b> como NH₄, Tolueno, CO₂ y más.</li>
          <li>Observar variaciones de <b>temperatura y humedad</b> a lo largo del día.</li>
          <li>Entender el impacto ambiental en la Comuna 13 del <b>Oriente de Cali</b> con visualizaciones modernas.</li>
      </ul>
      <b>¡Explora el menú lateral y empieza tu análisis ambiental!</b>
      </div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{__import__("base64").b64encode(open("data/mapacali.png", "rb").read()).decode()}' 
                 width='400' style='border-radius: 8px; display: inline-block;'/>
            <div style='font-size: 13px; color: #5D6D7E; margin-top: 6px;'>Oriente de Cali</div>
        </div>
    """, unsafe_allow_html=True)

# --- Secciones interactivas ---
st.markdown("---")
st.markdown("### Secciones disponibles:")

seccion1, seccion2 = st.columns(2)

with seccion1:
    st.success("🟢 Página 1\n\n**Análisis de variables de estudio como Humedad y Temperatura**")
    st.markdown("Visualiza y compara variables ambientales.")

with seccion2:
    st.warning("🟡 Página 2\n\n**Evolución Temporal**")
    st.markdown("Composición promedio de gases, relaciones con clima y más insights.")

st.markdown("---")
st.markdown("<center><i>Desarrollado por Mariana Mera, Manuela Mayorga y Ángeles Amú</i></center>", unsafe_allow_html=True)
