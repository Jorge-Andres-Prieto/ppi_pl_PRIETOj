import matplotlib.pyplot as plt
import streamlit as st

# Crea un DataFrame
df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})

# Crea un gráfico de líneas
st.line_chart(df)
