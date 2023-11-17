import streamlit as st

def nominal_a_efectiva(tasa_nominal, periodo_capitalizacion):
    if periodo_capitalizacion == 'Mensual':
        n = 12
    elif periodo_capitalizacion == 'Trimestral':
        n = 4
    elif periodo_capitalizacion == 'Semestral':
        n = 2
    else:  # Anual
        n = 1
    
    tasa_efectiva = n * ((1 + tasa_nominal) ** (1 / n) - 1)
    return tasa_efectiva

def efectiva_a_nominal(tasa_efectiva, periodo_capitalizacion):
    if periodo_capitalizacion == 'Mensual':
        n = 12
    elif periodo_capitalizacion == 'Trimestral':
        n = 4
    elif periodo_capitalizacion == 'Semestral':
        n = 2
    else:  # Anual
        n = 1
    
    tasa_nominal = ((1 + tasa_efectiva / n) ** n) - 1
    return tasa_nominal

st.title('Conversor de Tasas de Interés')

tipo_conversion = st.selectbox('Seleccione el tipo de conversión:', ['Nominal a Efectiva', 'Efectiva a Nominal'])

if tipo_conversion == 'Nominal a Efectiva':
    tasa_nominal = st.number_input('Ingrese la tasa de interés nominal:', min_value=0.0, value=0.0, step=0.01)
    periodo_capitalizacion = st.selectbox('Seleccione el periodo de capitalización:', ['Mensual', 'Trimestral', 'Semestral', 'Anual'])

    if st.button('Convertir'):
        tasa_efectiva = nominal_a_efectiva(tasa_nominal, periodo_capitalizacion)
        st.write(f"La tasa de interés efectiva es: {tasa_efectiva:.4f}")
else:
    tasa_efectiva = st.number_input('Ingrese la tasa de interés efectiva:', min_value=0.0, value=0.0, step=0.01)
    periodo_capitalizacion = st.selectbox('Seleccione el periodo de capitalización:', ['Mensual', 'Trimestral', 'Semestral', 'Anual'])

    if st.button('Convertir'):
        tasa_nominal = efectiva_a_nominal(tasa_efectiva, periodo_capitalizacion)
        st.write(f"La tasa de interés nominal es: {tasa_nominal:.4f}")
