# Actividad 4 - Diseño de Lenguajes de Programación

## Descripción
Este programa realiza la extracción de nombres de productos y URLs de imágenes desde un archivo HTML descargado del sitio web de [La Torre ](https://www.latorre.com.gt/chocolate?_q=chocolate&map=ft). Los datos obtenidos se exportan a un archivo CSV estructurado.

## Estructura del Proyecto:
1. [productos.html](https://github.com/paulabaal12/ACT4-DLP/blob/main/productos.html): Archivo HTML descargado del sitio web.
2. [productos.csv](https://github.com/paulabaal12/ACT4-DLP/blob/main/productos.csv): Archivo donde se almacenan los productos extraídos.
3. [main.py](https://github.com/paulabaal12/ACT4-DLP/blob/main/main.py): Archivo principal que contiene la lógica del programa.

## Funcionamiento
1. Carga del HTML
La función ```cargar_html(archivo)``` lee el archivo HTML descargado y carga su contenido como texto.

2. Extracción de Datos
La función ```extraer_productos(html)``` utiliza expresiones regulares (regex) para localizar:
    - Nombres de productos:

        ```python
        regex_nombre = r'<span[^>]*class="[^"]*vtex-product-summary-2-x-brandName[^"]*"[^>]*>(.*?)<!--'
        ```
        Este patrón busca el contenido entre etiquetas ```<span>``` específicas.

    - URLs de imágenes:

        ```python
        regex_imagen = r'<img[^>]*src="([^"]+)"[^>]*class="[^"]*vtex-product-summary-2-x-image[^"]*"'
        ```
        Este patrón localiza enlaces de imágenes en los atributos ```src```.

    Los datos extraídos se agrupan usando ```zip()``` para asociar nombres con imágenes.

3. **Exportación a CSV**

    La función ```exportar_csv(productos, archivo_salida)``` escribe los datos extraídos en un archivo CSV con dos columnas:

    - Nombre del Producto
    - URL de la Imagen

## Ejecución
1. Descarga el archivo HTML desde el navegador.
2. Ejecuta el script ```main.py``` para procesar los datos.
3. Los resultados estarán disponibles en el archivo ```productos.csv```.

## Video de ejecución
En este video explicamos como funciona el codigo y su ejecución.
[Enlace a video](https://youtu.be/M5GgWscYSv4).

## Desarrollado por:
- **[Mónica Salvatierra - 22249](https://github.com/alee2602)**
- **[Paula Barillas - 22764](https://github.com/paulabaal12)**
- **[Derek Arreaga - 22537](https://github.com/FabianKel)**
- **[Andrés Kou - 22305](https://github.com/EdwinOrtegaK)**
- **[Esteban Zambrano - 22119](https://github.com/EstebanZG999)**
