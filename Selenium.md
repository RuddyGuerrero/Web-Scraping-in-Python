# 🧑‍🏫 Web Scraping con Selenium y XPath

## ¿Qué es Selenium?

**Selenium** es una herramienta que permite **automatizar navegadores web**. Se usa en **testing** y **web scraping**.

> 💡 Selenium es como un robot que abre Chrome o Firefox, hace clics, escribe en formularios y copia información automáticamente.

### Conceptos clave

| Concepto           | Explicación                                                                 |
|-------------------|----------------------------------------------------------------------------|
| **Driver**         | Programa que controla un navegador específico (Chrome → chromedriver)      |
| **WebElement**     | Representa un elemento de la página (botón, enlace, input, etc.)          |
| **get(url)**       | Abrir una página web                                                        |
| **find_element(s)**| Buscar elementos en la página usando XPath, CSS Selector, ID, clase…      |
| **click()**        | Hacer clic en un elemento                                                   |
| **send_keys()**    | Escribir texto en un input o textarea                                       |
| **text**           | Extraer el texto visible de un elemento                                     |
| **get_attribute()**| Extraer un atributo de un elemento (por ejemplo `href` o `src`)            |
| **quit()**         | Cerrar el navegador                                                         |

## Instalación

```bash
pip install selenium pandas
```

## Ejemplo de Selenium

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Abrir navegador y cargar página ---
driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

# --- Esperar que cargue al menos una cita (espera explícita) ---
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="quote"]'))
)

# --- Obtener citas ---
citas = driver.find_elements(By.XPATH, '//span[@class="text"]')
citas = [c.text for c in citas]
print("Citas:", citas)

# --- Obtener autores ---
autores = driver.find_elements(By.XPATH, '//small[@class="author"]')
autores = [a.text for a in autores]
print("Autores:", autores)

# --- Obtener tags ---
tags = driver.find_elements(By.XPATH, '//div[@class="tags"]/a')
tags = [t.text for t in tags]
print("Tags:", tags)

# --- Hacer clic en el botón 'Next' para ir a la siguiente página ---
next_button = driver.find_element(By.XPATH, '//li[@class="next"]/a')
next_button.click()

# --- Esperar que cargue la siguiente página ---
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="quote"]'))
)

# --- Obtener citas de la siguiente página ---
citas_sig = driver.find_elements(By.XPATH, '//span[@class="text"]')
citas_sig = [c.text for c in citas_sig]
print("Citas siguiente página:", citas_sig)

# --- Cerrar navegador ---
driver.quit()
```

## Mini reto: Quotes to Scrape

Página: https://quotes.toscrape.com

Objetivos:

1. Obtener todas las citas (`text`)
2. Obtener todos los autores (`author`)
3. Obtener todos los tags (`tags`)
4. Filtrar solo citas de “Albert Einstein”
5. Contar el número de citas en la página

```python
# Mini Reto: Quotes to Scrape
# Página: https://quotes.toscrape.com

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir navegador y cargar la página
driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com')

# Obtener todas las citas (texto)
citas = None  # COMPLETAR

# Obtener todos los autores
autores = None  # COMPLETAR

# Obtener todos los tags
tags = None  # COMPLETAR

# Filtrar solo citas de “Albert Einstein”
citas_einstein = None  # COMPLETAR

# Contar el número de citas en la página
num_citas = None  # COMPLETAR

# Imprimir los resultados
print("Citas:", citas)
print("Autores:", autores)
print("Tags:", tags)
print("Citas de Einstein:", citas_einstein)
print("Número de citas:", num_citas)

# Cerrar navegador
driver.quit()
```


## Mini Proyecto: La Liga

Página: https://www.adamchoi.co.uk/leagues/spain-la-liga

Objetivos:
1. Abrir la página y hacer clic en “All matches”
2. Estraer datos de la tabla
3. Exportar los datos a un .csv
4. Analizar con pandas (opcional)

```python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.adamchoi.co.uk/leagues/spain-la-liga')

wait = WebDriverWait(driver, 20)

# Cerrar banner de cookies
try:
    consent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//p[text()="Consent"]'))
    )
    driver.execute_script("arguments[0].click();", consent)
except:
    print("No apareció banner")

# Acceder al shadow root
shadow_host = driver.find_element(By.CSS_SELECTOR, 'league-table-widget')
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

# Ahora podemos buscar filas dentro del shadow DOM
rows = shadow_root.find_elements(By.CSS_SELECTOR, 'table#league-table tbody tr')

print(f"Filas encontradas: {len(rows)}")


# Continuar analizando los datos que aparecen en row
```

