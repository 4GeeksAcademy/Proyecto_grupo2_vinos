from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

# Configuración de Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin abrir navegador
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-quic")
chrome_options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")

# Inicializar WebDriver con WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)  # Inicializar WebDriverWait

# Leer URLs desde el archivo .txt
with open('pruebavino00.txt', 'r') as file:
    urls_list = [line.strip() for line in file.readlines()]

# Lista para almacenar datos de los vinos
wine_data = []

# Recorrer cada URL de búsqueda en Vivino
for original_url in urls_list:
    print(f"Procesando URL: {original_url}")

    try:
        # Abrir URL en el navegador
        driver.get(original_url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Scroll progresivo hasta que no haya más vinos
        previous_count = 0
        for _ in range(10):  # Intentar 10 ciclos de carga
            driver.execute_script("window.scrollBy(0, 800);")  # Scroll suave
            time.sleep(2)  # Esperar para que se carguen más vinos
            wine_elements = driver.find_elements(By.CSS_SELECTOR, 'a.wineCard__image--3x8ul')

            if len(wine_elements) == previous_count:
                break  # Si no hay nuevos vinos, salir del bucle
            previous_count = len(wine_elements)

        # Extraer enlaces de los vinos
        wine_links = [wine.get_attribute('href') for wine in wine_elements if wine.get_attribute('href')]

        # Expresión regular para extraer la ID del vino desde la URL
        wine_id_pattern = re.compile(r"(\d+)$")

        # Recorrer cada vino y extraer información
        for link in wine_links:
            driver.get(link)
            time.sleep(2)  # Esperar carga de la página
            
            try:
                # Extraer la ID del vino desde la URL
                wine_id_match = wine_id_pattern.search(link)
                wine_id = wine_id_match.group(1) if wine_id_match else "N/A"

                # Esperar a que aparezcan las notas de sabor
                taste_sections = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2")))

                # Extraer texto de cada columna (si hay menos de 3, llenar con "N/A")
                taste_notes = [section.text for section in taste_sections[:3]]
                while len(taste_notes) < 3:
                    taste_notes.append("N/A")

                # Agregar a la lista de datos
                wine_data.append([wine_id, link] + taste_notes)

            except Exception as e:
                print(f"Error al extraer datos del vino {link}: {e}")
                wine_data.append(["N/A", link, "N/A", "N/A", "N/A"])

    except Exception as e:
        print(f"Error al procesar la URL {original_url}: {e}")

# Guardar en CSV
df = pd.DataFrame(wine_data, columns=["ID", "URL", "Columna 1", "Columna 2", "Columna 3"])
df.to_csv("vivino_tasting_notes.csv", index=False, encoding="utf-8")

print("Extracción finalizada. Datos guardados en vivino_tasting_notes.csv")

# Cerrar Selenium
driver.quit()
