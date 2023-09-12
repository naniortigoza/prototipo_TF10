import pandas as pd

# Rutas de los archivos CSV
archivo_csv1 = 'datos/datos_propiedades_externo.csv'
archivo_csv2 = 'datos/datos_propiedades_interno.csv'

# Leer los archivos CSV en DataFrames
df1 = pd.read_csv(archivo_csv1)
df2 = pd.read_csv(archivo_csv2)

# Concatenar los DataFrames verticalmente (uno debajo del otro)
df_concatenado = pd.concat([df1, df2], ignore_index=True)

# Guardar el DataFrame concatenado en un nuevo archivo CSV
archivo_concatenado = 'datos/datos_propiedades.csv'
df_concatenado.to_csv(archivo_concatenado, index=False)

print(f'Archivos concatenados y guardados en {archivo_concatenado}')
