import pandas as pd
import joblib
from datetime import datetime

# Cargar el modelo entrenado
model = joblib.load("modelo_random_forest.pkl")

# Leer el archivo de datos nuevos
data_nuevos = pd.read_csv('datos/datos_nuevos.csv')

# Asegurarse de que las columnas coinciden con las características utilizadas en el modelo
required_columns = ['Tasa_Inflacion', 'Variacion_PIB', 'Precio_m2', 'Tamanho', 'Habitaciones']
if not all(col in data_nuevos.columns for col in required_columns):
    raise ValueError("El archivo de datos nuevos debe contener las columnas requeridas.")

# Realizar las predicciones
X_nuevos = data_nuevos[required_columns]  # Seleccionar las características
predicciones = model.predict(X_nuevos)  # Realizar las predicciones

# Agregar las predicciones al DataFrame original
data_nuevos['Precio_Predicho'] = predicciones

# Obtener la fecha actual en el formato AAAA-MM-DD
fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Nombre del archivo con la fecha actual
nombre_archivo = f'datos_predichos/precios_{fecha_actual}.csv'

# Guarda el DataFrame en el archivo CSV con el nombre que incluye la fecha actual
data_nuevos.to_csv(nombre_archivo, index=False)