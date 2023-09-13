import pandas as pd
import joblib
from sklearn.model_selection import train_test_split        # pip install scikit-learn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos
datos_economicos = pd.read_csv('datos/datos_economicos.csv')
datos_propiedades = pd.read_csv('datos/datos_propiedades.csv')

# Unir los datos por Zona_ID
datos_combinados = datos_propiedades.merge(datos_economicos, left_on='Zona_ID', right_on='Zona_ID', how='inner')

# Preparar los datos
X = datos_combinados[['Tasa_Inflacion', 'Variacion_PIB', 'Tamanho', 'Habitaciones', 'Tipo_Propiedad']]
y = datos_combinados['Precio']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=200, random_state=42, max_depth=10)  # Añadir max_depth para evitar sobreajuste
rf_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = rf_model.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio (MSE): {mse}')

# Calcular el coeficiente de determinación R^2
r2 = r2_score(y_test, y_pred)
print(f'Coeficiente de determinación (R^2): {r2}')

# Guardar el modelo entrenado en un archivo
modelo_archivo = 'modelo_random_forest.pkl'
joblib.dump(rf_model, modelo_archivo)
print(f'Modelo guardado en {modelo_archivo}')

# Exportar los resultados de predicción a un archivo CSV
resultados = pd.DataFrame({'Precio_Real': y_test, 'Precio_Predicho': y_pred})
resultados.to_csv('datos/resultados_prediccion.csv', index=False)

# Obtener la importancia de las variables
importancias = rf_model.feature_importances_
print('\nImportancia de las variables:')
for i, importancia in enumerate(importancias):
    print(f'Variable {X.columns[i]}: {importancia}')


