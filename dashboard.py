import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import random
from PIL import Image
import requests
from io import BytesIO
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Config de la página
st.set_page_config(
    page_title="Dashboard sobre vino mundial",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.title("Datos para una bodega perfecta")
       
    # Crear el desplegable para seleccionar el tipo de vino
vino_tipo = st.selectbox(
        "Selecciona el tipo de vino",
        ("Vino Tinto", "Vino Blanco", "Vino Espumoso")
        )

# Definir las rutas de los archivos CSV según el tipo de vino seleccionado
if vino_tipo == "Vino Tinto":
        archivo_csv = r'C:\Users\yiyip\OneDrive\Documents\GitHub\Proyecto_grupo2_vinos\csv\tintos.csv'  
elif vino_tipo == "Vino Blanco":
        archivo_csv = r"C:\Users\yiyip\OneDrive\Documents\GitHub\Proyecto_grupo2_vinos\csv\blancos.csv"  
else:
     archivo_csv = r"C:\Users\yiyip\OneDrive\Documents\GitHub\Proyecto_grupo2_vinos\csv\espumosos.csv"  

    # Cargar el CSV seleccionado en el DataFrame df
df = pd.read_csv(archivo_csv)

 # Separar las notas de cata en una lista
def extract_taste_notes(row):
    notes = []
    for col in ["Taste_Note_1", "Taste_Note_2", "Taste_Note_3"]:
        if pd.notna(row[col]):
            notes.extend(row[col].split(", "))
    return notes

df["All_Taste_Notes"] = df.apply(extract_taste_notes, axis=1)

taste_counter = Counter()
for notes in df["All_Taste_Notes"]:
    taste_counter.update(notes)

taste_df = pd.DataFrame(taste_counter.items(), columns=["Taste Note", "Count"])
taste_df = taste_df.sort_values(by="Count", ascending=False)

# 1. Gráfico de las notas de cata más valoradas
plt.figure(figsize=(10, 5))
sns.barplot(x=taste_df["Taste Note"].head(10), y=taste_df["Count"].head(10), palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Notas de Cata Más Frecuentes")
plt.show()

# 2. Correlación entre atributos y valoración
cols_numericas = ["Ligero/Poderoso", "Suave/Tánico", "Seco/Dulce", "Débil/Ácido", "Valoración"]
df[cols_numericas] = df[cols_numericas].replace("No disponible", np.nan).astype(float)
df_corr = df[cols_numericas].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(df_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlación entre Características Sensoriales y Valoración")
plt.show()

# 3. Relación entre tipo de uva y valoración
df_melted = df.melt(id_vars=["Valoración"], value_vars=["Uva 1", "Uva 2", "Uva 3", "Uva 4"], var_name="Uva Tipo", value_name="Uva")
plt.figure(figsize=(12, 6))
sns.boxplot(x="Uva", y="Valoración", data=df_melted, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Distribución de Valoración por Tipo de Uva")
plt.show()

# 4. Relación entre tipo de vino, precio y valoración
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Precio", y="Valoración", hue="Tipo de vino", data=df, palette="coolwarm", alpha=0.7)
plt.title("Relación entre Tipo de Vino, Precio y Valoración")
plt.legend(title="Tipo de vino")
plt.show()
