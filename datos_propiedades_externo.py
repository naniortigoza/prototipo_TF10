import requests                  # pip install requests
import re
import datetime
import csv
import demoji                   # pip install demoji
import pandas as pd             # pip install pandas

from unidecode import unidecode # pip install Unidecode
from bs4 import BeautifulSoup   # pip install beautifulsoup4
from datetime import datetime

# Variables global
id_auto = 1
year = datetime.now().year

# Lee los archivos CSV en un DataFrame
data_zona = pd.read_csv("datos/datos_zonas.csv")
data_economicos = pd.read_csv("datos/datos_economicos.csv")

# Función para generar un nuevo ID
def generar_id():
    global id_auto
    nuevo_id = id_auto
    id_auto += 1
    return nuevo_id

# Función para buscar el texto en la columna Barrios
def buscar_zona_id(texto):
    for index, row in data_zona.iterrows():
        if texto in row["Barrios"]:
            return row["Zona_ID"]
    return None

# Función para obtener el último ID_Datos correspondiente a una Zona_ID en data_economicos
def obtener_ultimo_id_datos(zona_id):
    filtro = data_economicos['Zona_ID'] == zona_id
    id_datos_por_zona = data_economicos[filtro]['ID_Datos'].unique()
    if len(id_datos_por_zona) > 0:
        max_id_datos = max(id_datos_por_zona)
    
    return max_id_datos

# Lista de URLs que deseas obtener y analizar
urls = [
    'https://www.remax.com.py/es-py/propiedades/casa/venta/tacumbu/15-de-agosto-15-de-agosto-y-14%C2%B0-proyectada/143079002-27',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/san-roque/143094007-15',
    'https://www.remax.com.py/es-py/propiedades/departamento/venta/loma-pyta/lombardo-c-dr-garay-lombardo-c-dr-garay/143079031-94',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/zeballos-cue/san-ramon-san-ramon-y-calle-xxiv-san-ramon-y-calle-xxiv/114006030-7',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/villa-aurelia/timoteo-aguirre-timoteo-aguirre-y-aristigueta/143028061-4',
    'https://www.remax.com.py/es-py/propiedades/departamento/venta/recoleta/sobre-legion-civil-extranjera-legion-civil-extranjera-casi-las-perlas/143014141-115',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/tacumbu/15-de-agosto-15-de-agosto-y-14%C2%B0-proyectada/143079002-27',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/san-roque/143094007-15',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/zeballos-cue/san-ramon-san-ramon-y-calle-xxiv-san-ramon-y-calle-xxiv/114006030-7',
    'https://www.remax.com.py/es-py/propiedades/departamento/venta/las-lomas-carmelitas/molas-lopez-molas-lopez/143056025-21',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/obrero/143026146-22',
    'https://www.remax.com.py/es-py/propiedades/departamento/venta/san-roque/paraguari-esquina-simon-bolivar-paraguari-esquina-simon-bolivar/143041001-364',
    'https://www.remax.com.py/es-py/propiedades/casa/venta/hipodromo/teniente-primero-venancio-c-concepcion-teniente-primero-venancio-c-concepcion/143019024-104',
    'https://www.remax.com.py/es-py/propiedades/terreno/venta/san-cristobal/capitan-herminio-maldonado-c-eusebio-lillo-robles-barrio-herrera/114006028-2'
    ]

# Crear una lista de encabezados de columna
encabezados = ["Propiedad_ID", "ID_Datos", "Tipo_Propiedad", "Ubicacion", "Tamanho", "Habitaciones", "Precio", "Antiguedad", "Carac_Adicionales", "Ubicacion_Especial"]

# Crear una lista para almacenar los registros ficticios
registros = []

# Descarga el conjunto de datos de emojis (solo necesita hacerse una vez)
#demoji.download_codes()

