#!/usr/bin/env python

import sys
import joblib  # Importa la biblioteca necesaria para cargar el modelo

# Cargar el modelo entrenado
modelo = joblib.load('modelo_random_forest.pkl')

for linea in sys.stdin:
    # Supongamos que cada línea contiene una instancia de datos
    # Procesa la línea y realiza predicciones con el modelo
    datos = linea.strip().split(',')  # Suponiendo que los datos están separados por comas
    # Realiza cualquier preprocesamiento necesario en los datos
    # A continuación, realiza una predicción con el modelo
    resultado_prediccion = modelo.predict(datos)
    # Emite la salida del mapper (clave, valor)
    print(f'Prediccion\t{resultado_prediccion}')
