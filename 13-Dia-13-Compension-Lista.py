# Ejercicios Dia 14

# 1. Filtrar solo los negativos y ceros en la lista

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negs_and_zeros = [num for num in numbers if num <= 0]

print(f"\n{negs_and_zeros}\n")

# 2. Aplanar la siguiente lista de lista de listas en una lista unidimensional

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist in list_of_lists for inner_list in sublist for number in inner_list]

print(f"{flattened_list}\n")

# 3. Usando la comprensión de listas, cree la siguiente lista de tuplas:

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(f"{result}\n")

# 5. Aplanar la siguiente lista para formar una nueva lista:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for country_tuple_list in countries
    for country, capital in country_tuple_list
]

print(f"{flattened_countries}\n")

# 6. Cambiar la siguiente lista a una lista de diccionarios:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dict_list = [
    {'country': country.upper(), 'city': city.upper()}
    for country_tuple_list in countries
    for country, city in country_tuple_list
]

print(f"{countries_dict_list}\n")

# 7. Cambiar la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [
    f"{first} {last}"  # Concatenar nombre y apellido
    for name_tuple_list in names
    for first, last in name_tuple_list
]

print(f"{full_names}\n")

# 8. Escribir una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales

line_params = lambda x1, y1, x2, y2: ((y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1)

m, b = line_params(1, 2, 3, 6)
print("Pendiente:", m)
print("Intersección Y:", b)
print("")
