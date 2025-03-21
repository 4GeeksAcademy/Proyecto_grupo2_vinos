# Elige tu vino

## Descripción

Elige tu vino es un proyecto que, mediante técnicas de análisis de datos y machine learning, tiene como objetivo definir el "vino perfecto" para los usuarios. Se basa en miles de datos extraídos de la página web Vivino.es, los cuales hemos recolectado inicialmente mediante scraping. Utilizando técnicas como regresión, KNN y clustering, hemos implementado herramientas que complementan lo que ya ofrece esa plataforma, ayudando aún más a los usuarios en su búsqueda del vino ideal.

Las funcionalidades incluyen:

Datos relevantes e infografía sobre los vinos más destacados del mundo.
Recomendación de vinos más baratos similares a los que te gustan, pero que pueden ser un poco caros.
Predicción de la valoración de vinos que aún no están presentes en la web.
Este proyecto se realiza en el marco del bootcamp de Machine Learning de la 4GeekAcademy, llevado a cabo de noviembre de 2024 a marzo de 2025.

## Etapas del Proyecto


### 1. **Planificación : 9 horas **
En esta fase, se exploraron varias ideas y conceptos de proyectos. Después de un brainstorming, un análisis de factibilidad e interés del equipo, se definió el alcance y los objetivos del proyecto, identificando qué datos serían necesarios y cómo se utilizarían para entrenar los modelos. Además, se realizó un análisis preliminar sobre la página web Vivino.es para definir qué información sería esencial y cómo se almacenaría.

### 2. **Obtención de Datos (Scraping) : 3 semanas**

En esta etapa, se implementó el proceso de web scraping de la página Vivino.es para extraer miles de datos relacionados con vinos tintos, blancos y espumosos, tales como sus características (variedad, región, precio, valoración, notas de sabor, maridajes, etc.). Utilizamos Python y las siguientes librerías: Pandas, BeautifulSoup, Selenium (módulo WebDriver), expresiones regulares (Re), Time y OS. Se extrajeron datos de casi 32,000 vinos, los cuales formaron la base del análisis. La creación y extracción de esta información fue un proceso largo, ya que se extrajo primero la URL y luego la información dentro de cada página de vino, lo cual requirió un tiempo considerable de ejecución.

Finalmente, se realizó una primera limpieza de los datos: estructuración final y combinación de la información, tratamiento de valores duplicados, detección y reemplazo de texto incompleto.

### 3. **Análisis Exploratorio de Datos (EDA) : 1 semana**

Con los datos obtenidos, se realizó un análisis exploratorio (EDA) para entender las relaciones entre las distintas características de los vinos. Esto incluyó la visualización de datos y la identificación de patrones y tendencias. Se aplicaron técnicas más profundas de limpieza de datos, tratamiento de valores faltantes, creación de gráficos para la infografía y transformación de variables (encoding) para garantizar que los datos estuvieran listos para ser procesados por los modelos de machine learning.

### 4. **Desarrollo de Modelos Predictivos 2 semanas**
.....

### 5. **Desarollo de un Streamlit 1 semana**
.....

## Archivos y su Propósito

Aquí puedes describir brevemente qué hace cada archivo importante en el proyecto.


- **README.md**: Este archivo, donde se explica la estructura del proyecto y cómo trabajar con él.
- **webscraping.ipynb, conversor2.0.py, savourify**: Codigos desarollados para el scrapping de vivino.es
- **Archivo de dataframes**: Resultados finales despues del merge y la primera limpieza de los 3 dataframes de base : tintos, blancos y espumosos.
- **....**: ....

## Instalación

Pasos detallados sobre cómo instalar y configurar el proyecto en tu entorno local.

1. Enlace Streamlit :

Pagina principal 

Botones : 

- Datos de analisis : 
    - EDA gráficos generales : mapa del mundo (vinos x país, bodega x país, valoración promedio x país, precio prom x país)
    - EDA José Maria 
    - Datos interactivos : 

 

## Uso

Explicación de cómo usar el proyecto una vez que esté configurado.

1. Inicia la aplicación ...
