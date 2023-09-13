#!/usr/bin/env python

import sys
import joblib  # Importa la biblioteca necesaria para cargar el modelo

# Cargar el modelo entrenado
modelo = joblib.load('modelo_random_forest.pkl')

# Leer la primera línea que contiene los encabezados y omitirla
header = next(sys.stdin)

for linea in sys.stdin:
    # Supongamos que cada línea contiene datos de uno de los archivos
    datos = linea.strip().split(',')  # Suponiendo que los datos están separados por comas
    
    # Verificar si la línea tiene el número correcto de campos
    if len(datos) == 6 and datos[0] != 'Propiedad_ID':
        # Este es un registro de datos_propiedades.csv
        Propiedad_ID, Tasa_Inflacion, Variacion_PIB, Precio_m2, Tamanho, Habitaciones = datos
        
        # Convertir características a números flotantes
        datos_para_modelo = [
            float(Tasa_Inflacion),
            float(Variacion_PIB),
            float(Precio_m2),
            float(Tamanho),
            float(Habitaciones),
        ]
        
        # Realizar la predicción para esta línea
        resultado_prediccion = modelo.predict([datos_para_modelo])

        # Emitir resultados de predicción (clave, valor)
        print(f'Prediccion\t{Propiedad_ID}\t{resultado_prediccion[0]}')
