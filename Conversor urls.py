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
"https://www.vivino.com/api/w/2696113",
"https://www.vivino.com/api/w/2696113",
"https://www.vivino.com/api/w/1157820",
"https://www.vivino.com/api/w/1610937",
"https://www.vivino.com/api/w/3518950",
"https://www.vivino.com/api/w/7102672",
"https://www.vivino.com/api/w/6361748",
"https://www.vivino.com/api/w/1136819",
"https://www.vivino.com/api/w/12467366",
"https://www.vivino.com/api/w/9502",
"https://www.vivino.com/api/w/3962568",
"https://www.vivino.com/api/w/1175101",
"https://www.vivino.com/api/w/1756739",
"https://www.vivino.com/api/w/2476962",
"https://www.vivino.com/api/w/1100130",
"https://www.vivino.com/api/w/5270119",
"https://www.vivino.com/api/w/8308117",
"https://www.vivino.com/api/w/1312069",
"https://www.vivino.com/api/w/8666859",
"https://www.vivino.com/api/w/7319800",
"https://www.vivino.com/api/w/2356145",
"https://www.vivino.com/api/w/2229496",
"https://www.vivino.com/api/w/2604058",
"https://www.vivino.com/api/w/1176131",
"https://www.vivino.com/api/w/7508035",
"https://www.vivino.com/api/w/11031591",
"https://www.vivino.com/api/w/1419040",
"https://www.vivino.com/api/w/1203088",
"https://www.vivino.com/api/w/12314892",
"https://www.vivino.com/api/w/7834792",
"https://www.vivino.com/api/w/7170335",
"https://www.vivino.com/api/w/5962428",
"https://www.vivino.com/api/w/5492146",
"https://www.vivino.com/api/w/1366324",
"https://www.vivino.com/api/w/2476270",
"https://www.vivino.com/api/w/2129969",
"https://www.vivino.com/api/w/1157824",
"https://www.vivino.com/api/w/1630294",
"https://www.vivino.com/api/w/11290429",
"https://www.vivino.com/api/w/2019451",
"https://www.vivino.com/api/w/1713331",
"https://www.vivino.com/api/w/8927043",
"https://www.vivino.com/api/w/3254213",
"https://www.vivino.com/api/w/1781271",
"https://www.vivino.com/api/w/2034128",
"https://www.vivino.com/api/w/2104093",
"https://www.vivino.com/api/w/10272799",
"https://www.vivino.com/api/w/12980233",
"https://www.vivino.com/api/w/8414231",
"https://www.vivino.com/api/w/1654331",
"https://www.vivino.com/api/w/1172215",
"https://www.vivino.com/api/w/7980933",
"https://www.vivino.com/api/w/6673791",
"https://www.vivino.com/api/w/7665654",
"https://www.vivino.com/api/w/1160525",
"https://www.vivino.com/api/w/6003782",
"https://www.vivino.com/api/w/2335037",
"https://www.vivino.com/api/w/1628204",
"https://www.vivino.com/api/w/5528860",
"https://www.vivino.com/api/w/1770730",
"https://www.vivino.com/api/w/7319800",
"https://www.vivino.com/api/w/1277585",
"https://www.vivino.com/api/w/6428299",
"https://www.vivino.com/api/w/5825082",
"https://www.vivino.com/api/w/1897030",
"https://www.vivino.com/api/w/86559",
"https://www.vivino.com/api/w/1799",
"https://www.vivino.com/api/w/11980101",
"https://www.vivino.com/api/w/9889291",
"https://www.vivino.com/api/w/1508196",
"https://www.vivino.com/api/w/1366324",
"https://www.vivino.com/api/w/5786",
"https://www.vivino.com/api/w/7051259",
"https://www.vivino.com/api/w/1157820",
"https://www.vivino.com/api/w/8735674",
"https://www.vivino.com/api/w/1204920",
"https://www.vivino.com/api/w/8735674",
"https://www.vivino.com/api/w/5113689",
"https://www.vivino.com/api/w/1115042",
"https://www.vivino.com/api/w/4990729",
"https://www.vivino.com/api/w/6278804",
"https://www.vivino.com/api/w/1965396",
"https://www.vivino.com/api/w/10666674",
"https://www.vivino.com/api/w/2915307",
"https://www.vivino.com/api/w/6332557",
"https://www.vivino.com/api/w/3645221",
"https://www.vivino.com/api/w/4349115",
"https://www.vivino.com/api/w/11980125",
"https://www.vivino.com/api/w/6332557",
"https://www.vivino.com/api/w/3274546",
"https://www.vivino.com/api/w/1138218",
"https://www.vivino.com/api/w/11314358",
"https://www.vivino.com/api/w/1176131",
"https://www.vivino.com/api/w/4254643",
"https://www.vivino.com/api/w/2092049",
"https://www.vivino.com/api/w/1315077",
"https://www.vivino.com/api/w/12429922",
"https://www.vivino.com/api/w/2302999",
"https://www.vivino.com/api/w/1676725",
"https://www.vivino.com/api/w/6733808",
"https://www.vivino.com/api/w/1255547",
"https://www.vivino.com/api/w/2292476",
"https://www.vivino.com/api/w/1261545",
"https://www.vivino.com/api/w/2833148",
"https://www.vivino.com/api/w/1427369",
"https://www.vivino.com/api/w/9571182",
"https://www.vivino.com/api/w/8666859",
"https://www.vivino.com/api/w/8666802",
"https://www.vivino.com/api/w/1156464",
"https://www.vivino.com/api/w/6573414",
"https://www.vivino.com/api/w/1205348",
"https://www.vivino.com/api/w/9618321",
"https://www.vivino.com/api/w/1998548",
"https://www.vivino.com/api/w/1312310",
"https://www.vivino.com/api/w/1133685",
"https://www.vivino.com/api/w/8290443",
"https://www.vivino.com/api/w/8902890",
"https://www.vivino.com/api/w/1210331",
"https://www.vivino.com/api/w/1651025",
"https://www.vivino.com/api/w/12618266",
"https://www.vivino.com/api/w/15153",
"https://www.vivino.com/api/w/8618424",
"https://www.vivino.com/api/w/8618424",
"https://www.vivino.com/api/w/6889128",
"https://www.vivino.com/api/w/2906169",
"https://www.vivino.com/api/w/1223408",
"https://www.vivino.com/api/w/1990325",
"https://www.vivino.com/api/w/1402193",
"https://www.vivino.com/api/w/6409502",
"https://www.vivino.com/api/w/8163363",
"https://www.vivino.com/api/w/3593166",
"https://www.vivino.com/api/w/1889584",
"https://www.vivino.com/api/w/8223895",
"https://www.vivino.com/api/w/6253965",
"https://www.vivino.com/api/w/6489060",
"https://www.vivino.com/api/w/12035441",
"https://www.vivino.com/api/w/1181414",
"https://www.vivino.com/api/w/2335242",
"https://www.vivino.com/api/w/12651432",
"https://www.vivino.com/api/w/15162",
"https://www.vivino.com/api/w/1172446",
"https://www.vivino.com/api/w/1228821",
"https://www.vivino.com/api/w/5621293",
"https://www.vivino.com/api/w/1239704",
"https://www.vivino.com/api/w/2362889",
"https://www.vivino.com/api/w/5786403",
"https://www.vivino.com/api/w/2603026",
"https://www.vivino.com/api/w/7240954",
"https://www.vivino.com/api/w/1130511",
"https://www.vivino.com/api/w/1406874",
"https://www.vivino.com/api/w/1748985",
"https://www.vivino.com/api/w/4998630",
"https://www.vivino.com/api/w/2643603",
"https://www.vivino.com/api/w/7730356",
"https://www.vivino.com/api/w/1289973",
"https://www.vivino.com/api/w/1370776",
"https://www.vivino.com/api/w/1173344",
"https://www.vivino.com/api/w/1414800",
"https://www.vivino.com/api/w/2043864",
"https://www.vivino.com/api/w/7970520",
"https://www.vivino.com/api/w/1684983",
"https://www.vivino.com/api/w/2281898",
"https://www.vivino.com/api/w/9475143",
"https://www.vivino.com/api/w/13143446",
"https://www.vivino.com/api/w/1871720",
"https://www.vivino.com/api/w/2572685",
"https://www.vivino.com/api/w/9279521",
"https://www.vivino.com/api/w/12776913",
"https://www.vivino.com/api/w/15161",
"https://www.vivino.com/api/w/6167338",
"https://www.vivino.com/api/w/1271562",
"https://www.vivino.com/api/w/4311421",
"https://www.vivino.com/api/w/15153",
"https://www.vivino.com/api/w/1223408",
"https://www.vivino.com/api/w/2097186",
"https://www.vivino.com/api/w/2097186",
"https://www.vivino.com/api/w/11624914",
"https://www.vivino.com/api/w/4158914",
"https://www.vivino.com/api/w/3154082",
"https://www.vivino.com/api/w/1223408",
"https://www.vivino.com/api/w/9001164",
"https://www.vivino.com/api/w/6463639",
"https://www.vivino.com/api/w/1210471",
"https://www.vivino.com/api/w/4749359",
"https://www.vivino.com/api/w/2113345",
"https://www.vivino.com/api/w/1766902",
"https://www.vivino.com/api/w/1497432",
"https://www.vivino.com/api/w/4595006",
"https://www.vivino.com/api/w/1809808",
"https://www.vivino.com/api/w/12041422",
"https://www.vivino.com/api/w/6447942",
"https://www.vivino.com/api/w/1784087",
"https://www.vivino.com/api/w/7445848",
"https://www.vivino.com/api/w/7009293",
"https://www.vivino.com/api/w/6974436",
"https://www.vivino.com/api/w/7614063",
"https://www.vivino.com/api/w/11295451",
"https://www.vivino.com/api/w/12453119",
"https://www.vivino.com/api/w/83408",
"https://www.vivino.com/api/w/11120048",
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
with open('def_espumoso400.txt', 'w') as file:
    for url in new_urls:
        file.write(url + '\n')

# Cerrar el navegador
driver.quit()

print("Las nuevas URLs han sido guardadas en 'def_espumoso400.txt'.")