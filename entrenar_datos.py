import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos
datos_economicos = pd.read_csv('datos/datos_economicos.csv')
datos_propiedades = pd.read_csv('datos/datos_propiedades.csv')

# Unir los datos por Zona_ID
datos_combinados = datos_propiedades.merge(datos_economicos, left_on='ID_Datos', right_on='ID_Datos', how='inner')

# Preparar los datos
X = datos_combinados[['Tasa_Inflacion', 'Variacion_PIB', 'Precio_m2', 'Tamanho', 'Habitaciones']]
y = datos_combinados['Precio']

# Ajustar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)  # Añadir max_depth para evitar sobreajuste
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

# Guardar el modelo entrenado en un archivo
modelo_archivo = 'modelo_random_forest.pkl'
joblib.dump(rf_model, modelo_archivo)
print(f'Modelo guardado en {modelo_archivo}')
