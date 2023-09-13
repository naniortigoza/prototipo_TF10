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
    if len(datos) == 6 and datos[0] != 'ID_Datos':
        # Este es un registro de datos_economicos.csv
        ID_Datos, ID_Zona, Fecha, Tasa_Inflacion, Variacion_PIB, Precio_m2 = datos
        
        # Extraer características de la fecha
        fecha_obj = datetime.strptime(Fecha, '%d/%m/%Y')
        dia = fecha_obj.day
        mes = fecha_obj.month
        anio = fecha_obj.year
        
        # Convertir características a números flotantes y pasar al modelo
        datos_para_modelo = [dia, mes, anio, float(Tasa_Inflacion), float(Variacion_PIB), float(Precio_m2)]
        resultado_prediccion = modelo.predict(datos_para_modelo)
        
        # Emitir resultados de predicción (clave, valor)
        print(f'Prediccion_Datos_Economicos\t{ID_Datos}\t{resultado_prediccion}')
    
    elif len(datos) == 10 and datos[0] != 'Propiedad_ID':
        # Este es un registro de datos_propiedades.csv
        Propiedad_ID, Zona_ID, Tipo_Propiedad, Ubicacion, Tamano, Habitaciones, Precio, Antiguedad, Caracteristicas, Ubicacion_Especial = datos
        
        # Emite resultados de predicción para datos de propiedades
        print(f'Prediccion_Datos_Propiedades\t{Propiedad_ID}\t{resultado_prediccion}')
