import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import random
from PIL import Image
import requests
from io import BytesIO

# Cargar la imagen desde la URL
url = "https://ebootcamp.net/wp-content/uploads/2021/11/4Geeks-Academy.jpeg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Redimensionar la imagen
img = img.resize((100, 100))

# Cargar frases desde el archivo
def cargar_frases():
    try:
        with open("frases.txt", "r", encoding="utf-8") as file:
            frases = file.readlines()
        return [frase.strip() for frase in frases if frase.strip()]
    except FileNotFoundError:
        return ["No se encontraron frases sobre vino."]

frases = cargar_frases()

if "mostrar_analisis" not in st.session_state:
    st.session_state.mostrar_analisis = False

# Inicializar una frase aleatoria en session_state
if "frase_actual" not in st.session_state:
    st.session_state.frase_actual = random.choice(frases)

# Función para cambiar la frase
def cambiar_frase():
    st.session_state.frase_actual = random.choice(frases)

#Config de la página
st.set_page_config(
    page_title="Dashboard sobre vino mundial",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Sidebar como menú lateral
with st.sidebar:
    st.image("images/wine_background.jpg", use_container_width=True)
    st.title("Menú")
    
    # Botón para abrir el panel de Trello en una nueva ventana
    if st.button("Inicio", key="inicio"):
        st.write("Bienvenido a la página de inicio")
        cambiar_frase()
          
    if st.button("Análisis de Datos", key="analisis"):
        st.write("Aquí va el análisis exploratorio")
        st.session_state.mostrar_analisis = True  # Cambia el estado para mostrar el análisis
        cambiar_frase()
                
        # Desplegable para opciones de análisis
        option = st.selectbox(
            "Selecciona una opción:",
            ("Zona de vinos más valorada", 
             "Tipo de Uva más apreciada", 
             "Dónde se encuentran los vinos más caros", 
             )
        )
        
        # Mostrar información según la opción seleccionada
        if option == "Zona de vinos más valorada":
            st.write("Aquí se mostrará información sobre la zona de vinos más valorada.")
        elif option == "Tipo de Uva más apreciada":
            st.write("Aquí se mostrará información sobre el tipo de uva más apreciada.")
        elif option == "Dónde se encuentran los vinos más caros":
            st.write("Aquí se mostrará información sobre dónde se encuentran los vinos más caros.")
    
    if st.button("Predicción de Vinos", key="prediccion"):
        st.write("Creando el negocio perfecto")
        cambiar_frase()
    
        option = st.selectbox(
            "Selecciona una opción:",
            ("Zona mas valorada para vinos", 
             "Tipo de vino mas valorado", 
             "Notas de sabor mas valoradas", 
             "La Bodega Perfecta")
        )
        # Mostrar información según la opción seleccionada
        if option == "Zona de vinos más valorada":
            st.write("Aquí se mostrará información sobre la zona de vinos más valorada.")
        elif option == "Tipo de vino más apreciado":
            st.write("Aquí se mostrará información sobre el tipo de vino más apreciado.")
        elif option == "Notas de sabor más apreciadas":
            st.write("Aquí se mostrará información sobre las notas de sabor más apreciadas.")
        elif option == "La Bodega Perfecta":
            st.write("Aquí se mostrará información sobre la bodega perfecta.")

    if st.button("Aconsejador de vino", key="aconsejador"):
        st.write("Conocemos el vino que quieres")
        cambiar_frase()
    
        option = st.selectbox(
            "Selecciona una opción:",
            ("Características de tu vino perfecto", 
             "Sabores de tu vino perfecto", 
             "Vinos similares",
             "Maridaje"
            )
        )
        # Mostrar información según la opción seleccionada
        if option == "Características de tu vino perfecto":
            st.write("Suave, tánico, dulce, ácido")
        elif option == "Sabores de tu vino perfecto":
            st.write("En base a tres campos con notas de sabor")
        elif option == "Vinos similares":
            st.write("Dinos un vino y te recomendamos otros similares (Input)")
        elif option == "Maridaje":
            st.write("Dinos una comida y te recomendamos vinos")

    if st.button("Modelo de prediccion", key="modelo"):
        st.write("El vino del futuro")
        cambiar_frase()

        option = st.selectbox(
            "Selecciona una opción:",
            ("Valorador de vino", 
             "El vino perfecto", 
            )
        )
        if option == "Valorador de vino":
            st.write("Asignar valoración en base a inputs")
        elif option == "El vino perfecto":
            st.write("Predicción de vino valoración perfecta")

    if st.button("Panel de Trello", key="trello"):
        js = "window.open('https://trello.com/b/SknN5szU/proyecto-data-science-4geeks', '_blank')"
        st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)
    if st.button("Repositorio del Proyecto", key="repositorio"):
        js = "window.open('https://github.com/4GeeksAcademy/Proyecto_grupo2_vinos', '_blank')"
        st.markdown(f'<script>{js}</script>', unsafe_allow_html=True)

    
