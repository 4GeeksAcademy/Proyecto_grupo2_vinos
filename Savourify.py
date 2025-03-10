from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Crear un objeto Service con el chromedriver proporcionado por ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Iniciar el driver de Chrome usando el objeto Service
driver = webdriver.Chrome(service=service)

# Leer las URLs desde el archivo de texto
with open("vinos espumosos de 40 a 100.txt", "r") as file:
    urls = file.readlines()
urls = [url.strip() for url in urls]  # Limpiar los saltos de línea

data = []

# Función para hacer scroll
def scroll_page():
    # Hacer scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Esperar a que carguen más elementos

# Recorrer cada URL
for index, url in enumerate(urls, start=1):
    driver.get(url)
    time.sleep(5)  # Esperar a que la página cargue

    # Hacer scroll hasta el final de la página
    scroll_page()

    # Extraer el ID del vino
    wine_id = url.split("/")[-1]
    print(f"Revisando vino {index}/{len(urls)}: {wine_id}")

    try:
        # Esperar a que el elemento de notas de sabor esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2"))
        )

        # Extraer las notas de sabor
        taste_notes_elements = driver.find_elements(By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2")
        taste_notes = [el.text.strip() for el in taste_notes_elements if el.text.strip()]

        # Mostrar las notas de sabor que está extrayendo
        print(f"Notas de sabor para {wine_id}: {taste_notes}")

        # Dividir las notas de sabor por comas y guardarlas en campos separados
        taste_notes_dict = {}
        for i, note in enumerate(taste_notes):
            # Separar por comas
            separated_notes = note.split(",")
            for j, separated_note in enumerate(separated_notes):
                taste_notes_dict[f"Taste_Notes_{i+1}_{j+1}"] = separated_note.strip()

        # Asegurarse de que haya un campo para cada nota de sabor, hasta un máximo de 3
        for i in range(len(taste_notes), 3):  # Asumiendo que el máximo es 3 notas
            taste_notes_dict[f"Taste_Notes_{i+1}_1"] = "No disponible"

    except Exception as e:
        print(f"Error al extraer las notas de sabor de {wine_id}: {e}")
        taste_notes_dict = {"Taste_Notes_1_1": "No disponible"}

    # Guardar en la lista
    data.append({"Wine_ID": wine_id, **taste_notes_dict})

   

# Al finalizar, guardar el resto de los datos si hay menos de 25 vinos al final
if data:
    df = pd.DataFrame(data)
    df.to_csv("espumosos40a100.csv", index=False)
    print("Datos finales guardados en vivino_wines_final.csv")

# Cerrar el driver
driver.quit()

print("Proceso completado.")

