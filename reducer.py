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
    clave, Propiedad_ID, valor_prediccion = linea.strip().split('\t')
    
    # Escribe los resultados al archivo CSV
    if clave == 'Prediccion':
        csv_writer.writerow([Propiedad_ID, valor_prediccion])
