import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st



st.set_page_config(page_title="Análise de Veículos", layout="wide")

st.title("🚗 Análise de Dados de Veículos")
st.markdown("""
Este aplicativo permite a visualização interativa de um conjunto de dados de veículos.
Você pode:
- Visualizar histogramas do odômetro
- Criar gráficos de dispersão para analisar preço vs ano
""")
st.markdown("---")

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



st.subheader("🔍 Selecione as colunas para o gráfico de dispersão")
x_axis = st.selectbox('Eixo X', options=car_data.columns, index=car_data.columns.get_loc("model_year"))
y_axis = st.selectbox('Eixo Y', options=car_data.columns, index=car_data.columns.get_loc("price"))

if st.button('Criar gráfico de dispersão personalizado'):
    fig = px.scatter(car_data, x=x_axis, y=y_axis, color='type')
    st.plotly_chart(fig, use_container_width=True)


st.subheader("🚘 Filtrar por tipo de veículo")
vehicle_types = car_data['type'].unique()
selected_types = st.multiselect('Escolha os tipos', vehicle_types, default=vehicle_types)

filtered_data = car_data[car_data['type'].isin(selected_types)]

   

st.markdown("---")
st.markdown("Desenvolvido por Lucas 🚀 | Powered by Streamlit & Plotly")
