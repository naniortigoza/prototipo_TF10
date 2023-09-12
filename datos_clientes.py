import csv
from faker import Faker         # pip install faker
import random

# Crear una instancia de Faker para generar datos ficticios en español
faker = Faker("es_ES")

# Definir el número de registros ficticios que deseas crear
num_registros = 100

# Crear una lista de encabezados de columna
encabezados = ["Cliente_ID", "Nombre", "Apellido", "Correo_Electronico", "Telefono", "Presupuesto_Maximo", "Preferencia_de_Ubicacion", "Fecha_de_Registro"]

# Crear una lista para almacenar los registros ficticios
registros = []

# Generar registros ficticios
for i in range(1, num_registros + 1):
    cliente_id = i
    nombre = faker.first_name()
    apellido = faker.last_name()
    correo = faker.email()
    telefono = faker.phone_number()
    presupuesto_maximo = random.randint(10000000 // 1000000, 1000000000 // 1000000) * 1000000  # Presupuesto entre 10,000,000 y 1,000,000,000
    preferencia_ubicacion = faker.city()
    fecha_registro = faker.date_between(start_date="-2y", end_date="today")  # Fecha de registro en los últimos 2 años

    # Agregar los datos a la lista de registros
    registros.append([cliente_id, nombre, apellido, correo, telefono, presupuesto_maximo, preferencia_ubicacion, fecha_registro])

# Nombre del archivo CSV donde deseas guardar los datos
nombre_archivo = 'datos/datos_clientes.csv'

# Escribir los datos ficticios en un archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir los encabezados
    escritor_csv.writerow(encabezados)
    
    # Escribir los registros ficticios
    for registro in registros:
        escritor_csv.writerow(registro)

print(f'Datos guardados en {nombre_archivo}')