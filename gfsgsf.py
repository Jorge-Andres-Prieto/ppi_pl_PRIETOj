import matplotlib.pyplot as plt
import streamlit as st

# Crear datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")

# Mostrar el gráfico en Streamlit
st.pyplot()
