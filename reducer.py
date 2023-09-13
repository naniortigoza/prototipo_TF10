#!/usr/bin/env python

import sys

# Inicializa variables para realizar cálculos de resumen
total_predicciones = 0
suma_predicciones = 0.0

# Lista para almacenar los resultados
resultados = []

for linea in sys.stdin:
    # Parsea la entrada del mapper
    clave, Propiedad_ID, valor_prediccion = linea.strip().split('\t')
    
    # Realiza cálculos de resumen con los valores
    valor_prediccion = float(valor_prediccion)
    
    if clave == 'Prediccion':
        total_predicciones += 1
        suma_predicciones += valor_prediccion

# Calcula estadísticas finales
promedio_predicciones = suma_predicciones / total_predicciones if total_predicciones > 0 else 0

# Agrega el resultado a la lista de resultados
resultados.append(f'Promedio_Predicciones_Propiedades\t{promedio_predicciones}')

# Escribe los resultados en un archivo CSV
with open('resultados.csv', 'w') as archivo_salida:
    archivo_salida.write('\n'.join(resultados))
