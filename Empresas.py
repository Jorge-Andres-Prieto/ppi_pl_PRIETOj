# Importar las librerías requeridas
import streamlit as st
import numpy as np
import pandas as pd

# Cargar los datos
ruta_registradas = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv'

registradas_df = pd.read_csv(ruta_registradas)

# Encontrar los nombres de las columnas
columnas_df = registradas_df.columns.tolist()

# Búsqueda por nombre de empresa
termino_busqueda = st.text_input("Ingrese el nombre de la empresa a buscar:", "")
# Convertir a mayúsculas y eliminar espacios
termino_busqueda = termino_busqueda.upper().strip()

# Filtrar el DataFrame
resultados_df = registradas_df[registradas_df["RAZON SOCIAL"].str.match(termino_busqueda, case=False)]

# Mostrar los resultados
if len(resultados_df) > 0:
    st.table(resultados_df[columnas_df])
else:
    st.info("No se encontraron empresas con el nombre ingresado.")
