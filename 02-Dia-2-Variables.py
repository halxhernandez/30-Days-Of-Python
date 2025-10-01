# Ejercicios Nivel 1

# 1.1. Declarar una variable de nombre, apellido, nombre completo, país, ciudad,
#     edad, año, es_casado, es_verdad y asignarle un valor

name = "Alejandro"
surname = "Hernández"
full_name = name + " " + surname
country = "México"
city = "CDMX"
age = 30.0
year = 2025
is_married = False
is_true = True

# 1.2. Declarar múltiples variables en una línea

sex, sisters, food, is_small = "Male", 2, "Mole", False

# Ejercicios Nivel 2

# 2.1. Verificar el tipo de datos de las variables anteriores

print(f"\nTipo de la variable name: {type(name)}")
print(f"Tipo de la variable surname: {type(surname)}")
print(f"Tipo de la variable full_name: {type(full_name)}")
print(f"Tipo de la variable country: {type(country)}")
print(f"Tipo de la variable city: {type(city)}")
print(f"Tipo de la variable age: {type(age)}")
print(f"Tipo de la variable year: {type(year)}")
print(f"Tipo de la variable is_married: {type(is_married)}")
print(f"Tipo de la variable is_true: {type(is_true)}")
print(f"Tipo de la variable sex: {type(sex)}")
print(f"Tipo de la variable sisters: {type(sisters)}")
print(f"Tipo de la variable food: {type(food)}")
print(f"Tipo de la variable is_small: {type(is_small)}\n")

# 2.2. Encontrar la longitud de la variable name

print(f"Longitud de {name}: {len(name)}")

# 2.3. Comparar la longitud de la variable name y surname

print(f"Diferencia de longitud entre {name} y {surname}: {len(name) -  len(surname)}\n")

# 2.4. Declarar 5 como num_one y 4 como num_two

num_one, num_two = 5, 4

# 2.5. Sumar num_one y num_two y asignar el valor a la variable total

total = num_one + num_two

# 2.6. Restar num_two de num_one y asignar el valor a la variable diff

diff = num_two - num_one

# 2.7. Multiplicar num_two y num_one y asignar el valor a la variable product

product = num_two * num_one

# 2.8. Dividir num_one por num_two y asignar el valor a la variable division

division = num_one / num_two

# 2.9. Encontrar el módulo de num_one por num_two y asignar el valor a la variable remainder

remainder = num_one % num_two

# 2.10. Calcular num_one elevado a num_two y asignar el valor a la variable exp

exp = num_one ** num_two

# 2.11. Encontrar la división de piso de num_one por num_two y asignar el valor a la variable floor_division

floor_division = num_one // num_two

# 2.12. El radio de un círculo es 30 metros

import math
radius = 30

# i. Calcular el área del círculo y asignar el valor a la variable area_of_circle

area_of_circle = math.pi * (radius ** 2)

# ii. Calcular las circunferencia del círculo y asignar el valor a la variable circum_of_circle

circum_of_cicle = (2 * math.pi) * radius

# iii. Tomar el radio como entrada del usuario y calcular el área

input_area = float(input("Ingrese el radio: "))
area = math.pi * (input_area ** 2)

print(f"El área de un círculo con {input_area} m. de radio es {round(area, 2)} m. cuadrados\n")

# 2.13. Obtener el nombre, apellido, pais y edad de un usuario y almacenar el valor en los
#       nombres de las variables correspondientes

name = input("Ingresa tu nombre: ")
surname = input("Ingresa tu apellido: ")
country = input("Ingresa tu país de residencia: ")
age = int(input("Ingresa tu edad: "))

print(f"\nname = {name}")
print(f"surname = {surname}")
print(f"country = {country}")
print(f"age = {age}\n")
