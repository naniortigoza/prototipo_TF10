from faker import Faker
import csv
import pandas as pd
import random
from datetime import datetime, timedelta

# Función para generar un nuevo ID de propiedad que no se duplique
def generar_id_propiedad_unico(ids_generados, max_id=50):
    while True:
        propiedad_id = random.randint(1, max_id)
        if propiedad_id not in ids_generados:
            ids_generados.add(propiedad_id)
            return propiedad_id

# Función para buscar el precio de una propiedad por su ID
def buscar_precio_por_id_propiedad(id_propiedad):
    try:
        # Lee el archivo CSV en un DataFrame
        data = pd.read_csv("datos/datos_propiedades.csv")
        
        # Busca la fila correspondiente al ID de la propiedad
        fila = data[data['Propiedad_ID'] == id_propiedad]
        
        # Obtiene el precio de venta de esa propiedad
        precio = fila['Precio'].values[0]
        
        return precio
    except FileNotFoundError:
        return None
    except IndexError:
        return None

# Función para buscar el presupuesto máximo de un cliente por su ID
def buscar_presupuesto_maximo_por_id_cliente(id_cliente):
    try:
        # Lee el archivo CSV en un DataFrame
        data = pd.read_csv("datos/datos_clientes.csv")
        
        # Busca la fila correspondiente al ID del cliente
        fila = data[data['Cliente_ID'] == cliente_id]
        
        # Obtiene el precio de venta de esa propiedad
        presupuesto_maximo = fila['Presupuesto_Maximo'].values[0]
        
        return presupuesto_maximo
    except FileNotFoundError:
        return None
    except IndexError:
        return None

# Crear una instancia de Faker para generar datos en español
faker = Faker("es_ES")

# Crear una lista de encabezados de columna
encabezados = ["ID de Venta", "Propiedad_ID", "Cliente_ID", "Fecha de Venta", "Precio de Venta"]

# Define la fecha de inicio (1 de noviembre de 2019) y la fecha de fin (31 de diciembre de 2019)
start_date = datetime(2019, 11, 1)
end_date = datetime(2019, 11, 30)

# Definir el número de registros para crear
num_registros = 20

# Crear una lista para almacenar los registros
registros = []

# Generar registros
for id_transaccion in range(1, num_registros + 1):
    # Selecciona un cliente aleatorio de la lista de clientes
    cliente_id = random.randint(1, 100)
    presupuesto_maximo = buscar_presupuesto_maximo_por_id_cliente(cliente_id)

    propiedad_id = 0
    intentos = 0
    precio_venta = None  # Valor predeterminado

    while propiedad_id <= 100 and intentos < 5:
        # Generar un nuevo ID de propiedad que no se duplique
        propiedad_id = generar_id_propiedad_unico(set(), max_id=100)

        # Buscar el precio real de la propiedad
        precio_real = buscar_precio_por_id_propiedad(propiedad_id)

        if precio_real is not None and precio_real <= presupuesto_maximo:
            # Calcula el precio máximo permitido como el 110% del precio de la propiedad
            precio_maximo = int(precio_real * 1.1)
            # Genera un precio de venta aleatorio entre el precio de la propiedad y el precio máximo
            precio_venta = random.randint(precio_real, precio_maximo)
            # Redondea el precio de venta al múltiplo de 1,000,000 más cercano
            precio_venta = (precio_venta // 1000000) * 1000000
            break  # Si encontramos una propiedad adecuada, salimos del bucle while

        intentos += 1

    if propiedad_id == 0 or precio_venta is None:
        continue  # Salta este registro si no se encontró una propiedad que cumpla con el presupuesto después de 5 intentos

    # Fecha de Venta
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    fecha_venta = random_date.strftime("%d/%m/%Y")

    # Agregar los datos a la lista de registros
    registros.append([id_transaccion, propiedad_id, cliente_id, fecha_venta, precio_venta])

# Nombre del archivo CSV donde deseas guardar los datos
nombre_archivo = 'datos/datos_ventas.csv'

# Escribir los datos en un archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los encabezados
    escritor_csv.writerow(encabezados)
    
    # Escribir los registros
    for registro in registros:
        escritor_csv.writerow(registro)

print(f'Datos guardados en {nombre_archivo}')
