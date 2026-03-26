from selenium import webdriver
from selenium.webdriver.common.by import By

# Crear un navegador (Chrome)
driver = webdriver.Chrome()  

# Abrir la página
driver.get("https://quotes.toscrape.com/")

citas_elements = driver.find_elements(By.XPATH, '//div[@class="quote"]/span[@class="text"]')
citas = [cita.text for cita in citas_elements]
print(citas)

autores_elements = driver.find_elements(By.XPATH, '//div[@class="quote"]/span/small[@class="author"]')
autores = [autor.text for autor in autores_elements]
print(autores)

tags_elements = driver.find_elements(By.XPATH, '//div[@class="quote"]/div[@class="tags"]/a')
tags = [tag.text for tag in tags_elements]
print(tags)

driver.quit()