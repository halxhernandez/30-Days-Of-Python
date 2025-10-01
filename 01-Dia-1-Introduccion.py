# Ejercicios Nivel 1

# 1.1. Operaciones básicas

x = 3
y = 4

add = x + y
sub = x - y
mul = x * y
mod = x % y
div = x / y
exp = x ** y
f_div = x // y

print(f"\nSuma: {add}")
print(f"Resta: {sub}")
print(f"Multiplicación: {mul}")
print(f"Módulo: {mod}")
print(f"División: {div}")
print(f"Exponencial: {exp}")
print(f"División de piso: {f_div}")

# 1.2. Escribir cadenas e imprimirlas

name = "Alejandro"
surname = "Hernández"
country = "México"
hobbie = "Estoy disfrutando de 30 días de Python"

print(f"\nHola, mi nombre es {name} {surname}, soy de {country} y {hobbie}\n")

# 1.3. Comprobar tipos de datos

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finlandia"]))
print(type("Alejandro"))
print(type("México"), "\n")

# Ejercicios Nivel 2

# 2.1. Diferentes tipos de datos

num_int = 10
num_float = 10.5
num_complex = 10 + 4j
string = "Alejandro"
data_bool = True
data_list = ["Alejandro", 30, 1.80, "Pandas"]
data_tuple = ("Alejandro", 30, 1.80, "Pandas")
data_set = {1, 2, 3, 4, 5}
data_dict = {"Name": "Alejandro", "Age": 30, "Sex": "Male"}

print(type(num_int))
print(type(num_float))
print(type(num_complex))
print(type(string))
print(type(data_bool))
print(type(data_list))
print(type(data_tuple))
print(type(data_set))
print(type(data_dict), "\n")

# 2.2. Calcular la distancia euclidiana entre (2, 3) y (10, 8)

import math

p1, p2 = (2, 3)
q1, q2 = (10, 8)

distance = math.sqrt((p1 - q1)**2 + (p2 - q2)**2)
print(f"Euclidean distance: {distance}", "\n")
