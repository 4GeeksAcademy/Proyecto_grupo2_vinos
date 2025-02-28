import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.service import Service



def get_sabor_vino (url, driver,soup):

      
# Navegar a la página
    driver.get(url)
    values=[]
# Mapeo de etiquetas y las clases de las barras de progreso
    labels_tinto = ["Ligero/Poderoso", "Suave/Tánico", "Seco/Dulce", "Débil/Ácido"]
    labels_blanco = ["Ligero/Poderoso", "Seco/Dulce", "Débil/Ácido"]
    Labels_espumoso = ["Ligero/Poderoso", "Débil/Ácido","Amable/Con burbujas"] 
    # Buscar el elemento por clase
    element = soup.find('a', class_='breadCrumbs__link--1TY6b', attrs={'data-cy': 'breadcrumb-winetype'})

# Extraer y mostrar el texto
    if element:
        if element.text == "Vino tinto":
            labels = labels_tinto
        elif element.text == "Vino blanco":
            labels = labels_blanco
        elif element.text == "Vino espumoso":
            labels = Labels_espumoso    
    else:
        print(f"Tipo de vino no reconocido: {element
            .text}")

    print(element.text)  # Esto imprimirá "Vino espumoso"
    
    # Diccionario para guardar los resultados
    progress_values = {}

    try:
        # Buscar todas las barras de progreso
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'indicatorBar__progress--3aXLX')))
        progress_elements = driver.find_elements(By.CLASS_NAME, 'indicatorBar__progress--3aXLX')
        print(f"Se encontraron {len(progress_elements)} barras de progreso") 
            
        # Asegurarnos de que tenemos el mismo número de barras de progreso que etiquetas
        if len(progress_elements) == len(labels):
            print((progress_elements))
            print((labels))
            # Iterar sobre las barras de progreso y asignarles las etiquetas correspondientes
            for i, element in enumerate(progress_elements):
                left_value = element.get_attribute('style').split('left: ')[1]
                if "%"  in left_value:
                    left_value = left_value.split('%')[0]
                else:
                    None
                
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