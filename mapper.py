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
    
    # Verificar el tipo de datos y omitir encabezados en cada archivo
    if len(datos) == 6 and datos[0] != 'ID_Datos':
        # Este es un registro de datos_economicos.csv
        ID_Datos, ID_Zona, Fecha, Tasa_Inflacion, Variacion_PIB, Precio_m2 = datos
        
        # Realiza cualquier preprocesamiento necesario en estos datos
        # A continuación, realiza una predicción con el modelo
        
        # Emitir resultados de predicción (clave, valor)
        print(f'Prediccion_Datos_Economicos\t{ID_Datos}\t{modelo.predict(datos)}')
    
    elif len(datos) == 10 and datos[0] != 'Propiedad_ID':
        # Este es un registro de datos_propiedades.csv
        Propiedad_ID, Zona_ID, Tipo_Propiedad, Ubicacion, Tamano, Habitaciones, Precio, Antiguedad, Caracteristicas, Ubicacion_Especial = datos
        
        # Realiza cualquier preprocesamiento necesario en estos datos
        # A continuación, realiza una predicción con el modelo
        
        # Emitir resultados de predicción (clave, valor)
        print(f'Prediccion_Datos_Propiedades\t{Propiedad_ID}\t{modelo.predict(datos)}')
