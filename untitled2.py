#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np



#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/CalistroAguilar24/PRUEBA/main/fallecidos_covid%20(3).csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='FECHA_CORTE', y='EDAD_DECLARADA')
