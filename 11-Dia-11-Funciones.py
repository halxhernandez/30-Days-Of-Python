# Ejercicios Nivel 1

# 1. Declarar la función add_two_numbers. Está función debe aceptar dos parámetros y devolver la suma

def add_two_numbers(num1, num2):
    add = num1 + num2
    return add

print(f"\nLa suma de 2 y 3 es {add_two_numbers(2, 3)}\n")

# 2. El área de un círculo se calcula de la siguiente manera: area = π x r x r. Escribir una función que
#    calcule el área de un círculo

def area_of_circle(radius):
    PI = 3.1416
    area = PI * (radius ** 2)
    return round(area, 2)

print(f"El área de un círculo con 5 cm de radio es {area_of_circle(5)} cm2\n")

# 3. Escribir una función llamada add_all_nums que tome cualquier número de argumentos y los sume.

def add_all_nums(*nums):
    add = 0
    for num in nums:
        add += num
    return add

print(f"La suma de 3, 4, 5 es {add_all_nums(3, 4, 5)}")
print(f"La suma de 3, 4, 5, 6, 7, 8, 9, 10 es {add_all_nums(3, 4, 5, 6, 7, 8, 9, 10)}\n")

# 4. La temperatura en °C se puede convertir a °F usando la formula: °F = (°C x 9/5) + 32
#    Escribir una función que convierta °C a °F

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

print(f"50°C correnponden a {convert_celsius_to_fahrenheit(50)}°F\n")

# 5. Escribir una función llamada check_season que tome un parámetro de mes y devuelva la temporada:
#    Otoño, Invierno, Primevera o Verano

def check_season(month):

    if month.lower() in ["marzo", "abril", "mayo"]:
        return "Primavera"

    elif month.lower() in ["junio", "julio", "agosto"]:
        return "Verano"

    elif month.lower() in ["septiembre", "octubre", "noviembre"]:
        return "Otoño"

    else:
        return "Invierno"

print(f"El mes de Marzo corresponde a la estación de {check_season("marzo")}")
print(f"El mes de Julio corresponde a la estación de {check_season("Julio")}")
print(f"El mes de Octubre corresponde a la estación de {check_season("Octubre")}")
print(f"El mes de Diciembre corresponde a la estación de {check_season("diciembre")}\n")

# 6. Escribir una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal

def calculate_slope(a, b, c):
    slope = -a / b
    return round(slope, 2)

print(f"La pendiente de la ecuación 2x-2y+6=0 es {calculate_slope(2, -3, 6)}\n")

# 7. La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el
#    conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn .

import math
import re

def solve_quadratic_eqn(a, b, c):

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = round((-b + math.sqrt(discriminant)) / (2*a), 2)
        x2 = round((-b - math.sqrt(discriminant)) / (2*a), 2)
        return x1, x2

    elif discriminant == 0:
        x = round(-b / (2*a), 2)
        return x, x

    else:
        real = round(-b / (2*a), 2)
        imag = round(math.sqrt(abs(discriminant)) / (2*a), 2)
        return complex(real, imag), complex(real, -imag)

print(f"Las raices de la ecuación x²-3x+2=0 son {solve_quadratic_eqn(1, -3, 2)}")
print(f"Las raices de la ecuación x²-2x+1=0 son {solve_quadratic_eqn(1, -2, 1)}")
print(f"Las raices de la ecuación x²+x+1=0 son {solve_quadratic_eqn(1, 1, 1)}\n")

# 8. Declarar una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista

def print_list(ls):
    for i in ls:
        print(i)

frutas = ["Manzana", "Banana", "Naranja", "Uva"]
print_list(frutas)
print("")

# 9. Declarar una función llamada reverse_list. Esta toma un array como parámetro y devuelve su valor inverso (usando bucles).

def reverse_list(ls):
    reversed_list = []
    for i in range(len(ls) - 1, -1, -1):
        reversed_list.append(ls[i])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]), "\n")

# 10. Declarar una función llamada capitalize_list_items. Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas

def capitalize_list_items(ls):
    capitalize_list = []
    for i in ls:
        capitalize_list.append(i.upper())
    return capitalize_list

text = ["alejandro", "hernandez", "rodriguez"]
print(capitalize_list_items(text), "\n")

# 11. Declara una función llamada add_item. Esta función toma como parámetros una lista y un elemento. Devuelve una lista con el elemento añadido al final

def add_item(ls, value):
    ls.append(value)
    return ls

food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5), "\n")

# 12. Declarar una función llamada remove_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado

def remove_item(ls: list, value):
    ls.remove(value)
    return ls

food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "Mango"))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3), "\n")

# 13. Declarar una función llamada sum_of_numbers. Esta función toma un parámetro numérico y suma todos los números en ese rango

def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100), "\n")

# 14. Declarar una función llamada sum_of_odds. Esta función toma un parámetro numérico y suma todos los números impares en ese rango

def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(15), "\n")

# 15. Declarar una función llamada sum_of_even. Esta función toma un parámetro numérico y suma todos los números pares en ese rango

def sum_of_even(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(15), "\n")

# Ejercicios Nivel 2

# 16. Declarar una función llamada evens_and_odds. Esta función toma un entero positivo como parámetro y cuenta el número de pares e impares en el número

def evens_and_odds(num):
    odds = []
    evens = []

    for i in range(num + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    print(f"Los números pares son {len(evens)}")
    print(f"Los números impares son {len(odds)}\n")

evens_and_odds(100)

# 17. Llamar a la función factorial, tomar un número entero como parámetro y devolver un factorial del número

def factorial(num):
    if num < 0:
        return "El factorial no está definido para números negativos."

    total = 1
    for i in range(1, num + 1):
        total *= i
    return total

print(factorial(5))
print(factorial(0))
print(factorial(-3), "\n")

# 18. Llamar a una función is_empty, tomar un parámetro y verifica si está vacío o no

def is_empty(ls):
    return len(ls) == 0

print(is_empty([]))
print(is_empty([1, 2, 3]), "\n")

# 19. Escribir diferentes funciones que acepten listas. Estas funciones deben calcular la media, la mediana, la moda, el rango,
#     la varianza y la desviación estándar (desviación estándar)

import statistics

def mean(ls):
    return statistics.mean(ls)

def median(ls):
    return statistics.median(ls)

def mode(ls):
    return statistics.mode(ls)

def data_range(ls):
    return max(ls) - min(ls)

def variance(ls):
    return statistics.variance(ls)

def std_deviation(ls):
    return statistics.stdev(ls)

data = [2, 3, 5, 7, 3, 5, 8, 3]

print("Media:", mean(data))
print("Mediana:", median(data))
print("Moda:", mode(data))
print("Rango:", data_range(data))
print("Varianza:", variance(data))
print("Desviación estándar:", std_deviation(data), "\n")

# Ejercicios Nivel 3

# 20. Escriba una función llamada is_prime, que verifique si un número es primo

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(12), "\n")

# 21. Escriba una función que verifique si todos los elementos son únicos en la lista

def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 3]), "\n")

# 22. Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos

def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(x, first_type) for x in lst)

print(all_same_type([1, 2, 3]))
print(all_same_type([1, "2", 3]))
print(all_same_type([]), "\n")

# 23. Escriba una función que verifique si la variable proporcionada es una variable de Python válida

def is_valid_variable(name):
    import keyword
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True

print(is_valid_variable("my_var"))
print(is_valid_variable("2var"))
print(is_valid_variable("for"), "\n")
