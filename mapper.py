#!/usr/bin/env python

import sys
import joblib  # Importa la biblioteca necesaria para cargar el modelo
from datetime import datetime  # Importa la biblioteca para trabajar con fechas

# Cargar el modelo entrenado
modelo = joblib.load('modelo_random_forest.pkl')

# Leer la primera línea que contiene los encabezados y omitirla
header = next(sys.stdin)

for linea in sys.stdin:
    # Supongamos que cada línea contiene datos de uno de los archivos
    datos = linea.strip().split(',')  # Suponiendo que los datos están separados por comas
    
    # Verificar el tipo de datos y omitir encabezados en cada archivo
    if len(datos) == 8 and datos[0] != 'ID_Datos':
        # Este es un registro de datos_economicos.csv
        ID_Datos, ID_Zona, Dia, Mes, Anio, Tasa_Inflacion, Variacion_PIB, Precio_m2 = datos
        
        # Convertir características a números flotantes y pasar al modelo
        datos_para_modelo = [
            [
                float(Tasa_Inflacion),
                float(Variacion_PIB),
                float(Precio_m2)
            ]
        ]  # Convierte a matriz 2D
        resultado_prediccion = modelo.predict(datos_para_modelo)
        
        # Emitir resultados de predicción (clave, valor)
        print(f'Prediccion_Datos_Economicos\t{ID_Datos}\t{resultado_prediccion}')
    
    elif len(datos) == 10 and datos[0] != 'Propiedad_ID':
        # Este es un registro de datos_propiedades.csv
        Propiedad_ID, Zona_ID, Tipo_Propiedad, Ubicacion, Tamano, Habitaciones, Precio, Antiguedad, Carac_Adicionales, Ubicacion_Especial = datos
        
        # Convertir características a números flotantes y pasar al modelo
        datos_para_modelo = [
            [
                float(Tamano),
                float(Habitaciones),
                float(Precio)
            ]
        ]  # Convierte a matriz 2D
        resultado_prediccion = modelo.predict(datos_para_modelo)
        
        # Emite resultados de predicción para datos de propiedades
        print(f'Prediccion_Datos_Propiedades\t{Propiedad_ID}\t{resultado_prediccion}')
