# Ejercicios Nivel 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("")

# 1. Utilizar un bucle for para imprimir cada país en la lista de paises

for country in countries:
    print(country)

print("")

# 2. Utilizar un bucle for para imprimir cada nombre en la lista de nombres

for name in names:
    print(name)

print("")

# 3. Utilizar un bucle for para imprimir cada número en la lista de números

for num in numbers:
    print(num)

print("")

# Ejercicios Nivel 2

# 4. Utilizar map para crear una nueva lista cambiando cada país a mayúsculas en la lista de países

change_to_upper = lambda x: x.upper()
countries_upper = map(change_to_upper, countries)

print(f"{list(countries_upper)}\n")

# 5. Utilizar map para crear una nueva lista cambiando cada número por su cuadrado en la lista de números

def square(num):
    return num ** 2

squares = map(square, numbers)

print(f"{list(squares)}\n")

# 6. Utilizar map para cambiar cada nombre a mayúscula en la lista de nombres

def change_name_upper(name):
    return name.upper()

names_upper = map(change_name_upper, names)

print(f"{list(names_upper)}\n")

# 7. Utilizar filter para filtrar los países que contienen la palabra "land"

filter_land = lambda x: "land" in x
land = filter(filter_land, countries)

print(f"{list(land)}\n")

# 8. Utilizar filter para filtrar países que tengan exactamente seis caracteres

is_country_long = lambda country: len(country) == 6
long_countries = filter(is_country_long, countries)

print(f"{list(long_countries)}\n")

# 9. Utilizar filter para filtrar los países que contengan seis letras o más en la lista de países.

def country_long(country):
    if len(country) > 6:
        return True
    return False

len_countries = filter(country_long, countries)

print(f"{list(len_countries)}\n")

# 10. Utilizar filter para filtrar los países que comienzan con 'E'

countrie_begin_e = lambda country: country.startswith("E")
countries_begin_e = filter(countrie_begin_e, countries)

print(f"{list(countries_begin_e)}\n")

# 11. Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))

from functools import reduce

result = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 5,
           map(lambda x: x * 2, numbers))
)
print(f"{result}\n")

# 12. Declarar una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print(f"{get_string_lists([1, "abc", None, "xyz", 45])}\n")

# 13. Utilizar reduce para sumar todos los números en la lista de números

suma_total = reduce(lambda a, b: a + b, numbers)

print(f"{suma_total}\n")

# 14. Utilizar reduce para concatenar todos los países y producir esta oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

phrase = reduce(
    lambda a, b: f"{a}, {b}" if b != countries[-1] else f"{a}, and {b}",
    countries
) + " are north European countries"

print(f"{phrase}\n")
