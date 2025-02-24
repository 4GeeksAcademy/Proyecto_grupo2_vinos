from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Modo headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

# Lista de URLs a procesar
urls_list = [
"https://www.vivino.com/api/w/10488113",
"https://www.vivino.com/api/w/9930105",
"https://www.vivino.com/api/w/5304181",
"https://www.vivino.com/api/w/10554888",
"https://www.vivino.com/api/w/10802124",
"https://www.vivino.com/api/w/1471042",
"https://www.vivino.com/api/w/2931116",
"https://www.vivino.com/api/w/1208591",
"https://www.vivino.com/api/w/9304576",
"https://www.vivino.com/api/w/1115819"
    
]

# Lista para almacenar las nuevas URLs
new_urls = []

# Procesar cada URL en la lista
for original_url in urls_list:
    print(f"Procesando URL: {original_url}")  # Mostrar el progreso

    # Abrir la URL
    driver.get(original_url)

    # Esperar a que la página se cargue completamente
    time.sleep(1)  # Ajusta el tiempo según sea necesario

    # Obtener la nueva URL
    new_url = driver.current_url
    print(f"Nueva URL: {new_url}")

    # Agregar la nueva URL a la lista
    new_urls.append(new_url)

# Guardar las nuevas URLs en un archivo
with open('new_urls.txt', 'w') as file:
    for url in new_urls:
        file.write(url + '\n')

# Cerrar el navegador
driver.quit()

print("Las nuevas URLs han sido guardadas en 'new_urls.txt'.")