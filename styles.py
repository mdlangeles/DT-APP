import streamlit as st

def aplicar_estilos():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

    :root {
        --color-bg: #f0fbff;
        --color-text: #000000;
        --color-accent1: #00f0ff;
        --color-accent2: #ff00f7;
        --color-input-bg: #e6faff;
        --color-input-bg-light: rgba(0, 0, 0, 0.04);
        --color-input-border: #00cfff;
        --color-button-bg: #00cfff;
        --color-button-hover: #ff00f7;
        --color-sidebar-bg: #d8f7ff;
        --color-expander-bg: #f9f9f9;
        --color-expander-border: #e0e0e0;
    }

    html, body, #root, [data-testid="stAppViewContainer"] {
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: var(--color-bg) !important;
        font-family: 'Inter', sans-serif;
        color: var(--color-text) !important;
    }

    [data-testid="stSidebar"] {
        background-color: var(--color-sidebar-bg) !important;
        color: var(--color-text) !important;
    }

    [data-testid="stSidebar"] * {
        color: var(--color-text) !important;
    }

    /* Título global en negro sólido */
    h1 {
        font-weight: 700;
        font-size: 2.8rem;
        text-align: center;
        color: var(--color-text);
        background: none;
        -webkit-background-clip: unset;
        -webkit-text-fill-color: unset;
        margin-bottom: 0.3rem;
    }

    /* Clase para títulos con gradiente */
    .gradient-title {
        background: linear-gradient(90deg, var(--color-accent1), var(--color-accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h2, h3 {
        color: #154360;
    }

    p {
        text-align: center;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        color: var(--color-text);
        font-size: 1rem;
        font-weight: 400;
    }

    .stButton>button {
        background: var(--color-button-bg);
        color: var(--color-bg);
        border-radius: 14px;
        padding: 0.75em 1.8em;
        font-weight: 700;
        font-size: 1.05rem;
        border: none;
        cursor: pointer;
        transition: background 0.35s ease, color 0.35s ease;
        box-shadow: 0 0 12px var(--color-button-bg);
    }

    .stButton>button:hover {
        background: var(--color-button-hover);
        color: var(--color-text);
        box-shadow: 0 0 20px var(--color-button-hover);
    }

    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    textarea {
        background-color: var(--color-input-bg-light) !important;
        color: var(--color-text) !important;
        border-radius: 12px;
        border: 1.5px solid var(--color-input-border);
        padding: 0.6em 1em;
        font-size: 1rem;
        font-weight: 500;
        transition: border-color 0.3s ease;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    textarea:focus {
        outline: none;
        border-color: var(--color-button-hover);
        box-shadow: 0 0 10px var(--color-button-hover);
    }

    img {
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0, 240, 255, 0.4);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }

    img:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 35px rgba(255, 0, 247, 0.6);
    }

    /* --- Estilo para Expanders --- */
    [data-testid="stExpander"] {
        background-color: var(--color-expander-bg) !important;
        border: 1px solid var(--color-expander-border);
        border-radius: 12px;
        padding: 0.5em;
        margin-top: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    [data-testid="stExpander"] > details > summary {
        font-weight: 700;
        color: #154360;
        font-size: 1rem;
    }

    .js-plotly-plot .plotly {
        background-color: #FAFAFA !important;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #AAB7B8;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
