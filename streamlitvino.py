import streamlit as st 
import pandas as pd 
import plotly.express as px
import altair as alt
import random
from PIL import Image
import requests
from io import BytesIO
import plotly.colors as pc
import matplotlib.pyplot as plt
import seaborn as sns

country_mapping = {
        "Italia": "Italy",
        "Austria": "Austria",
        "España": "Spain",
        "Francia": "France",
        "Alemania": "Germany",
        "Sudáfrica": "South Africa",
        "Eslovenia": "Slovenia",
        "Australia": "Australia",
        "Portugal": "Portugal",
        "Argentina": "Argentina",
        "Hungría": "Hungary",
        "Grecia": "Greece",
        "New Zealand": "New Zealand",
        "Estados Unidos": "United States",
        "Chile": "Chile",
        "Croacia": "Croatia",
        "Rumanía": "Romania",
        "Bulgaria": "Bulgaria",
        "Marruecos": "Morocco",
        "Perú": "Peru",
        "Brasil": "Brazil",
        "Líbano": "Lebanon",
        "Luxembourg": "Luxembourg",
        "Suiza": "Switzerland",
        "Japón": "Japan",
        "Georgia": "Georgia",
        "Armenia": "Armenia",
        "Ucrania": "Ukraine",
        "México": "Mexico",
        "Reino Unido": "United Kingdom",
        "Israel": "Israel",
        "República Checa": "Czech Republic",
        "Países Bajos": "Netherlands",
        "Bélgica": "Belgium",
        "Canadá": "Canada",
        "Chipre": "Cyprus",
        "Norte de Macedonia": "North Macedonia",
        "Polonia": "Poland",
        "Serbia": "Serbia",
        "Eslovaquia": "Slovakia",
        "Uruguay": "Uruguay",
        "China": "China",
        "Moldavia": "Moldova",
        "Dinamarca": "Denmark",
        "Albania": "Albania",
        "Afganistán": "Afghanistan",
        "Albania": "Albania",
        "Algeria": "Algeria",
        "Andorra": "Andorra",
        "Angola": "Angola",
        "Antigua y Barbuda": "Antigua and Barbuda",
        "Arabia Saudita": "Saudi Arabia",
        "Argentina": "Argentina",
        "Armenia": "Armenia",
        "Australia": "Australia",
        "Austria": "Austria",
        "Azerbaiyán": "Azerbaijan",
        "Bahamas": "Bahamas",
        "Baréin": "Bahrain",
        "Bangladés": "Bangladesh",
        "Barbados": "Barbados",
        "Bélgica": "Belgium",
        "Belice": "Belize",
        "Benín": "Benin",
        "Bhután": "Bhutan",
        "Bielorrusia": "Belarus",
        "Birmania": "Myanmar",
        "Botsuana": "Botswana",
        "Brasil": "Brazil",
        "Brunéi": "Brunei",
        "Bulgaria": "Bulgaria",
        "Burkina Faso": "Burkina Faso",
        "Burundi": "Burundi",
        "Bután": "Bhutan",
        "Cabo Verde": "Cape Verde",
        "Camboya": "Cambodia",
        "Camerún": "Cameroon",
        "Canadá": "Canada",
        "Catar": "Qatar",
        "Chad": "Chad",
        "Chile": "Chile",
        "China": "China",
        "Chipre": "Cyprus",
        "Colombia": "Colombia",
        "Comoras": "Comoros",
        "Congo": "Congo",
        "Corea del Norte": "North Korea",
        "Corea del Sur": "South Korea",
        "Costa Rica": "Costa Rica",
        "Croacia": "Croatia",
        "Cuba": "Cuba",
        "Curazao": "Curaçao",
        "Chipre": "Cyprus",
        "República Checa": "Czech Republic",
        "Côte d'Ivoire": "Ivory Coast",
        "Dinamarca": "Denmark",
        "Djibouti": "Djibouti",
        "Dominica": "Dominica",
        "República Dominicana": "Dominican Republic",
        "Ecuador": "Ecuador",
        "Egipto": "Egypt",
        "El Salvador": "El Salvador",
        "Emiratos Árabes Unidos": "United Arab Emirates",
        "Ecuador": "Ecuador",
        "Eslovaquia": "Slovakia",
        "Eslovenia": "Slovenia",
        "España": "Spain",
        "Estados Unidos": "United States",
        "Etiopía": "Ethiopia",
        "Fiyi": "Fiji",
        "Filipinas": "Philippines",
        "Finlandia": "Finland",
        "Francia": "France",
        "Gabon": "Gabon",
        "Gambia": "Gambia",
        "Georgia": "Georgia",
        "Ghana": "Ghana",
        "Granada": "Grenada",
        "Grecia": "Greece",
        "Guatemala": "Guatemala",
        "Guinea": "Guinea",
        "Guinea-Bisáu": "Guinea-Bissau",
        "Guyana": "Guyana",
        "Haití": "Haiti",
        "Honduras": "Honduras",
        "Hungría": "Hungary",
        "India": "India",
        "Indonesia": "Indonesia",
        "Irak": "Iraq",
        "Irlanda": "Ireland",
        "Isla de Man": "Isle of Man",
        "Islas Cook": "Cook Islands",
        "Islas Feroe": "Faroe Islands",
        "Islas Malvinas": "Falkland Islands",
        "Islandia": "Iceland",
        "Israel": "Israel",
        "Italia": "Italy",
        "Jamaica": "Jamaica",
        "Japón": "Japan",
        "Jordania": "Jordan",
        "Kazajistán": "Kazakhstan",
        "Kenia": "Kenya",
        "Kirguistán": "Kyrgyzstan",
        "Kiribati": "Kiribati",
        "Kuwait": "Kuwait",
        "Laos": "Laos",
        "Lesoto": "Lesotho",
        "Letonia": "Latvia",
        "Líbano": "Lebanon",
        "Liberia": "Liberia",
        "Libia": "Libya",
        "Liechtenstein": "Liechtenstein",
        "Lituania": "Lithuania",
        "Luxemburgo": "Luxembourg",
        "Madagascar": "Madagascar",
        "Malasia": "Malaysia",
        "Malaui": "Malawi",
        "Maldivas": "Maldives",
        "Malta": "Malta",
        "Marruecos": "Morocco",
        "Mauricio": "Mauritius",
        "Mauritania": "Mauritania",
        "México": "Mexico",
        "Micronesia": "Micronesia",
        "Mónaco": "Monaco",
        "Mongolia": "Mongolia",
        "Mozambique": "Mozambique",
        "Namibia": "Namibia",
        "Nauru": "Nauru",
        "Nepal": "Nepal",
        "Nicaragua": "Nicaragua",
        "Níger": "Niger",
        "Nigeria": "Nigeria",
        "Noruega": "Norway",
        "Nueva Zelanda": "New Zealand",
        "Omán": "Oman",
        "Países Bajos": "Netherlands",
        "Pakistán": "Pakistan",
        "Palau": "Palau",
        "Panamá": "Panama",
        "Papúa Nueva Guinea": "Papua New Guinea",
        "Paraguay": "Paraguay",
        "Perú": "Peru",
        "Polonia": "Poland",
        "Portugal": "Portugal",
        "Reino Unido": "United Kingdom",
        "República Checa": "Czech Republic",
        "Rumanía": "Romania",
        "Rusia": "Russia",
        "Ruanda": "Rwanda",
        "Sahara Occidental": "Western Sahara",
        "Samoa": "Samoa",
        "San Cristóbal y Nieves": "Saint Kitts and Nevis",
        "San Marino": "San Marino",
        "Santa Lucía": "Saint Lucia",
        "Senegal": "Senegal",
        "Serbia": "Serbia",
        "Seychelles": "Seychelles",
        "Sierra Leona": "Sierra Leone",
        "Singapur": "Singapore",
        "Siria": "Syria",
        "Somalia": "Somalia",
        "Sri Lanka": "Sri Lanka",
        "Suazilandia": "Eswatini",
        "Sudán": "Sudan",
        "Sudáfrica": "South Africa",
        "Suecia": "Sweden",
        "Suiza": "Switzerland",
        "Surinam": "Suriname",
        "Siria": "Syria",
        "Somalia": "Somalia",
        "Sri Lanka": "Sri Lanka",
        "Tailandia": "Thailand",
        "Tanzania": "Tanzania",
        "Togo": "Togo",
        "Trinidad y Tobago": "Trinidad and Tobago",
        "Túnez": "Tunisia",
        "Turkmenistán": "Turkmenistan",
        "Turquía": "Turkey",
        "Tuvalu": "Tuvalu",
        "Uganda": "Uganda",
        "Ucrania": "Ukraine",
        "Uruguay": "Uruguay",
        "Uzbekistán": "Uzbekistan",
        "Vanuatu": "Vanuatu",
        "Vaticano": "Vatican",
        "Venezuela": "Venezuela",
        "Vietnam": "Vietnam",
        "Yemen": "Yemen",
        "Zambia": "Zambia",
        "Zimbabue": "Zimbabwe"
    }

