import pandas as pd
import streamlit as st


st.set_page_config(page_title='QR SAVR', page_icon=":heart:")
st.header('Update QR SAVR QR03')
st.subheader('Please fill in the form below')

st.sidebar.markdown('''
Created with 💔 by Syahmi
''')

excel_file = 'QR SAVR B4 BBB 2023.xlsx'
sheet_name = 'QR03 Kejanggalaan & Pembaikan'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='H:BC',
                   header=3)

senarai_PE=df["Feeder Name - Nama Jalan"]

with st.form(key="updatedefect"):
    senarai_PE = st.selectbox(label="PE Name*",options=senarai_PE,index=None)
    IPCterbakar = st.number_input(label="IPC Kesan Bakar",step=1,min_value=0)

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Defect")


