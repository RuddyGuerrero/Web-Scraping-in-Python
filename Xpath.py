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
titulo = tree.xpath('//h1/text()')

# 2. Nombres de productos
productos = tree.xpath('//div[@class="producto"]/h2/text()')

# 3. Precios
precios = tree.xpath('//span[@class="precio"]/text()')

# 4. Links
links = tree.xpath('//a/@href')

# 5. Primer producto
primer_producto = tree.xpath('(//div[@class="producto"]/h2/text())[1]')

# Mostrar resultados
print("Título:", titulo)
print("Productos:", productos)
print("Precios:", precios)
print("Links:", links)
print("Primer producto:", primer_producto)