# Ejercicios Dia 3

# 3.1. Declarar edad como variable entera

from math import pi
age = 30

# 3.2. Declarar altura como variable flotante

height = 1.70

# 3.3. Declarar una variable que almacene un numero complejo

num_complex = 3 + 5j

# 3.4. Escribir un script que solicite al usuario ingresar la base y altura del triángulo
#      y calcular el área del triángulo (área = 0.5 x bxh)

base = float(input("\nIngrese base: "))
height_tr = float(input("Ingrese altura: "))

area = 0.5 * (base * height_tr)

print(f"El área del triángulo es {round(area, 2)}\n")

# 3.5. Escribir un script que solicite al usuario ingresar los lados a,b y c del triángulo.
#      Calcular el perímetro del triángulo (perímetro = a + b + c)

a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

perimeter = a + b + c

print(f"El perímetro del triángulo es {round(perimeter, 2)}\n")

# 3.6. Obtener el largo y el ancho de un rectángulo usando las instrucciones.
#      Calcular el área (área = largo x ancho) y el perímetro (perímetro = 2 x (largo + ancho)).

large_rec = float(input("Ingrese largo: "))
width_rec = float(input("Ingrese ancho: "))

area_rec = large_rec * width_rec
perimeter_rec = 2 * (large_rec + width_rec)

print(f"El área del rectángulo es {round(area_rec, 2)}")
print(f"El perímetro del rectángulo es {round(perimeter_rec, 2)}\n")

# 3.7. Obtener el radio de un círculo usando las instrucciones. Calcula el área (área = pi x r x r)
#      y la circunferencia (c = 2 x pi x r), donde pi = 3,14

radius_cir = float(input("Ingrese radio: "))
pi = 3.14

area_cir = pi * (radius_cir ** 2)
circumference = 2 * pi * radius_cir

print(f"El área del círculo es {round(area_cir, 2)}")
print(f"La circunferencia del círculo es {round(circumference, 2)}\n")

# 3.8. Calcular la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2

m = 2
b = -2

slope = m
intersection_y = b
intersection_x = - intersection_y / slope

print(f"Ecuación: y = {m}x + {b}")
print(f"Pendiente (m): {slope}")
print(f"Intersección con el eje y (b): {intersection_y}")
print(f"Intersección con el eje x: {intersection_x}\n")

# 3.9. La pendiente es (m = y2 - y1/x2 - x1). Halla la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10).

x1, y1 = (2, 6)
x2, y2 = (6, 10)
m_2 = (y2 - y1) / (x2 - x1)

import math
distance = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)

print(f"Pendiente: {round(m_2, 2)}",)
print(f"Distancia euclidiana: {round(distance, 2)}", "\n")

# 3.10. Comparar las pendientes en las tareas 8 y 9.

print(f"Las pendientes son iguales: {m == m_2}\n")

# # 3.11. Calcular el valor de y (y = x^2 + 6x + 9). Intenta usar diferentes valores de x y determina en qué valor de x y será 0.

x = float(input("Ingresa el valor de x: "))
y = x**2 + 6*x + 9

print(f"El valor de y = x^2 + 6x + 9 es {y}\n")

# 3.12. Encontrar la longitud de 'python' y 'dragon' y haz una afirmación de comparación falsa

word1 = "python"
word2 = "dragon"

print(f"Las palabras python y dragon tiene diferente longitud: {len(word1) != len(word2)}\n")

# 3.13. Utilizar el operador and para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'

print("on" in word1 and "on" in word2, "\n")

# 3.14. 'Espero que este curso no esté lleno de jerga'. Usar el operador "in" para comprobar si hay jerga en la oración

prayer = "Espero que este curso no esté lleno de jerga"
result = "jerga" in prayer

print(f"Existe la palabra 'jerga' en la oración: {result}\n")

# 3.15. Encontrar la longitud del texto de Python y convierte el valor a flotante y conviértelo en cadena

len_python = float(len(word1))
len_py_str = str(len_python)

print(f"{len_py_str} es de tipo {type(len_py_str)}\n")

# 3.16. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no con Python?

num = float(input("Ingrese un número: "))
is_int = num % 2

if is_int == 0:
    print(f"{num} es un numero par\n")
else:
    print(f"{num} es un numero impar\n")

# 3.17. Comprobar si el tipo de '10' es igual al tipo de 10

print(f"'10' es igual a 10: {'10' == 10}\n")

# 3.18. Escribir un script que solicite al usuario ingresar las horas y la tarifa por hora. ¿Calcular el salario de la persona?

hours = float(input("Ingresar las horas: "))
rate = float(input("Ingresar la tarifa por hora: "))

salary = hours * rate

print(f"Tus ganancias semanales son {round(salary, 2)}\n")

# 3.19. Escribir un script que solicite al usuario ingresar el número de años que quiere vivir. Calcular la cantidad de segundos
#       que la persona viviría.

lived = int(input("Ingrese el número de años que qusiera vivir: "))
hrs_lived = 365 * 24 * lived
min_lived = hrs_lived * 60
sec_lived = min_lived * 60

print(f"Usted viviría por {sec_lived} segundos\n")
