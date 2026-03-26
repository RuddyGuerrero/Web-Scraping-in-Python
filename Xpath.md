# Introducción a XPath en Python

## 1️⃣ ¿Qué es XPath?

XPath (XML Path Language) es un lenguaje para navegar y buscar información en documentos HTML/XML.


## 2️⃣ Introducción a lxml y etree

### 🔍 ¿Qué es lxml?

Librería de Python para procesar HTML y XML.

### 🧠 ¿Qué es etree?

Convierte el HTML en una estructura de árbol que Python puede recorrer.

## 3️⃣ Uso básico

``` python
from lxml import etree

html = "<html><body><p>Hola</p></body></html>"
tree = etree.HTML(html)

print(tree.xpath('//p/text()'))
```

## 4️⃣ Ejemplos XPath

## 4️⃣ Ejemplos XPath

| XPath                        | Significado                              |
|------------------------------|------------------------------------------|
| //h1                         | Todos los h1                             |
| //p                          | Todos los párrafos                       |
| //p/text()                   | Texto de los párrafos                    |
| //a/@href                    | Atributos href (links)                   |
| //li[1]                      | Primer elemento                          |
| //li[last()]                 | Último elemento                          |
| //div[@id="main"]            | Div con id="main"                        |
| //p[@class="texto"]          | P con clase "texto"                      |
| //a[text()="Google"]         | Enlace con texto exacto "Google"         |
| //li[position()=2]           | Segundo elemento                         |
| //li[position()>1]           | Elementos a partir del segundo           |
| //*[contains(@class,"item")] | Elementos cuya clase contiene "item"     |
| //a[contains(@href,"google")]| Links que contienen "google"             |
| //div//p                     | P dentro de cualquier div                |
| /html/body/div               | Ruta absoluta                            |
| //input[@type="text"]        | Inputs tipo texto                        |
| //img/@src                   | URLs de imágenes                         |

## 5️⃣ Ejercicio

```python
from lxml import etree

html = """
<html>
  <body>
    <h1>Título</h1>
    <p class="texto">Hola mundo</p>
    <p>Hola hola carcola</p>
  </body>
</html>
"""

tree = etree.HTML(html)

resultado1 = tree.xpath('//p[@class="texto"]/text()')
resultado2 = tree.xpath('//p/text()')

print(resultado)
```

## 🚀 Mini reto

```python
from lxml import etree

from lxml import etree

html = """
<html>
  <body>
    <h1>Tienda Online</h1>
    
    <div class="productos">
      <div class="producto">
        <h2>Portátil</h2>
        <a href="link1.com">Ver producto</a>
        <span class="precio">1000€</span>
      </div>
      
      <div class="producto">
        <h2>Ratón</h2>
        <a href="link2.com">Ver producto</a>
        <span class="precio">25€</span>
      </div>
      
      <div class="producto">
        <h2>Teclado</h2>
        <a href="link3.com">Ver producto</a>
        <span class="precio">50€</span>
      </div>
    </div>
    
    <div class="contacto">
      <p>Email: tienda@email.com</p>
    </div>
    
  </body>
</html>
"""

tree = etree.HTML(html)

# 1. Título
titulo = None  # COMPLETAR

# 2. Nombres de productos
productos = None  # COMPLETAR

# 3. Precios
precios = None  # COMPLETAR

# 4. Links
links = None  # COMPLETAR

# 5. Primer producto
primer_producto = None  # COMPLETAR

# Mostrar resultados
print("Título:", titulo)
print("Productos:", productos)
print("Precios:", precios)
print("Links:", links)
print("Primer producto:", primer_producto)
```

### Obtener:

- El título de la página
- Todos los nombres de productos
- Todos los precios
- Todos los links (href)
- El nombre del primer producto
