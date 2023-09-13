import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos con nombres de columnas
columnas_datos_economicos = ['ID_Datos', 'Zona_ID', 'Dia', 'Mes', 'Anho', 'Tasa_Inflacion', 'Variacion_PIB', 'Precio_m2']
columnas_datos_propiedades = ['Propiedad_ID', 'Zona_ID', 'Tipo_Propiedad', 'Ubicacion', 'Tamanho', 'Habitaciones', 'Precio', 'Antiguedad', 'Carac_Adicionales', 'Ubicacion_Especial']

datos_economicos = pd.read_csv('datos/datos_economicos.csv', names=columnas_datos_economicos, header=None)
datos_propiedades = pd.read_csv('datos/datos_propiedades.csv', names=columnas_datos_propiedades, header=None)

# Unir los datos por Zona_ID
datos_combinados = datos_propiedades.merge(datos_economicos, left_on='Zona_ID', right_on='Zona_ID', how='inner')

# Preparar los datos
X = datos_combinados[['Tasa_Inflacion', 'Variacion_PIB', 'Precio_m2', 'Tamanho', 'Habitaciones']]
y = datos_combinados['Precio']

# Ajustar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=200, random_state=42, max_depth=10)  # Añadir max_depth para evitar sobreajuste
rf_model.fit(X, y)

# Realizar predicciones en el conjunto de datos
y_pred = rf_model.predict(X)

# Redondear los valores predichos a números enteros
y_pred_enteros = [round(valor) for valor in y_pred]

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y, y_pred)
print(f'Error cuadrático medio (MSE): {mse}')

# Calcular el coeficiente de determinación R^2
r2 = r2_score(y, y_pred)
print(f'Coeficiente de determinación (R^2): {r2}')

# Obtener la importancia de las variables
importancias = rf_model.feature_importances_
print('\nImportancia de las variables:')
for i, importancia in enumerate(importancias):
    print(f'Variable {X.columns[i]}: {importancia}')

# Exportar los resultados de predicción a un archivo CSV con el precio real y predicho (enteros)
resultados = pd.DataFrame({'Precio_Real': y, 'Precio_Predicho': y_pred_enteros})
resultados.to_csv('datos/resultados_prediccion.csv', index=False)

# Guardar el modelo entrenado en un archivo
modelo_archivo = 'modelo_random_forest.pkl'
joblib.dump(rf_model, modelo_archivo)
print(f'Modelo guardado en {modelo_archivo}')
