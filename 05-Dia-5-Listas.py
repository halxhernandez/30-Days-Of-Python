# Ejercicios Nivel 1

# 5.1. Declarar una lista vacía

from audioop import reverse


my_list = list()

# 5.2. Declarar una lista con más de 5 elementos

list_2 = [1, 2, 3, 4, 5]
print(f"\n{list_2}\n")

# 5.3. Encontrar la longitud de la lista anterior

print(len(list_2), "\n")

# 5.4. Obtener el primer elemento, el elemento medio y el último elemento de la lista

first_element = list_2[0]
middle_element = list_2[2]
last_element = list_2[-1]

print(f"Primer elemento: {first_element}")
print(f"Elemento medio: {middle_element}")
print(f"Último elemento: {last_element}", "\n")

# 5.5. Declarar una lista llamada mixed_data_types, colocar (nombre, edad, altura, estado civil, dirección)

mixed_data_types = ["Alejandro", 30, 1.70, "Soltero", "Calle Loma S/N"]
print(mixed_data_types, "\n")

# 5.6. Declarar una variable de lista llamada it_companies y asignar valores iniciales Facebook, Google, Microsoft,
#      IBM, Oracle y Amazon

it_companies = ["Facebook", "Google", "Microsoft", "IBM", "Oracle", "Amazon"]

# 5.7. Imprimir la lista anterior

print(it_companies, "\n")

# 5.8. Imprimir el número de empresas en la lista

print("Numero de empresas", len(it_companies), "\n")

# 5.9. Imprimir la primera, segunda y última empresa

first_company = it_companies[0]
second_company = it_companies[1]
last_company = it_companies[-1]

print(f"Primera empresa: {first_company}")
print(f"Segunda empresa: {second_company}")
print(f"Última empresa: {last_company}\n")

# 5.10. Imprimir la lista después de modificar una de las empresas

it_companies[1] = "Tesla"
print(f"{it_companies}\n")

# 5.11. Añadir una empresa de TI a it_companies

it_companies.append("Apple")
print(f"{it_companies}\n")

# 5.12. Insertar una empresa de TI en medio de las lista de empresas

it_companies.insert(3, "Google")
print(f"{it_companies}\n")

# 5.13. Cambiar uno de los elementos de it_companies a mayúsculas

it_companies[2] = it_companies[2].upper()
print(f"{it_companies}\n")

# 5.14. Unir it_companies con una cadena #

print(f"#{it_companies}\n")

# 5.15. Comprobar si una determinada empresa existe

print(f"Existe 'Nvidia' en la lista: {'Nvidia' in it_companies}")
print(f"Existe 'Google' en la lista: {'Google' in it_companies}\n")

# 5.16. Ordenar la lista usando el método sort()

it_companies.sort()
print(f"{it_companies}\n")

# 5.17. Invertir la lista en orden descendente utilizando el método reverse()

it_companies.reverse()
print(f"{it_companies}\n")

# 5.18. Separar las primeras 3 empresas de la lista

print(f"{it_companies[:3]}\n")

# 5.19. Eliminar las últimas 3 empresas de la lista

del it_companies[-3:]
print(f"{it_companies}\n")

# 5.20. Elimina de la lista la o las empresas de TI intermedias

del it_companies[2]
print(f"{it_companies}\n")

# 5.21. Eliminar la primera empresa de TI de la lista

del it_companies[0]
print(f"{it_companies}\n")

# 5.22. Eliminar la o las empresas de TI intermedias de la lista

del it_companies[1]
print(f"{it_companies}\n")

# 5.23. Eliminar la última empresa de TI de la lista

del it_companies[-1]
print(f"{it_companies}\n")

# 5.24. Eliminar todas las empresas de la lista

it_companies.clear()
print(f"{it_companies}\n")

# 5.25. De las siguientes listas

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

# 5.26. Unir las listas y asinar el resultado a la variable full_stack, luego
#       insertas Python y SQL después de Redux

full_stack = front_end + back_end
redux_index = full_stack.index("Redux")

full_stack[redux_index + 1: redux_index + 1] = ["Python", "SQL"]
print(f"{full_stack}\n")

# Ejercicios Nilvel 2

# 5.27. Lo siguiente es una lista de 10 estudiantes por edades

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# -> Ordenar la lista y encontrar la edad mímina y máxima

ages.sort()
print(f"Edad mínima: {ages[0]}")
print(f"Edad máxima: {ages[-1]}\n")

# -> Agregar la edad mínima y máxima nuevamente a la lista

min_age = ages[0]
max_age = ages[-1]

ages.extend([min_age, max_age])
print(f"{ages}\n")

# -> Encontrar la edad media

avg_age = sum(ages) / len(ages)
print(f"Edad promedio: {avg_age}\n")

# -> Encontrar el rango de edades

range_age = max_age - min_age
print(f"Rango de edades: {range_age}\n")
