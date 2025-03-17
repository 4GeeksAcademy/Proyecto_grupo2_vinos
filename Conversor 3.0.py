import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor

# Function to save URLs to a file
def save_urls_to_file(urls, batch_number):
    filename = f'def_blancos7199_{batch_number}.txt'
    with open(filename, 'w') as file:
        file.write('\n'.join(urls))
    print(f"Las nuevas URLs han sido guardadas en '{filename}'.")

# Function to process a single URL
def process_url(original_url):
    try:
        # Use the global driver instance
        driver.get(original_url)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        new_url = driver.current_url
        return new_url
    except Exception as e:
        print(f"Error procesando {original_url}: {e}")
        return None

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--log-level=3")  # Suppress logs

# Read URLs from a .txt file
with open('blancos7199.txt', 'r') as file:
    urls_list = [line.strip() for line in file.readlines()]

# List to store new URLs
new_urls = []
batch_size = 100
batch_number = 1

# Create a single WebDriver instance
driver = webdriver.Chrome(options=options)

# Process URLs in parallel with a limited number of workers
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(process_url, urls_list))

# Filter out None results and collect new URLs
new_urls = [url for url in results if url]

# Save URLs in batches
for i in range(0, len(new_urls), batch_size):
    save_urls_to_file(new_urls[i:i + batch_size], batch_number)
    batch_number += 1

# Close the WebDriver
driver.quit()

print("Proceso completado.")