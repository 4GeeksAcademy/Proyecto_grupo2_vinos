#CARACTERISTICAS VINOS
# URL de la página de Vivino



import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.service import Service



def get_sabor_vino2 (url, driver,soup):

      
# Navegar a la página
    driver.get(url)
    values=[]
# Mapeo de etiquetas y las clases de las barras de progreso
    labels = ["Ligero/Poderoso", "Suave/Tánico", "Seco/Dulce", "Débil/Ácido","Amable/Con burbujas"]
    # Buscar el elemento por clase
    element = soup.find('a', class_='breadCrumbs__link--1TY6b')

# Extraer y mostrar el texto
    if element:
        print(element.text)  # Esto imprimirá "Vino espumoso"
    else:
        print("Elemento no encontrado")
    # Diccionario para guardar los resultados
    progress_values = {}

    try:
        # Buscar todas las barras de progreso
        progress_elements = driver.find_elements(By.CLASS_NAME, 'indicatorBar__progress--3aXLX')
        
        # Asegurarnos de que tenemos el mismo número de barras de progreso que etiquetas
        if len(progress_elements) == len(labels):
            # Iterar sobre las barras de progreso y asignarles las etiquetas correspondientes
            for i, element in enumerate(progress_elements):
                left_value = element.get_attribute('style').split('left: ')[1].split('%')[0] if 'left' in element.get_attribute('style') else None
            
                
                if left_value:
                    # Convertir a float y convertirlo en una nota del 1 al 10 (dividiendo entre 10)
                    value = round(float(left_value) / 10,1)
                    # Asignar la etiqueta correspondiente
                    progress_values[labels[i]] = value
                    print(f"{labels[i]}: {value}")
                    values.append(value)
                else:
                    print(f"No se encontró el atributo 'left' para {labels[i]}.")
        else:
            print("El número de barras de progreso no coincide con el número de etiquetas esperadas.")
        
    except Exception as e:
        print(f"Error durante la extracción: {e}")

    return()
  



   

