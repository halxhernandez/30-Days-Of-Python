# Ejercicios Nivel 1

# 1. Escribir una función que cuente el número de líneas y palabras de un texto. Todos los archivos estan en la carpeta de datos:
# a) Leer el archivo obama_speech.txt y contar el número de líneas y palabras. Hacer lo mismo con los archivos michelle_obama_speech.txt,
#    donal_speech.txt y melina_trump_speech.txt

def count_lines_and_words(file_path):
    line_count = 0
    word_count = 0

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)

    return line_count, word_count


path_obama = "./data/obama_speech.txt"
path_michelle = "./data/michelle_obama_speech.txt"
path_donald = "./data/donald_speech.txt"
path_melina = "./data/melina_trump_speech.txt"

lines_obama, words_obama = count_lines_and_words(path_obama)
lines_michelle, words_michelle = count_lines_and_words(path_michelle)
lines_donald, words_donald = count_lines_and_words(path_donald)
lines_melina, words_melina = count_lines_and_words(path_melina)

print(f"\nEl archivo obama tiene {lines_obama} líneas y {words_obama} palabras")
print(f"El archivo michelle tiene {lines_michelle} líneas y {words_michelle} palabras")
print(f"El archivo donald tiene {lines_donald} líneas y {words_donald} palabras")
print(f"El archivo melina tiene {lines_melina} líneas y {words_melina} palabras\n")

# 2. Leer el archivo de datos Countries_data.json en el directorio de datos y cree una función que encuentre los diez idiomas más hablados

import json
from collections import Counter

def most_spoken_languages(filename, n):
    with open(filename, "r", encoding="utf-8") as f:
        countries = json.load(f)

    languages = []
    for country in countries:
        if "languages" in country:
            languages.extend(country["languages"])

    language_counts = Counter(languages)

    top_languages = [(count, lang) for lang, count in language_counts.most_common(n)]

    return top_languages

print(f"{most_spoken_languages(filename='./data/countries_data.json', n=10)}")
print(f"{most_spoken_languages(filename='./data/countries_data.json', n=3)}\n")

# 3. Lea el archivo de datos Countries_data.json en el directorio de datos, cree una función que genere una lista de los diez países más poblados

def most_populated_countries(filename, n):
    with open(filename, "r", encoding="utf-8") as f:
        countries = json.load(f)

    country_populations = [
        {'country': country['name'], 'population': country['population']}
        for country in countries if 'population' in country
    ]

    sorted_countries = sorted(country_populations, key=lambda x: x['population'], reverse=True)

    return sorted_countries[:n]

print(f"{most_populated_countries(filename='./data/countries_data.json', n=10)}")
print(f"{most_populated_countries(filename='./data/countries_data.json', n=3)}\n")

# Ejercicios Nivel 2

# 4. Extraiga todas las direcciones de correo electrónico entrantes como una lista del archivo email_exchange_big.txt

import re

def extract_emails(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(pattern, text)

    unique_emails = sorted(set(emails))

    return unique_emails

emails = extract_emails("./data/email_exchanges_big.txt")
print(f"{emails}\n")

# 5. Encuentra las palabras más comunes en inglés. Llama a tu función find_most_common_words. Esta aceptará dos parámetros: una cadena o un archivo y un entero positivo que indica el número de palabras. Tu función devolverá un array de tuplas en orden descendente. Consulta el resultado.

def find_most_common_words(filename, n):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r'\b[a-z]+\b', text)

    word_counts = Counter(words)

    top_words = [(count, word) for word, count in word_counts.most_common(n)]

    return top_words

# 6. Utilice la función find_most_frequent_words para encontrar: a) Las diez palabras más frecuentes utilizadas en el discurso de Obama b) Las diez palabras más #    frecuentes utilizadas en el discurso de Michelle c) Las diez palabras más frecuentes utilizadas en el discurso de Trump d) Las diez palabras más frecuentes
#    utilizadas en el discurso de Melina

print(f"Las diez palabras más frecuentes en el discuros de Obama:")
print(f"{find_most_common_words(path_obama, 10)}\n")

print(f"Las diez palabras más frecuentes en el discuros de Michelle:")
print(f"{find_most_common_words(path_michelle, 10)}\n")

print(f"Las diez palabras más frecuentes en el discuros de Trump:")
print(f"{find_most_common_words(path_donald, 10)}\n")

print(f"Las diez palabras más frecuentes en el discuros de Melina:")
print(f"{find_most_common_words(path_melina, 10)}\n")
