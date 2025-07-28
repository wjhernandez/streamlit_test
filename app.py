import streamlit as st
import pandas as pd
import numpy as np
import time

st.header('Lanzar una moneda')

# Deslizador para elegir cantidad de lanzamientos
number_of_trials = st.slider('¿Número de lanzamientos?', 1, 1000, 10)

# Botón para iniciar el experimento
start_button = st.button('🎲 Ejecutar')

# Si se presiona el botón
if start_button:
    st.write(f'🚀 Ejecutando experimento con {number_of_trials} lanzamientos...')

    results = []
    progress_bar = st.progress(0)

    for i in range(number_of_trials):
        result = np.random.randint(0, 2)  # 0 = cara, 1 = sello
        results.append(result)
        progress_bar.progress((i + 1) / number_of_trials)
        time.sleep(0.01)  # pausa breve para animación

    results_df = pd.DataFrame(results, columns=['Resultado'])
    results_df['Resultado'] = results_df['Resultado'].map({0: 'Cara', 1: 'Sello'})
    st.write('Resultados de los lanzamientos:')
    st.dataframe(results_df)

    promedio = np.mean(results)
    st.write(f'Porcentaje de "Sello": {promedio*100:.2f}%')
