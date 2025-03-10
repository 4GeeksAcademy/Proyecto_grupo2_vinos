from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd  
import time
import os

# Configurar el WebDriver de Chrome con opciones avanzadas
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")  # Mejora estabilidad en algunos entornos
options.add_argument("--log-level=3")  # Reduce logs innecesarios
options.add_argument("--enable-logging")  # Activa logs para ver posibles fallos

driver = webdriver.Chrome(service=service, options=options)

# Leer las URLs desde el archivo
input_filename = "Vinos blancos de 9 a 11.txt"
output_basename = os.path.splitext(os.path.basename(input_filename))[0]  # "espumosos40a100"

start_index = 100  # Cambia este valor para elegir desde qué fila comenzar

with open(input_filename, "r", encoding="utf-8") as file:
    urls = [url.strip() for url in file.readlines() if url.strip().startswith("http")]

urls = urls[start_index:]  # Cortar la lista desde la fila deseada

data = []
file_count = 1  # Contador de archivos
batch_size = 100  # Cada cuántos registros se guarda

# Función para hacer scroll
def scroll_page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Esperar a que cargue más contenido

# Recorrer cada URL
for index, url in enumerate(urls, start=start_index + 1):
    if not url:
        print(f"⚠️ URL vacía en el índice {index}, saltando...")
        continue
    
    print(f"🔍 Accediendo a {url}")
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    except Exception as e:
        print(f"⚠️ No se pudo cargar la página {url}, saltando... Error: {e}")
        continue

    scroll_page()

    # Extraer el ID del vino desde la URL
    ID = url.split("/")[-1]
    print(f"🔍 Procesando vino {index}/{len(urls) + start_index}: {ID}")

    try:
        # Esperar a que aparezcan las notas de sabor
        taste_notes_elements = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2"))
        )
        
        # Extraer las notas de sabor
        taste_notes = [el.text.strip() for el in taste_notes_elements if el.text.strip()]
        print(f"✅ Notas de sabor para {ID}: {taste_notes}")

        # Dividir las notas de sabor por comas y guardarlas en campos separados
        taste_notes_dict = {}
        for i, note in enumerate(taste_notes):
            separated_notes = note.split(",")
            for j, separated_note in enumerate(separated_notes):
                taste_notes_dict[f"Taste_Notes_{i+1}_{j+1}"] = separated_note.strip()

        # Asegurarse de que haya un campo para cada nota de sabor, hasta un máximo de 3
        for i in range(len(taste_notes), 3):  # Asumiendo que el máximo es 3 notas
            taste_notes_dict[f"Taste_Notes_{i+1}_1"] = "No disponible"

    except Exception as e:
        print(f"⚠️ Error al extraer las notas de sabor de {ID}: {e}")
        taste_notes_dict = {"Taste_Notes_1_1": "No disponible"}

    # Guardar en la lista
    data.append({"ID": ID, **taste_notes_dict})

    # Guardar cada `batch_size` registros
    if len(data) >= batch_size:
        output_filename = f"{output_basename}_{file_count}.csv"
        df = pd.DataFrame(data)
        df.to_csv(output_filename, index=False, encoding="utf-8-sig")
        print(f"💾 Guardado {batch_size} registros en {output_filename}")
        data.clear()  # Vaciar la lista para la siguiente tanda
        file_count += 1  # Incrementar el contador de archivos

# Guardar los registros restantes
if data:
    output_filename = f"{output_basename}_{file_count}.csv"
    df = pd.DataFrame(data)
    df.to_csv(output_filename, index=False, encoding="utf-8-sig")
    print(f"💾 Guardado {len(data)} registros finales en {output_filename}")

# Cerrar el driver
driver.quit()
print("✅ Proceso completado.")
