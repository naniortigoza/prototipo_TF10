#!/usr/bin/env python

import sys

# Inicializa variables para realizar cálculos de resumen
total_predicciones = 0
suma_predicciones = 0.0

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

# Emite el resultado final
print(f'Promedio_Predicciones_Propiedades\t{promedio_predicciones}')
