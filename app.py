import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st



car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
        
build_histogram = st.checkbox('Criar histograma de odômetro')
if build_histogram:
    st.write('Criando histograma...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão: Preço vs Ano')
if build_scatter:
    st.write('Criando gráfico de dispersão...')
    fig = px.scatter(car_data, x="model_year", y="price", color="type")
    st.plotly_chart(fig, use_container_width=True)