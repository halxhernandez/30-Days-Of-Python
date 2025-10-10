# Ejercicios Nivel 1

# 1. Escribir una función que genere un random_iser_id de seis dígitos/caracteres

import random
import string
from turtle import color

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = "".join(random.choices(characters, k=6))
    return user_id

print(f"\n{random_user_id()}\n")

# 2. Modificar la tarea anterior. Declarar una función llamada user_id_gen_by_user. No acepta parámetros, pero acepta dos entradas mediante
#    input(). Una de las entradas es el número de caracteres y la otra, el número de ID que se generarán

def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de IDs que desea generar: "))

    characters = string.ascii_letters + string.digits
    ids = []

    for i in range(num_ids):
        user_id = "".join(random.choices(characters, k=num_chars))
        ids.append(user_id)

    return "\n".join(ids)

print(f"\n{user_id_gen_by_user()}\n")

# 3. Escribir una función llamada rgb_color_gen. Esta generará colores RGB (tres valores de 0 a 255 cada uno)

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r}, {g}, {b})"

print(f"\n{rgb_color_gen()}\n")

# Ejercicios Nivel 2

# 4. Escribir una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales
#    escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, af.

def list_of_hexa_colors(n):
    colors = []

    for _ in range(n):
        color = "#" + "".join(random.choices("0123456789abcdef", k=6))
        colors.append(color)
    return colors

print(f"\n{list_of_hexa_colors(5)}\n")

# 5. Escribir una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz

def list_of_rgb_colors(n):
    colors = []

    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        color = f"rgb({r}, {g}, {b})"
        colors.append(color)
    return colors

print(f"\n{list_of_rgb_colors(5)}\n")

# 6. Escribir una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb

def generate_colors(type, n):
    colors = []

    if type.lower() == "hexa":
        for _ in range(n):
            color = "#" + "".join(random.choices("0123456789abcdef", k=6))
            colors.append(color)

    elif type.lower() == "rgb":
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r}, {g}, {b})")

    return colors

print(generate_colors("hexa", 3))
print(f"{generate_colors("rgb", 3)}\n")

# Ejercicios Nivel 3

# 7. Llamar a una función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria

def shuffle_list(list_items):
    shuffled_list = list_items.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

numbers = [1, 2, 3, 4, 5, 6, 7]
print(f"Original: {numbers}")
print(f"Shuffled: {shuffle_list(numbers)}\n")

# 8. Escribir una función que devuelva una matriz de siete números aleatorios del 0 al 9. Todos los números deben ser únicos

def unique_random_numbers():
    random_numbers = random.sample(range(10), 7)
    return random_numbers

print(f"{unique_random_numbers()}\n")
