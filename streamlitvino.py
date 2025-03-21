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
            "Tecnología": ["Tamaño del DataFrame", "Uso de Web Scraping", "Integridad de datos"],
            "Descripción": ["32,000 vinos (espumosos, blancos, tintos)",
                            "BeautifulSoup y Selenium",
                            "NLP y KNN"]
        })

    st.markdown("### Tecnologías utilizadas")
    st.table(tecnologias.set_index("Tecnología")) 


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
#Lista de paises en ingles para usar plotly :
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
    df["País"] = df["País"].replace(country_mapping)

    # Grouping data by number of wines
    df_grouped_1 = df.groupby("País")["ID"].nunique().reset_index(name="num_vinos")
        
    # Create the choropleth map for the number of wines
    fig = px.choropleth(df_grouped_1, 
                        locations="País", 
                        locationmode="country names",  
                        color="num_vinos",  
                        hover_name="País",
                        color_continuous_scale=px.colors.sequential.Reds,  
                        labels={"num_vinos": f"Número de vinos {vino_tipo.lower()}s"})  # Dynamic title

    # Adjust map layout
    fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
    fig.update_layout(title=f"{vino_tipo} por País", geo=dict(showframe=False, projection_type="natural earth"))

    # Display the map in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Top 10 countries with the most wines
    df_top_10 = df_grouped_1.sort_values(by="num_vinos", ascending=False).head(10)
    st.subheader("🔝 Top 10 países con más vinos registrados")
    st.table(df_top_10.set_index("País"))

    # Number of wineries by country
    df_grouped_1 = df.groupby("País")["Bodega"].nunique().reset_index(name="num_bodegas")

    # Create the choropleth map for the number of wineries
    fig = px.choropleth(df_grouped_1, 
                        locations="País", 
                        locationmode="country names",  
                        color="num_bodegas",  
                        hover_name="País",
                        color_continuous_scale=px.colors.sequential.Reds,  
                        labels={"num_bodegas": f"Número de bodegas de {vino_tipo.lower()}s"})  # Dynamic title

    # Adjust map layout
    fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
    fig.update_layout(title=f"Distribución de Bodegas de {vino_tipo} por País", geo=dict(showframe=False, projection_type="natural earth"))

    # Display the map in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Top 10 countries with the most wineries
    df_top_10 = df_grouped_1.sort_values(by="num_bodegas", ascending=False).head(10)
    st.subheader("🏢 Top 10 países con más bodegas registradas")
    st.table(df_top_10.set_index("País"))

    # Average wine rating per country
    df['Valoración'] = pd.to_numeric(df['Valoración'], errors='coerce')
    df_grouped_2 = df.groupby("País")["Valoración"].mean().reset_index(name="avg_valoracion")

    # Create the choropleth map for average rating
    fig2 = px.choropleth(df_grouped_2, 
                        locations="País",  
                        locationmode="country names",  
                        color="avg_valoracion",  
                        hover_name="País",  
                        color_continuous_scale="RdYlGn",  
                        labels={"avg_valoracion": "Valoración Promedio"})  

    # Adjust map layout
    fig2.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
    fig2.update_layout(title=f"Valoración Promedio de {vino_tipo} por País", geo=dict(showframe=False, projection_type="natural earth"))

    # Display the map in Streamlit
    st.plotly_chart(fig2, use_container_width=True)

    # Top 10 countries with the best average rating
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




def eda_2():
    st.title("Visualizacion de los datos interactivos")
    st.write("Cargamos el DF (tendremos que pensar como hacer eso de manera automática)")
    df_interactivo= st.file_uploader("Elige el archivo CSV", type="csv", key="2")
    
    if df_interactivo is not None:
        df = pd.read_csv(df_interactivo) 
        st.write("Elige una columna para el eje X")
        eje_x= st.selectbox("Eje X", df.columns)
        st.write("Elige una columna para el eje Y")
        eje_y= st.selectbox("Eje Y", df.columns)
        
        if st.button("Visualizar gráfico"):
            fig= px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)
    

st.sidebar.title("Navegación")
pagina= st.sidebar.selectbox("Selecciona una página", ["Página principal", "EDA 1", "EDA 2","Bodega perfecta"])

if pagina == "Página principal":
    pagina_principal()
elif pagina == "EDA 1":
    eda_1()
elif pagina == "EDA 2":
    eda_2()

    