# Cargar la fuente Playball desde Google Fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playball&display=swap');
        @import url('https://fonts.googleapis.com/css?family=Tangerine&display=swap'');
                
        body {
            background-color: #9e2a2f;  /* Burdeos suave */
            font-family: 'Arial', sans-serif; /* Fuente general */
            background-size: cover;     /* Asegura que cubra toda la ventana */
            background-position: center; /* Centra el fondo */
            background-attachment: fixed; /* Hace que el fondo se quede fijo al desplazarse */
        }
        
        .header {
            width: 1024px; /* Ancho del encabezado */
            height: 768px; /* Alto del encabezado */
            background-color: #800000; /* Color de fondo */
            border-radius: 15px; /* Bordes redondeados */
            margin: 20px auto; /* Centrar el encabezado */
            padding: 20px; /* Espaciado interno */
            text-align: center; /* Centrar el texto */
        }
        .frase {
            font-family: 'Tangerine', cursive;
            font-size: 24px;
            color: white;
            margin-top: 20px;
        }
        .button {
            background-color: #b1dbde; /* Color de fondo del botón */
            color: #800000; /* Color del texto del botón */
            border: none; /* Sin borde */
            border-radius: 5px; /* Bordes redondeados */
            padding: 10px 20px; /* Espaciado interno */
            cursor: pointer; /* Cambiar cursor al pasar el mouse */
            transition: background-color 0.3s ease; /* Transición suave */
        }

        .button:hover {
            background-color: #800000; /* Color al pasar el mouse */
            color: white; /* Color del texto al pasar el mouse */
        }

        .hidden {
            opacity: 0; /* Cambiar a opacidad 0 */
        }

        /* Asegura que el contenido no sea cubierto */
        .main {
            z-index: 9999;
        }
    </style>
""", unsafe_allow_html=True)


# Contenido principal

# Mostrar encabezado con imagen y título
header_html = f"""
    <div style="text-align: center; background-color: #800000; padding: 20px; border-radius: 15px; margin: 20px;">
        <img src="{url}" width="100" height="100" style="display: block; float: right;">
        <p style="font-family: 'Playball', cursive; font-size: 35px; color: #b1dbde;">
            Proyecto de Data Science - 4Geeks <br> Analítica sobre vinos
        </p>   <p class="frase">{st.session_state.frase_actual}</p>            
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# Contenido principal
st.markdown('<div class="main">', unsafe_allow_html=True)

# Script para animar la transición de la frase
st.markdown("""
    <script>
        const fraseDiv = document.getElementById('frase');
        fraseDiv.classList.add('hidden'); // Iniciar con opacidad 0
        setTimeout(() => {
            fraseDiv.classList.remove('hidden'); // Cambiar a opacidad 1 después de un breve retraso
        }, 100); // Tiempo de espera antes de mostrar la nueva frase
    </script>
""", unsafe_allow_html=True)  

st.markdown('</div>', unsafe_allow_html=True)