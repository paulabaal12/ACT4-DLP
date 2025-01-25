import re
import csv

# Cargar archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()
    
# Buscar productos y URLs de imágenes
def extraer_productos(html):
    # Expresiones regulares para extraer nombres e imágenes
    regex_nombre = r'<span[^>]*class="[^"]*vtex-product-summary-2-x-brandName[^"]*"[^>]*>(.*?)<!--'
    regex_imagen = r'<img[^>]*src="([^"]+)"[^>]*class="[^"]*vtex-product-summary-2-x-image[^"]*"'
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)
    return zip(nombres, imagenes)

# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

pagina = cargar_html('productos.html')
productos = extraer_productos(pagina)
exportar_csv(productos, 'productos.csv')
print("Productos añadidos a productos.csv")
