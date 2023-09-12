import csv
from faker import Faker
import random

from datos_propiedades_externo import generar_id

# Crear una instancia de Faker para generar datos ficticios en español
faker = Faker("es_ES")

# Definir el número de registros ficticios que deseas crear
num_registros = 50

# Crear una lista de encabezados de columna
encabezados = ["Propiedad_ID", "Zona_ID", "Tipo_de_Propiedad", "Ubicacion", "Tamanho", "Habitaciones", "Precio", "Antiguedad", "Carac. Adicionales", "Ubicacion Especial"]

# Crear una lista para almacenar los registros ficticios
registros = []

# Crear una lista para realizar un seguimiento de los IDs generados de zona
ids_generados = []

# Generar registros ficticios
for j in range(1, num_registros + 1):
    # Generar un id único
    propiedad_id = generar_id()

    # Zona_ID
    zona_id = 6

    # Tipo de Propiedad
    tipo_de_propiedad = random.randint(1, 4)
    # 1-Casa 2-Departamento 3-Terreno 4-Local Comercial

    # La ubicación de la propiedad en latitud y longitud
    data_lat = random.uniform(-27, -19)
    data_lng = random.uniform(-62, -54)
    ubicacion = str(data_lat) + ", " + str(data_lng)

    # Tamaño
    tamanho = round(random.uniform(50, 1000), 2)  # Tamaño entre 50 y 1000 metros cuadrados

    # Número de Habitaciones
    habitaciones = random.randint(1, 5)

    # El precio de la propiedad en guaraníes
    precio = random.randint(10000000 // 1000000, 1000000000 // 1000000) * 1000000  # Precio entre 10,000,000 y 1,000,000,000 guaraníes

    # Antigüedad de la construcción en años
    antiguedad = random.randint(1, 10)

    # Caracteristicas_Adicionales: Cualquier característica especial de la propiedad, como piscina, jardín, garaje, etc.
    caracteristicas_adi = faker.paragraph()

    # Ubicacion_Especifica: Información adicional sobre la ubicación específica de la propiedad, como calles cercanas, puntos de referencia, etc.
    ubicacion_esp = faker.paragraph()

    # Agregar los datos a la lista de registros
    registros.append([propiedad_id, zona_id, tipo_de_propiedad, ubicacion, tamanho, habitaciones, precio, antiguedad, caracteristicas_adi, ubicacion_esp])
    
# Nombre del archivo CSV donde deseas guardar los datos
nombre_archivo = 'datos/datos_propiedades_interno.csv'

# Escribir los datos ficticios en un archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los encabezados
    escritor_csv.writerow(encabezados)
    
    # Escribir los registros ficticios
    for registro in registros:
        escritor_csv.writerow(registro)

print(f'Datos guardados en {nombre_archivo}')