# Ejercicios Nivel 1

import re
from collections import Counter

# 1. ¿Cuál es la word más frecuente en el siguiente párrafo?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.findall(r"\b\w+\b", paragraph)
counter = Counter(words)

sorted_words = sorted(
    [(count, word) for word, count in counter.items()],
    key=lambda x: x[0], reverse=True)

print(f"\n{sorted_words}\n")

# 2. La posición de algunas partículas en el eje x horizontal es -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8
#    en la dirección positiva. Extraer estos números de todo el texto y calcule la distancia entre las dos partículas más alejadas.

txt = "La posición de algunas partículas en el eje x horizontal es -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8 en la dirección positiva."


numbers = re.findall(r"-?\d+", txt)
numbers = [int(n) for n in numbers]

distance = max(numbers) - min(numbers)

print(f"Números extraídos: {numbers}")
print(f"Distancia entre las partículas más alejadas: {distance}\n")

# Ejercicios Nivel 2

# 3. Escribir un patrón que identifique si una cadena es una variable de Python válida

import keyword

def is_valid_variable(name):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.match(pattern, name)) and name not in keyword.kwlist

test = ["first_name", "first-name", "1first_name", "firstname"]

for word in test:
    print(f"{word} → {is_valid_variable(word)}")

# Ejercicios Nivel 3

# 4. Limpiar el siguiente texto. Después de limpiarlo, contar las tres palabras más frecuentes en la cadena

import re
from collections import Counter

# Texto original
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing;
&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)
    counter = Counter(words)
    return [(count, word) for word, count in counter.most_common(3)]

cleaned_text = clean_text(sentence)
print(f"\n{cleaned_text}")
print(f"{most_frequent_words(cleaned_text)}\n")
