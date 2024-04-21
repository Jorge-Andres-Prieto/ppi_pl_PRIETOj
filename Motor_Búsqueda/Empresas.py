import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests

def set_style():
    """Aplica estilos CSS personalizados a la aplicación."""
    style = """
    <style>
    html, body, [class*="css"] {
        background-color: #4285f4;
        color: #000000;
        font-family: 'sans serif';
    }
    .stTextInput > label, .stButton > button {
        color: #ffffff;
    }
    .stButton > button {
        background-color: #ffffff;
        color: #4285f4;
        border-radius: 5px;
        border: 1px solid #4285f4;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

class SearchApp:
    def __init__(self):
        # Inicializa como antes, ajustando las URL de datos y animaciones según sea necesario
        self.data_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv'

    def load_lottiefile(self, url: str) -> dict:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return {}

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_url)

    def main(self):
        set_style()  # Aplica los estilos al inicio del método main
        st.markdown("<h1 style='text-align: center; color: white;'>Motor de Búsqueda</h1>", unsafe_allow_html=True)
        # Resto de tu código sigue aquí

# El resto de tu clase y el punto de entrada de la aplicación se mantienen igual

if __name__ == "__main__":
    app = SearchApp()
    app.main()
