from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd  # Asegúrate de importar pandas

# Crear instancia de driver
driver = webdriver.Chrome()

# Lista de URLs
urls = [
"https://www.vivino.com/ES/es/weingut-prager-wachstum-bodenstein-gruner-veltliner/w/2137185",
"https://www.vivino.com/ES/es/pt-susana-esteban-sidecar-blanc/w/3751531",
"https://www.vivino.com/ES/es/tappero-merlo-domenico-kin/w/6369455",
"https://www.vivino.com/ES/es/fr-bourdy-cotes-du-jura-blanc/w/2665502",
"https://www.vivino.com/ES/es/chateau-olivier-pessac-leognan-blanc-grand-cru-classe-de-graves/w/87425",
"https://www.vivino.com/ES/es/federico-curtaz-kudos-etna-bianco-superiore/w/8500339",
"https://www.vivino.com/ES/es/bimbache-john-stone/w/8862424",
"https://www.vivino.com/ES/es/cantina-carta-filet-bianco/w/7303290",
"https://www.vivino.com/ES/es/alain-graillot-crozes-hermitage-blanc/w/1148131",
"https://www.vivino.com/ES/es/joseph-drouhin-drouhin-vaudon-chablis-premier-cru-mont-de-milieu/w/4016358",
"https://www.vivino.com/ES/es/francois-cotat-caillottes-sancerre/w/1409762",
"https://www.vivino.com/ES/es/fr-albert-mann-wineck-schlossberg-riesling-grand-cru/w/9917762",
"https://www.vivino.com/ES/es/domaine-jean-chartron-puligny-montrachet/w/87188",
]

data = []

# Función para hacer scroll
def scroll_page():
    # Hacer scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Esperar a que carguen más elementos

# Recorrer cada URL
for url in urls:
    driver.get(url)
    time.sleep(5)  # Esperar a que la página cargue

    # Hacer scroll hasta el final de la página
    scroll_page()

    # Extraer el ID del vino
    wine_id = url.split("/")[-1]

    try:
        # Esperar a que el elemento de notas de sabor esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2"))
        )

        # Extraer las notas de sabor
        taste_notes_elements = driver.find_elements(By.CSS_SELECTOR, "div.tasteNote__popularKeywords--1gIa2")
        taste_notes = [el.text.strip() for el in taste_notes_elements if el.text.strip()]

        # Asignar las notas de sabor a diferentes campos
        taste_notes_dict = {}
        for i, note in enumerate(taste_notes):
            taste_notes_dict[f"Taste_Notes_{i+1}"] = note

        # Asegurarse de que haya un campo para cada nota de sabor
        for i in range(len(taste_notes), 3):  # Asumiendo que el máximo es 3 notas
            taste_notes_dict[f"Taste_Notes_{i+1}"] = "No disponible"

    except Exception as e:
        print(f"Error al extraer las notas de sabor de {wine_id}: {e}")
        taste_notes_dict = {"Taste_Notes_1": "No disponible", "Taste_Notes_2": "No disponible", "Taste_Notes_3": "No disponible"}

    # Guardar en la lista
    data.append({"Wine_ID": wine_id, "Taste_Notes": taste_notes})

# Cerrar el driver
driver.quit()

# Guardar en CSV
df = pd.DataFrame(data)
df.to_csv("vivino_wines.csv", index=False)
print(df)
