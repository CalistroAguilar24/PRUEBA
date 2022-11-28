#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

#@st.experimental_memo

with st.sidebar:
   st.sidebar.header('Programación avanzada')
   image = Image.open('Logo_Oficial (1).png')
   st.image(image,use_column_width=True)
   selected = option_menu(
      menu_title = 'Menú',
      options = ['Inicio','Informe','Equipo'],
      icons = ['house','book','people'],
      menu_icon = 'cast',
      default_index = 0,
   )
if selected == 'Inicio':
   st.markdown("<h1 style ='text-align: center'> Introducción:</h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.header("Los desastres naturales han acompañado el desarrollo de la humanidad a lo largo de la historia; por ello, rescatar y analizar a los sismos desde la historia ayuda a comprender no sólo las acciones humanas en torno a ellos, sino también a descifrar las características y patrones de comportamiento de la actividad sísmica, lo que puede ayudar a los sismólogos, geólogos y otros especialistas a elaborar con mayores datos y precisión, los mapas de riesgo.")
   st.header(" Además, tener conocimiento sobre estos fenómenos nos permitirá construir una sociedad preventiva, la vulnerabilidad física y la vulnerabilidad social nos ayudará a contar con herramientas –como simulacros y mochilas de emergencia– para estar preparados ante lo que podemos esperar en un evento real.")          
           

   def download_data():
      url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      filename="Catalogo1960_2021.xlsx"
      urllib.request.urlretrieve(url,filename)
      df=pd.read_csv('Catalogo1960_2021.xlsx')
      return df
   c=download_data()
   st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
   st.dataframe(c)
   st.subheader("Características del Dataset")
   st.write(c.describe())
   #url del archivo en formato raw
   url = 'https://raw.githubusercontent.com/brigytt/G_PROGRA/main/Catalogo1960_2021.csv'
   datos = pd.read_csv(url,sep= ',')
   st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')
   image = Image.open('imagen 1.jpg')
   st.image(image,use_column_width=True)
if selected == 'Informe':
   st.markdown("<h1 style ='text-align: center'> CATÁLOGO SÍSMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   selected_year=st.sidebar.selectbox('Fecha', list(reversed(range(1960,2021))))
   def download_data():
      url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      filename="Catalogo1960_2021.xlsx"
      urllib.request.urlretrieve(url,filename)
      df=pd.read_csv('Catalogo1960_2021.xlsx')
      filt=(df["FECHA_UTC"] == selected_year)
      df[filt]
   download_data()
if selected == 'Equipo':
   st.markdown("<h1 style ='text-align: center'> Integrantes:</h1>", unsafe_allow_html= True)
   st.markdown("---")
   col1, col2, col3, col4 = st.columns(4)
	image1 = Image.open('b9fd20744ad6f008787ffed46a0b7149--s-cartoons-bart-simpson.jpg')
	col1.header("Miguel Calistro")
	col1.image(image1, use_column_width=True)
	grayscale = image1.convert('LA')
	col2.image(grayscale, use_column_width=True)
	image2 = Image.open('273-2736237_20-lisa-simpson-tumblr-listening-to-headphones-pictures.png')
	col3.header("Brigytt Contreras")
	col3.image(image2, use_column_width=True)
	grayscale = image2.convert('LA')
	col4.image(grayscale, use_column_width=True)
   
   col5, col6 = st.columns(2)
	image5 = Image.open('mqdefault.jpg')
	col5.header("Daniel Chamorro")
	col5.image(image5, use_column_width=True)
	grayscale = image5.convert('LA')
	col6.image(grayscale, use_column_width=True)
	
   

 

