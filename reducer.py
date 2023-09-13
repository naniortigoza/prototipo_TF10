#!/usr/bin/env python

import sys

# Inicializa variables para realizar cálculos de resumen
total_predicciones = 0
suma_predicciones = 0.0

for linea in sys.stdin:
    # Parsea la entrada del mapper
    clave, valor = linea.strip().split('\t')
    
    # Realiza cálculos de resumen con los valores
    if clave == 'Prediccion':
        valor_prediccion = float(valor)
        total_predicciones += 1
        suma_predicciones += valor_prediccion

# Calcula estadísticas finales
promedio_predicciones = suma_predicciones / total_predicciones

# Emite el resultado final
print(f'Promedio_Predicciones\t{promedio_predicciones}')
