#!/usr/bin/env python

import sys
import joblib  # Importa la biblioteca necesaria para cargar el modelo
import pandas as pd  # Importa Pandas para manipular los datos

# Cargar el modelo entrenado
modelo = joblib.load('modelo_random_forest.pkl')

# Leer la primera línea que contiene los encabezados y omitirla
header = next(sys.stdin)

# Crear un DataFrame para almacenar los datos combinados
datos_combinados = []

for linea in sys.stdin:
    # Supongamos que cada línea contiene datos de uno de los archivos
    datos = linea.strip().split(',')  # Suponiendo que los datos están separados por comas
    
    # Verificar el tipo de datos y omitir encabezados en cada archivo
    if len(datos) == 8 and datos[0] != 'ID_Datos':
        # Este es un registro de datos_economicos.csv
        ID_Datos, ID_Zona, Dia, Mes, Anho, Tasa_Inflacion, Variacion_PIB, Precio_m2 = datos
        
        # Convertir características a números flotantes
        datos_para_modelo = [
            float(Tasa_Inflacion),
            float(Variacion_PIB),
            float(Precio_m2),
        ]
        
        datos_combinados.append(datos_para_modelo)
    
    elif len(datos) == 10 and datos[0] != 'Propiedad_ID':
        # Este es un registro de datos_propiedades.csv
        Propiedad_ID, Zona_ID, Tipo_Propiedad, Ubicacion, Tamanho, Habitaciones, Precio, Antiguedad, Carac_Adicionales, Ubicacion_Especial = datos
        
        # Convertir características a números flotantes
        datos_para_modelo = [
            float(Tamanho),
            float(Habitaciones),
            float(Precio),
        ]
        
        datos_combinados.append(datos_para_modelo)

# Convertir la lista de datos combinados en un DataFrame
datos_para_modelo_df = pd.DataFrame(datos_combinados)

# Realizar predicciones en el conjunto de datos combinados
resultados_prediccion = modelo.predict(datos_para_modelo_df)

# Emitir resultados de predicción (clave, valor)
for resultado in resultados_prediccion:
    print(f'Prediccion\t{resultado}')
