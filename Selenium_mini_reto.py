from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir navegador y cargar la página
driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com')

# Obtener todas las citas (texto)
citas = driver.find_elements(By.XPATH, '//span[@class="text"]')
citas = [c.text for c in citas]

# Obtener todos los autores
autores = driver.find_elements(By.XPATH, '//small[@class="author"]')
autores = [a.text for a in autores]

# Obtener todos los tags
tags = driver.find_elements(By.XPATH, '//div[@class="tags"]/a')
tags = [t.text for t in tags]

# Filtrar solo citas de “Albert Einstein”
citas_einstein = [c.text for c in driver.find_elements(By.XPATH, '//div[@class="quote"]') if 'Albert Einstein' in c.text]

# Contar el número de citas en la página
num_citas = len(citas)

# Imprimir los resultados
print("Citas:", citas)
print("Autores:", autores)
print("Tags:", tags)
print("Citas de Einstein:", citas_einstein)
print("Número de citas:", num_citas)

# Cerrar navegador
driver.quit()