st.set_page_config(
    page_title="Dashboard sobre vino mundial",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

def pagina_principal():
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
    # Cargar la imagen desde la URL
    url = "https://ebootcamp.net/wp-content/uploads/2021/11/4Geeks-Academy.jpeg"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

# Redimensionar la imagen
    img = img.resize((100, 100))
    header_html = f"""
    <div style="text-align: center; background-color: #800000; padding: 20px; border-radius: 15px; margin: 20px;">
        <img src="{url}" width="100" height="100" style="display: block; float: right;">
        <p style="font-family: 'Playball', cursive; font-size: 35px; color: #b1dbde;">
            Proyecto de Data Science - 4Geeks <br> Analítica sobre vino mundial
        </p>   <p class="frase">{st.session_state.frase_actual}</p>            
    </div>
"""
    st.markdown(header_html, unsafe_allow_html=True)
 
    st.markdown(
            """
            <style>
            .styled-table {
                width: 50%;
                margin: auto;
                border-collapse: collapse;
            }
            .styled-table th {
                background-color: #800000;
                color: white;
                text-align: center;
                font-size: 20px;
                padding: 10px;
            }
            .styled-table td {
                text-align: center;
                padding: 8px;
                font-size: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    integrantes = pd.DataFrame({
            "Integrantes": ["Pauline Charvin", "Jose María Tudela", "Vicente Polo"]
        })

    st.markdown("<table class='styled-table'><tr><th>Nuestro proyecto de Data Science</th></tr>" +
                    "".join(f"<tr><td>{nombre}</td></tr>" for nombre in integrantes["Integrantes"]) +
                    "</table>", unsafe_allow_html=True)

    st.write("")

        # Segunda tabla con tecnologías usadas
    tecnologias = pd.DataFrame({
            "Tecnología": ["Tamaño del Dataset", "Uso de Web Scraping", "Integridad de datos"],
            "Descripción": ["32,000 vinos (espumosos, blancos, tintos)",
                            "BeautifulSoup y Selenium",
                            "NLP y KNN"]
        })

    st.markdown("### Tecnologías utilizadas")
    st.table(tecnologias.set_index("Tecnología")) 

    librerias = pd.DataFrame({
    "Librería": [
        "Streamlit", 
        "Pandas", 
        "Plotly Express", 
        "Altair", 
        "Random", 
        "PIL (Pillow)", 
        "Requests", 
        "BytesIO", 
        "Plotly Colors", 
        "Matplotlib", 
        "Seaborn"
    ],
    "Descripción": [
        "Framework para crear aplicaciones web interactivas.",
        "Librería para manejo y análisis de datos en estructuras tabulares.",
        "Librería para crear gráficos interactivos y visualizaciones.",
        "Librería para crear gráficos declarativos.",
        "Genera números aleatorios y realiza selecciones al azar.",
        "Librería para abrir, manipular y guardar imágenes.",
        "Permite hacer peticiones HTTP y obtener datos de la web.",
        "Módulo para trabajar con flujos de datos binarios (como imágenes).",
        "Proporciona una paleta de colores para visualizaciones en Plotly.",
        "Librería para la creación de gráficos estáticos.",
        "Librería para visualización de datos estadísticos y gráficos atractivos."
    ]
})

# Mostrar el título
    st.markdown("### Librerías utilizadas")
    st.table(librerias.set_index("Librería"))

def eda_1():
    st.title("📊 Primera parte del EDA")

    # Crear el desplegable para seleccionar el tipo de vino
    vino_tipo = st.selectbox(
        "Selecciona el tipo de vino",
        ("Vino Tinto", "Vino Blanco", "Vino Espumoso")
    )

# Definir las rutas de los archivos CSV según el tipo de vino seleccionado
    if vino_tipo == "Vino Tinto":
        archivo_csv = "https://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/tintos/BF_tintos_1to150_clean"  # Cambia la ruta a la correcta
    elif vino_tipo == "Vino Blanco":
        archivo_csv = "http://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/blancos/CLEAN_DF_BF_blancos"  # Cambia la ruta a la correcta
    else:
        archivo_csv = "https://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/espumosos/espumosos%20test.ipynb"  # Cambia la ruta a la correcta

# Cargar el CSV seleccionado en el DataFrame df
    df = pd.read_csv(archivo_csv)    
 

    df["País"] = df["País"].replace(country_mapping)

    # Grouping data by number of wines
    df_grouped_1 = df.groupby("País")["ID"].nunique().reset_index(name="num_vinos")
    
    # Columna para el gráfico
    col1, col2 = st.columns([2, 2])  # Controlamos el tamaño de las columnas
    
    with col1:
        st.subheader("Distribución de vinos por país")
        country_count = df['País'].value_counts().reset_index()
        country_count.columns = ['País', 'Cantidad']
        total_vinos = country_count['Cantidad'].sum()
        country_count['Porcentaje'] = (country_count['Cantidad'] / total_vinos) * 100
        
        pie_chart = alt.Chart(country_count).mark_arc().encode(
            theta='Cantidad:Q',  # El tamaño de cada sección
            color=alt.Color('País:N', legend=None),  # Color por país
            tooltip=['País:N', 'Cantidad:Q', 'Porcentaje:Q'],  # Mostrar el país, la cantidad y el porcentaje en el tooltip
            text=alt.Text('Porcentaje:Q', format='.1f')  # Mostrar el porcentaje en cada sección
        ).properties(width=350, height=300)  # Ajusta el tamaño del gráfico

        pie_chart = pie_chart.configure_mark(
            fontSize=14,  # Tamaño de la fuente
            fontWeight='bold'
        )
        st.altair_chart(pie_chart, use_container_width=True)

    with col2:
        # Columna para la tabla
        st.subheader("🔝 Top 10 países con más vinos registrados")
        # Top 10 países con más vinos
        df_top_10 = df_grouped_1.sort_values(by="num_vinos", ascending=False).head(10)
        st.table(df_top_10.set_index("País"))
        pass


    # Agrupar los datos por país y bodega, contando el número de vinos por combinación
    df_grouped_1 = df.groupby(["País", "Bodega"])["ID"].nunique().reset_index(name="num_vinos")

    # Crear las columnas para el layout
    col1, col2 = st.columns([2, 2])  # Controlamos el tamaño de las columnas

    country_bodega_count = df.groupby(["País", "Bodega"])["ID"].nunique().reset_index(name="Cantidad")
    total_vinos = country_bodega_count['Cantidad'].sum()
    country_bodega_count['Porcentaje'] = (country_bodega_count['Cantidad'] / total_vinos) * 100

    with col1:
        country_bodega_count_grouped = country_bodega_count.groupby("País")["Cantidad"].count().reset_index(name="num_bodegas")
        countries_with_more_than_20_bodegas = country_bodega_count_grouped[country_bodega_count_grouped['num_bodegas'] > 20]['País']
        filtered_data = country_bodega_count[country_bodega_count['País'].isin(countries_with_more_than_20_bodegas)]

        # Gráfico de barras apiladas
        bar_chart = alt.Chart(filtered_data).mark_bar().encode(
            x='Cantidad:Q',  # Longitud de las barras
            y=alt.Y('País:N', sort='-x'),  # Países, ordenados por la cantidad
            color=alt.Color('Bodega:N', legend=None),  # Colores por bodega sin leyenda
            tooltip=['País:N', 'Bodega:N', 'Cantidad:Q', 'Porcentaje:Q']  # Información mostrada al pasar el ratón
        ).properties(width=600, height=400)

        # Ajusta el diseño de la gráfica (opcional)
        bar_chart = bar_chart.configure_mark(
            fontSize=14,  # Tamaño de la fuente
            fontWeight='bold'
        )

        # Mostrar el gráfico en Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

        
    with col2:
        # Columna para la tabla
        st.subheader("🔝 Top 10 combinaciones de país y bodega con más vinos registrados")
        
        # Top 10 combinaciones de país y bodega con más vinos
        df_top_10 = df_grouped_1.sort_values(by="num_vinos", ascending=False).head(10)
        st.table(df_top_10.set_index(["País", "Bodega"]))

    
    # Primero, agrupar los datos y calcular el número de bodegas por país
    df_grouped_1 = df.groupby("País")["Bodega"].nunique().reset_index(name="num_bodegas")

    # Obtener los 10 países con más bodegas
    df_top_10 = df_grouped_1.sort_values(by="num_bodegas", ascending=False).head(10)

    # Crear las columnas para los gráficos
    col1, col2 = st.columns([2, 2])  # Controlamos el tamaño de las columnas
    
    # Graficar el Top 10 países con más bodegas registradas
    with col1: 
        fig = px.bar(df_top_10, 
                    x='País', 
                    y='num_bodegas', 
                    color='num_bodegas', 
                    title="🏢 Top 10 países con más bodegas registradas",
                    labels={'num_bodegas': 'Número de Bodegas', 'País': 'País'},
                    color_continuous_scale='Viridis')  # Puedes cambiar el color_continuous_scale a tu preferencia

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # Mostrar la tabla con los 10 países con más bodegas
    with col2: 
        st.subheader("🏢 Top 10 países con más bodegas registradas")
        st.table(df_top_10.set_index("País"))


    # Average wine rating per country
    df['Valoración'] = pd.to_numeric(df['Valoración'], errors='coerce')
    df_grouped_2 = df.groupby("País").agg(
    num_bodegas=('Bodega', 'nunique'),  # Contamos el número único de bodegas
    avg_valoracion=('Valoración', 'mean')  # Calculamos la valoración promedio
).reset_index()

    with col1: 
        fig4 = px.scatter(df_grouped_2, 
                        x="num_bodegas",  # Número de bodegas
                        y="avg_valoracion",  # Valoración promedio
                        color="avg_valoracion",  # Colorear según la valoración
                        hover_name="País",  # Muestra el país al pasar el ratón
                        title=f"Relación entre el Número de Bodegas y la Valoración Promedio de {vino_tipo}",
                        labels={'avg_valoracion': 'Valoración Promedio', 'num_bodegas': 'Número de Bodegas'},
                        color_continuous_scale="RdYlGn")  # Color según la valoración

        st.plotly_chart(fig4, use_container_width=True)

    # Top 10 países con mejor valoración promedio
    with col2:
        df_top_10_valoracion = df_grouped_2.sort_values(by="avg_valoracion", ascending=False).head(10)
        st.subheader("⭐ Top 10 países con la mejor valoración promedio de vinos")
        st.table(df_top_10_valoracion.set_index("País"))

    # Wine price by country
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
    df_grouped_3 = df.groupby("País")["Precio"].mean().reset_index(name="avg_precio")

    # Create the choropleth map for average price
    fig3 = px.choropleth(df_grouped_3, 
                        locations="País",  
                        locationmode="country names",  
                        color="avg_precio",  
                        hover_name="País",  
                        color_continuous_scale="Viridis",  
                        labels={"avg_precio": "Precio Promedio"})  

    # Adjust map layout
    fig3.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
    fig3.update_layout(title=f"Precio Promedio de {vino_tipo} por País", geo=dict(showframe=False, projection_type="natural earth"))

    # Display the map in Streamlit
    st.plotly_chart(fig3, use_container_width=True)

    # Top 10 countries with the highest average price
    df_top_10_precio = df_grouped_3.sort_values(by="avg_precio", ascending=False).head(10)
    st.subheader(f"💰 Top 10 países con mayor precio promedio de {vino_tipo}")
    st.table(df_top_10_precio.set_index("País"))
 

def bodega_perfecta():

    st.title("Datos para una bodega perfecta")
    
    # Crear el desplegable para seleccionar el tipo de vino
    # Crear el desplegable para seleccionar el tipo de vino
    vino_tipo = st.selectbox(
        "Selecciona el tipo de vino",
        ("Vino Tinto", "Vino Blanco", "Vino Espumoso")
    )

# Definir las rutas de los archivos CSV según el tipo de vino seleccionado
    if vino_tipo == "Vino Tinto":
        archivo_csv = "https://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/tintos/BF_tintos_1to150_clean"  # Cambia la ruta a la correcta
    elif vino_tipo == "Vino Blanco":
        archivo_csv = "http://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/blancos/CLEAN_DF_BF_blancos"  # Cambia la ruta a la correcta
    else:
        archivo_csv = "https://raw.githubusercontent.com/4GeeksAcademy/Proyecto_grupo2_vinos/refs/heads/pauline/espumosos/espumosos%20test.ipynb"  # Cambia la ruta a la correcta

    # Cargar el CSV seleccionado en el DataFrame df
    df = pd.read_csv(archivo_csv)

    # Crear columnas
    tab1, tab2 = st.columns(2)

    # Gráfico 1: Heatmap
    with tab1:
        st.subheader("Heatmap de Valoraciones")
        heatmap = alt.Chart(df).mark_rect().encode(
            x=alt.X('Año:O', title="Año"),
            y=alt.Y('País:O', title="País"),
            color=alt.Color('Valoración:Q', scale=alt.Scale(scheme='reds'))
        ).properties(width=400, height=300)
        st.altair_chart(heatmap, use_container_width=True)

    # Gráfico 2: Precio medio por tipo de uva
    with tab2:
        st.subheader("Precio medio por tipo de uva")
        bar_chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('mean(Precio):Q', title="Precio Medio"),
            y=alt.Y('Uva:N', title="Tipo de Uva", sort='-x'),
            color=alt.Color('Uva:N', legend=None)
        ).properties(width=400, height=300)
        st.altair_chart(bar_chart, use_container_width=True)

    # Gráfico 3: Proporción de vinos por país
    with tab1:
        st.subheader("Distribución de vinos por país")
        country_count = df['País'].value_counts().reset_index()
        country_count.columns = ['País', 'Cantidad']
        pie_chart = alt.Chart(country_count).mark_arc().encode(
            theta='Cantidad:Q',
            color=alt.Color('País:N', legend=None)
        ).properties(width=400, height=300)
        st.altair_chart(pie_chart, use_container_width=True)

def img_process():
    st.title("Subir y mostrar imagen")

    # Widget para subir la imagen
    uploaded_file = st.file_uploader("Sube una etiqueta de vino DE FRENTE", type=["png", "jpg", "jpeg"])

    # Si se sube una imagen, se muestra en pantalla
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        delantera = image.resize((200, 200))

        # Mostrar la imagen redimensionada y centrada
        st.image(delantera, caption="Etiqueta delantera de vino subida", use_container_width=False)
    
    uploaded_file = st.file_uploader("Sube una etiqueta de vino TRASERA", type=["png", "jpg", "jpeg"])

    # Si se sube una imagen, se muestra en pantalla
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        trasera = image.resize((200, 200))

        # Mostrar la imagen redimensionada y centrada
        st.image(trasera, caption="Etiqueta trasera de vino subida", use_container_width=False)

    precio = st.text_input("¿Cuál es el precio del vino?")

    # Mostrar el precio ingresado
    if precio:
        try:
            precio_float = float(precio)  # Convertir el precio a float
            st.write(f"El precio ingresado es: ${precio_float:.2f}")
        except ValueError:
            st.error("Por favor, ingresa un valor numérico válido para el precio.")
    

def recomendador_de_vinos():
    st.title("Recomendador de vinos")
    

st.sidebar.title("Navegación")
pagina= st.sidebar.selectbox("Selecciona una página", ["Página principal", "EDA 1", "Bodega Perfecta","Procesado de imagen", "Recomendador de vinos"])

if pagina == "Página principal":
    pagina_principal()
elif pagina == "EDA 1":
    eda_1()
elif pagina == "Bodega Perfecta":
    bodega_perfecta()
elif pagina == "Procesado de imagen":
    img_process()
elif pagina == "Recomendador de vinos":
    recomendador_de_vinos()