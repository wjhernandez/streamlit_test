import pandas as pd
import scipy.stats
import streamlit as st
import time

# Inicializamos las variables de estado
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

# Gráfico inicial con valor medio 0.5
chart = st.line_chart([0.5])

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# Slider para seleccionar número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para ejecutar experimento
start_button = st.button('Ejecutar')

st.write("Intentos seleccionados:", number_of_trials)


if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)

    # Guardar los resultados en el DataFrame de estado
    nuevo_resultado = pd.DataFrame(
        data=[[st.session_state['experiment_no'], number_of_trials, mean]],
        columns=['no', 'iteraciones', 'media']
    )

    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        nuevo_resultado
    ], axis=0).reset_index(drop=True)

# Mostrar tabla con resultados
st.write(st.session_state['df_experiment_results'])
