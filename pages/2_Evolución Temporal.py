import streamlit as st
import plotly.express as px
import pandas as pd
from styles import aplicar_estilos

st.set_page_config(page_title="Eco13 Dashboard", layout="wide")

aplicar_estilos()

# --- Configuración general ---
st.title("Evolución temporal por variable")

# --- Función para cargar y preprocesar los datos ---
@st.cache_data  
def cargar_datos():
    df = pd.read_csv("datos_gases_y_clima_abril2025.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df["Mes"] = df["Timestamp"].dt.month_name()
    df = df.sort_values("Timestamp")
    return df

df = cargar_datos()

# Diccionario para iterar con elegancia y sentido de la estética
variables = {
    "NH4 (ppm)": " NH4",
    "Tolueno (ppm)": " Tolueno",
    "Humedad (%)": " Humedad",
    "Temperatura (°C)": " Temperatura",
    "CO2 (ppm)": " CO2",
    "Acetone (ppm)": " Acetona",
    "Ethanol (ppm)": " Etanol",
    "CO (ppm)": " CO"
}

# Diccionario de descripciones para cada variable
descripciones = {
    "NH4 (ppm)": """
    - El **amoníaco (NH₄)** mostró concentraciones elevadas, probablemente asociadas a la **quema de residuos** o **descomposición de materia orgánica** en sectores con **recolección deficiente de basuras**.
    - En viviendas con **escasa ventilación** y alta densidad, este gas puede acumularse fácilmente, representando un **riesgo para la salud respiratoria**.
    """,

    "Tolueno (ppm)": """
    - El **tolueno**, presente en combustibles y solventes, muestra concentraciones que podrían estar relacionadas con **actividad vehicular**, **talleres informales** o **zonas comerciales densas**.
    - En entornos con **infraestructura no planificada y alta densidad humana**, su presencia refleja **exposición crónica a contaminantes volátiles**.
    """,

    "Humedad (%)": """
    - La **humedad relativa** tiende a ser elevada en sectores con **estructuras cerradas**, **materiales absorbentes** y escasa ventilación natural.
    - Estas condiciones favorecen la **retención de gases contaminantes** y agravan problemas respiratorios en zonas densamente habitadas.
    """,

    "Temperatura (°C)": """
    - Las **altas temperaturas** intensifican la **evaporación de compuestos químicos** como tolueno, etanol y acetona.
    - En barrios con **calles estrechas, techos metálicos y poca vegetación**, se forman **microclimas de isla de calor urbano**, que aumentan el estrés térmico y la contaminación ambiental.
    """,

    "CO2 (ppm)": """
    - El **CO₂** mantiene niveles relativamente estables, con aumentos asociados al uso intensivo de **cocinas y ocupación de espacios cerrados**.
    - En viviendas con **hacinamiento y pobre ventilación**, esto evidencia la **falta de renovación del aire**, afectando el bienestar general.
    """,

    "Acetone (ppm)": """
    - La **acetona** aparece como subproducto de actividades domésticas o comerciales que usan **productos de limpieza, esmaltes o solventes**.
    - En locales pequeños sin ventilación, su acumulación representa un riesgo, especialmente en **espacios de trabajo informal**.
    """,

    "Ethanol (ppm)": """
    - El **etanol** es común en contextos donde se utilizan **productos desinfectantes y de limpieza** de forma constante.
    - Su presencia en ambientes cerrados con **limitada circulación de aire** puede convertirse en un contaminante persistente y poco percibido.
    """,

    "CO (ppm)": """
    - El **monóxido de carbono (CO)** se relaciona con **prácticas de cocción** como el uso de fogones o combustión incompleta en hogares con **baja ventilación**.
    - Su acumulación en viviendas densamente ocupadas representa un **riesgo silencioso**, común en contextos con **limitado acceso a energías limpias**.
    """
}






# Recorremos de a 2 variables por fila
items = list(variables.items())
for i in range(0, len(items), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(items):
            columna, nombre_variable = items[i + j]
            with cols[j]:
                st.markdown(f"#### {nombre_variable}")
                fig = px.line(
                    df,
                    x="Timestamp",
                    y=columna,
                    color="Mes",
                    markers=True,
                    labels={columna: nombre_variable, "Timestamp": "Fecha"}
                )
                st.plotly_chart(fig, use_container_width=True)

                col_a, col_b, col_c = st.columns(3)
                col_a.metric(label="Media", value=f"{df[columna].mean():.2f}")
                col_b.metric(label="Máximo", value=f"{df[columna].max():.2f}")
                col_c.metric(label="Mínimo", value=f"{df[columna].min():.2f}")

                # Descripción interpretativa (colapsada por defecto)
                with st.expander("Descripción", expanded=False):
                    st.markdown(descripciones.get(columna, "Descripción no disponible."))


# --- Tabla resumen de promedios ---
with st.expander(" Promedios Mensuales", expanded=True):
    resumen = (
        df.groupby("Mes")[list(variables.keys())]
        .mean()
        .round(2)
        .sort_index()
    )
    st.dataframe(resumen.style.format("{:.2f}"))
