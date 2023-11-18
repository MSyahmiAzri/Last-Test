import pandas as pd
import streamlit as st


st.set_page_config(page_title='QR SAVR', 
                   page_icon="💔")


st.header('Senarai QR SAVR QR03')
#st.subheader('Please fill in the form below')

st.sidebar.markdown('''
Created with 💔 by SyuhadaAdila.
''')

excel_file = 'QR SAVR B4 BBB 2023.xlsx'
sheet_name = 'QR03 Kejanggalaan & Pembaikan'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='H:BC',
                   header=3)



st.dataframe(df)


