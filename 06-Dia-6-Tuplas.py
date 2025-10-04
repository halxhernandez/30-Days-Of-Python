# Ejercicios Nivel 1

# 1.1. Crear una tupla vacía

tpl = tuple()

# 1.2. Crear una tupla que contenga los nombres de tus hermanos y hermanas

sisters = ("Aylin", "Dariana", "Alya")
brothers = ("Elias", "Eithan")

print(f"\n{sisters}")
print(f"{brothers}\n")

# 1.3. Unir las tuplas anteriores

tuple_brothers = sisters + brothers
print(f"{tuple_brothers}\n")

# 1.4. ¿Cuántos hermanos tienes?

print(f"Tengo {len(tuple_brothers)} hermanos\n")

# 1.5. Mofidicar la tupla de hermanos y agregar el nombre de tu padre y madre y
#      asignarlo a family_members

family_members = tuple_brothers + ("Ciro", "Marcelina")
print(f"{family_members}\n")

# Ejercicios Nivel 2

# 2.1. Desempaquetar hermanos y padres de los miembros de la familia

brothers, parents = family_members[:5], family_members[5:]
print(f"{brothers}, {parents}\n")

# 2.2. Crear tuplas de frutas, verduras y productos animales. Unir las tres tuplas y
#      asignarlas a una variable llamada food_stuff_tp

fruits = ("Manzana", "Mango", "Sandia", "Guayaba", "Melon")
vegetables = ("Tomate", "Jitomate", "Cilantro", "Zanahoria", "Coliflor")
animal_products = ("Leche", "Huevo", "Jamon", "Queso", "Carne")

food_stuff_tp = fruits + vegetables + animal_products
print(f"{food_stuff_tp}\n")

# 2.3. Cambiar la tupla food_stuff_tp a una lista food_stuff_lt

food_stuff_lt = list(food_stuff_tp)
print(f"{food_stuff_lt}\n")

# 2.4. Extraer el elemento o elemetos del medio de la tupla food_stuff_tp

middle = int((len(food_stuff_tp) / 2))
print(f"{food_stuff_tp[middle]}\n")

# 2.5. Separar los primeros tres artículos y los tres artículos de la lista food_staff_lt

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(f"{first_three}, {last_three}\n")

# 2.6. Eliminar la tupla food_staff_tp por completo

del food_stuff_tp

# 2.7. Comprobar si un elemento existe en una tupla:

nordic_countries = ("Dinamarca", "Finlandia", "Islandia", "Noruega", "Suecia")

# -> Comprobar si "Estonia" es una país nórdico

mask = "Estonia" in nordic_countries
print(f"Estonia es una país nórdico: {mask}\n")

# -> Comprobar si "Islandia" es una país nórdico

mask = "Islandia" in nordic_countries
print(f"Islandia es una país nórdico: {mask}\n")
