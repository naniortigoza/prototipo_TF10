#!/usr/bin/env python

import sys
import csv

# Inicializa un objeto CSV para escribir los resultados
csv_writer = csv.writer(sys.stdout)

# Escribe la primera fila de encabezados en el archivo CSV
csv_writer.writerow(['Propiedad_ID', 'Precio_Predicho'])

# Procesa las líneas de entrada
for linea in sys.stdin:
    # Parsea la entrada del mapper
    partes = linea.strip().split('\t')

    # Verifica si hay suficientes partes
    if len(partes) == 3:
        clave, Propiedad_ID, valor_prediccion = partes

        # Escribe los resultados al archivo CSV
        if clave == 'Prediccion':
            csv_writer.writerow([Propiedad_ID, valor_prediccion])
    else:
        print(f"Error en la línea: {linea.strip()}")
