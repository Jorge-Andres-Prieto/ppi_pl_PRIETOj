import streamlit as st
import pandas as pd

# Cargar el dataframe de empresas
empresas_df = pd.read_csv("empresas.csv")

# Obtener la lista de barrios
barrios = empresas_df["BARRIO"].unique()

# Función para buscar empresas por razón social
def buscar_empresas(razon_social):
    return empresas_df[empresas_df["RAZON_SOCIAL"].str.contains(razon_social, regex=False)]

# Agregar widget de búsqueda por razón social
razon_social = st.text_input("Ingrese la razón social de la empresa")

# Filtrar las empresas por barrio
empresas_barrio = empresas_df[empresas_df["BARRIO"] == barrio_seleccionado]

# Buscar empresas por razón social
empresas_busqueda = buscar_empresas(razon_social)

# Mostrar la lista de empresas
st.table(empresas_busqueda & empresas_barrio)

# Calcular el número de empresas por sector
sectores_df = empresas_busqueda & empresas_barrio.groupby("CIIU").size()

# Mostrar las estadísticas
st.metric("Número de empresas", sectores_df.sum())
st.metric("Número de empleados", (empresas_busqueda & empresas_barrio)["empleados"].sum())

# Mostrar un mapa con las empresas del barrio
# (Opcional, requiere librerías adicionales)

# Agregar otras funcionalidades
# (Opcional)

