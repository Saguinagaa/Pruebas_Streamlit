import streamlit as st
import pandas as pd
import numpy as np

def calculate_amortization(interest_rate, months, loan_amount):
    # Calculating the monthly interest rate
    monthly_interest_rate = interest_rate / 12 / 100
    
    # Calculating the monthly payment using the formula for an amortizing loan
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    
    # Creating a DataFrame for the amortization schedule
    amortization_schedule = pd.DataFrame(
        columns=['Month','Payment', 'Principal',
                 'Interest', 'Remaining Balance'])
    remaining_balance = loan_amount
    
    for month in range(1, months + 1):
        interest = remaining_balance * monthly_interest_rate
        principal = monthly_payment - interest
        remaining_balance -= principal
        
        amortization_schedule = amortization_schedule._append({
            'Month': month,
            'Payment': monthly_payment,
            'Principal': principal,
            'Interest': interest,
            'Remaining Balance': remaining_balance
        }, ignore_index=True)
        
    amortization_schedule.rename(columns={"Month": "Mes", "Payment": "Pago",
                                  "Pricipal": "Abono a deuda", "Interest": "Abono a interes",
                                  "remaining_balance": "Deuda actual"})
    return monthly_payment, amortization_schedule

# Streamlit app
st.title('Calculadora de Préstamos y Amortización')

# User input for loan details
interest_rate = st.number_input('Tasa de interés anual (%)',
                                min_value=0.01, value=5.0, step=0.01)
months = st.number_input('Número de meses', min_value=1,
                         value=12, step=1)
loan_amount = st.number_input('Monto del préstamo',
                              min_value=1.0, value=1000.0, step=1.0)

if st.button('Calcular'):
    monthly_payment, amortization_table = calculate_amortization(
        interest_rate, months, loan_amount)
    
    st.subheader('Detalles del Préstamo')
    st.write(f'Monto del préstamo: {loan_amount}')
    st.write(f'Tasa de interés anual: {interest_rate}%')
    st.write(f'Número de meses: {months}')
    st.write(f'Cuota mensual: {monthly_payment:.2f}')
    
    st.subheader('Tabla de Amortización')
    st.write(amortization_table)
