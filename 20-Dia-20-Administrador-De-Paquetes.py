# Ejercicios Dia 20

# 1. Leer la API de gatos y cats_api = ' https://api.thecatapi.com/v1/breeds ' y encuentre:
# a) el mínimo, máximo, media, mediana y desviación estándar del peso de los gatos en unidades métricas.
# b) el mínimo, máximo, media, mediana y desviación estándar de la esperanza de vida de los gatos en años.
# c) crear una tabla de frecuencia de país y raza de gatos.

import requests
import pandas as pd
import numpy as np

# URL de la API
cats_api = 'https://api.thecatapi.com/v1/breeds'

# 1. Leer la API
response = requests.get(cats_api)
breeds = response.json()

# Convertir la información relevante en un DataFrame
data = []
for breed in breeds:
    # Peso
    weight = breed.get('weight', {}).get('metric', '')
    if weight:
        try:
            weight_min, weight_max = map(float, weight.split(' - '))
        except:
            weight_min, weight_max = np.nan, np.nan
    else:
        weight_min, weight_max = np.nan, np.nan

    # Esperanza de vida
    life_span = breed.get('life_span', '')
    if life_span:
        try:
            life_min, life_max = map(float, life_span.split(' - '))
        except:
            life_min, life_max = np.nan, np.nan
    else:
        life_min, life_max = np.nan, np.nan

    # País de origen
    country = breed.get('origin', '')

    data.append({
        'name': breed.get('name', ''),
        'weight_min': weight_min,
        'weight_max': weight_max,
        'weight_avg': np.nanmean([weight_min, weight_max]),
        'life_min': life_min,
        'life_max': life_max,
        'life_avg': np.nanmean([life_min, life_max]),
        'origin': country
    })

df = pd.DataFrame(data)

# 1. Estadísticas del peso (en kg)
weight_stats = {
    'min': df['weight_avg'].min(),
    'max': df['weight_avg'].max(),
    'mean': df['weight_avg'].mean(),
    'median': df['weight_avg'].median(),
    'std': df['weight_avg'].std()
}

# 2. Estadísticas de la esperanza de vida (en años)
life_stats = {
    'min': df['life_avg'].min(),
    'max': df['life_avg'].max(),
    'mean': df['life_avg'].mean(),
    'median': df['life_avg'].median(),
    'std': df['life_avg'].std()
}

# 3. Tabla de frecuencia de país y raza
freq_table = pd.crosstab(df['origin'], df['name'])

# Mostrar resultados
print("Estadísticas del peso (kg):")
print(weight_stats)
print("\nEstadísticas de la esperanza de vida (años):")
print(life_stats)
print("\nTabla de frecuencia de país y raza:")
print(freq_table)
