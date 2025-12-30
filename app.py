import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header("Análisis exploratorio de anuncios de coches")

# cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# botón histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma del odómetro")
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# botón scatter
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig = go.Figure(
        data=[go.Scatter(
            x=car_data["odometer"],
            y=car_data["price"],
            mode="markers"
        )]
    )
    fig.update_layout(title="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)

