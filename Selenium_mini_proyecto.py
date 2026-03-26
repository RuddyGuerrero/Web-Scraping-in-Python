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

# Lista para guardar los datos
data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    # Últimos 5 partidos
    form = [span.text for span in cells[-1].find_elements(By.TAG_NAME, 'span')]
    # Datos de la fila (excepto la columna de Form)
    row_data = [cells[0].text, cells[1].text] + [cell.text for cell in cells[2:-1]] + form
    data.append(row_data)

# Crear DataFrame con columnas claras
columns = ['Pos', 'Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts', 'F1', 'F2', 'F3', 'F4', 'F5']
df = pd.DataFrame(data, columns=columns)

print(df)
df.to_csv('La liga.csv')

driver.quit()