#!/usr/bin/env python

import sys

# Inicializa variables para realizar cálculos de resumen
total_predicciones_economicas = 0
suma_predicciones_economicas = 0.0

for linea in sys.stdin:
    # Parsea la entrada del mapper
    clave, ID, valor_prediccion = linea.strip().split('\t')
    
    # Realiza cálculos de resumen con los valores
    valor_prediccion = float(valor_prediccion)
    
    if clave == 'Prediccion_Datos_Economicos':
        total_predicciones_economicas += 1
        suma_predicciones_economicas += valor_prediccion

# Calcula estadísticas finales
promedio_predicciones_economicas = suma_predicciones_economicas / total_predicciones_economicas

# Emite el resultado final
print(f'Promedio_Predicciones_Datos_Economicos\t{promedio_predicciones_economicas}')
