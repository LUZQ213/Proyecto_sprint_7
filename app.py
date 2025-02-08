import pandas as pd
import streamlit as st 
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Aplicacion web para analizar las ventas de coches")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_1 = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)
    
build_histogram = st.checkbox('Construir un diagrama de dispersion')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un diagrama de dispersion para la columna odómetro')
    fig_2 = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(fig_2, use_container_width=True)
    