for url in urls:
    # Realiza una solicitud HTTP GET a la URL actual
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
         # Crear un diccionario para almacenar los datos de esta página
        datos_pagina = {}

        # Analiza el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        ########################################
        # Aquí realizamos el análisis de datos #
        ########################################

        # Generar un id único
        propiedad_id = generar_id()

        # Obtener el último ID_Datos correspondiente a esta Zona_ID
        ubicacion_esp = soup.find('div', class_='col-xs-12 key-address fts-mark').get_text().strip()
        zona_id = data_zona[data_zona['Barrios'].str.contains(ubicacion_esp[17:26])]['Zona_ID'].values[0]
        ultimo_id_datos = obtener_ultimo_id_datos(zona_id)
        
        # Tipo de propiedad
        titulo = soup.find('div', class_='col-xs-12 key-title').find('h1').get_text()
        titulo = str(titulo[0:titulo.find('-')-1])
        # Comparamos el texto obtenido con las categorías y asignamos el valor correspondiente
        if "Casa" in titulo:
            tipo_de_propiedad = 1
        elif "Departamento" in titulo:
            tipo_de_propiedad = 2
        elif "Terreno" in titulo:
            tipo_de_propiedad = 3
        elif "Local Comercial" in titulo:
            tipo_de_propiedad = 4
        else:
            # Puedes manejar un caso predeterminado si el texto no coincide con ninguna categoría conocida
            tipo_de_propiedad = 0  # Por ejemplo, 0 para otros casos

        # La ubicación de la propiedad en latitud y longitud
        texto_ubi = soup.find('input', class_='map listingfull-map-toggler')
        if texto_ubi:
            data_lat = texto_ubi['data-lat']
            data_lng = texto_ubi['data-lng']
            ubicacion = data_lat + ", " + data_lng
        else:
            ubicacion = ""

        # Tamaño
        pattern = re.compile(r'Sup\. Lote \(m²\):.*')
        tit_tamanho = soup.find('div', class_='data-item-label', attrs={'data-toggle': 'tooltip', 'data-original-title': pattern})
        if tit_tamanho:
            texto_tamanho = tit_tamanho.find_next_sibling('div')
            tamanho = float(texto_tamanho.find('span').get_text())
        else:
            tamanho = 0.0

        # Número de Habitaciones
        pattern = re.compile(r'Nº de Dormitorios:.*')
        tit_habitaciones = soup.find('div', class_='data-item-label', attrs={'data-toggle': 'tooltip', 'data-original-title': pattern})
        if tit_habitaciones:
            texto_habitaciones = tit_habitaciones.find_next_sibling('div')
            habitaciones = int(texto_habitaciones.find('span').get_text())
        else:
            habitaciones = 0

        # El precio de la propiedad en guaraníes
        precio_texto = soup.find('div', class_='key-price-div').find('a').get_text()
        precio_texto = precio_texto.replace(',', '')
        precio = int(precio_texto[0:precio_texto.find(' ')])

        # Antigüedad de la construcción en años
        pattern = re.compile(r'Año/Mes Construcción*')
        tit_antiguedad = soup.find('div', class_='data-item-label', attrs={'data-toggle': 'tooltip', 'data-original-title': pattern})
        if tit_antiguedad:
            texto_antiguedad = tit_antiguedad.find_next_sibling('div').find('span').get_text()
            antiguedad = year - int(texto_antiguedad[0:texto_antiguedad.find('/')])
        else:
            antiguedad = 0

        # Caracteristicas_Adicionales: Cualquier característica especial de la propiedad, como piscina, jardín, garaje, etc.
        caracteristicas_adi = soup.find('div', class_='desc-short fts-mark tab-pane').get_text()
        caracteristicas_adi = unidecode(demoji.replace(caracteristicas_adi.replace("°", "o"))) # Elimina los emojis del texto

        # Ubicacion_Especifica: Información adicional sobre la ubicación específica de la propiedad, como calles cercanas, puntos de referencia, etc.
        ubicacion_esp = soup.find('div', class_='col-xs-12 key-address fts-mark').get_text().replace("\n", "")
        #ubicacion_esp = unidecode(demoji.replace(ubicacion_esp.replace("°", "o"))).split # Elimina los emojis del texto

         # Agregar los datos a la lista de registros
        registros.append([propiedad_id, ultimo_id_datos, tipo_de_propiedad, ubicacion, tamanho, habitaciones, precio, antiguedad, caracteristicas_adi, ubicacion_esp])

# Nombre del archivo CSV donde deseas guardar los datos
nombre_archivo = 'datos/datos_propiedades.csv'

# Escribir los datos ficticios en un archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los encabezados
    escritor_csv.writerow(encabezados)
    
    # Escribir los registros ficticios
    for registro in registros:
        escritor_csv.writerow(registro)

print(f'Datos guardados en {nombre_archivo}')