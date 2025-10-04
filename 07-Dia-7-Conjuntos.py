# Ejercicios Nivel 1

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
A = {19, 22, 24, 20, 25}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.1. Encontrar la longitud del conjunto it_companies

print(f"\n{len(it_companies)}\n")

# 1.2. Añadir "Twitter" a it_companies

it_companies.append("Twitter")
print(f"{it_companies}\n")

# 1.3. Insertar varias empresas de TI a la vez en el conjunto it_companies

it_companies = it_companies + ["Nvidia", "Samsumg", "Huawei"]
print(f"{it_companies}\n")

# 1.4. Eliminar una de las empresas del conjunto it_companies

it_companies.pop()
print(f"{it_companies}\n")

# 1.5. ¿Cuál es la diferencia entre eliminar y descartar?

# El eliminar quita uno o más elementos de forma permanente en el conjunto
# mientras que el descartar no, ya que la nueva salida se puede almacenar
# en una nueva variable.

# Ejercicios Nivel 2

# 2.1. Unir A y B

print(f"{A.union(B)}\n")

# 2.2. Encontrar la intersección de A y B

print(f"{A.intersection(B)}\n")

# 2.3. A es un subconjunto de B

print(f"A es un subconjunto de B: {A.issubset(B)}\n")

# 2.4. Son A y B conjuntos disjuntos

print(f"Son A y B conjuntos disjuntos: {A.isdisjoint(B)}\n")

# 2.5. Unir A con B y B con A

print(f"AUB: {A.union(B)}, BUA: {B.union(A)}\n")

# 2.6. ¿Cuál es la diferencia simétrica entre A y B?

print(f"Diferencia simétrica entre A y B: {A.symmetric_difference(B)}\n")

# 2.7. Eliminar los conjunto por completo

del A, B

# Ejercicios Nivel 3

# 3.1. Convertir las edades en un conjunto y comparar la longitud de la lista y el conjunto

age_set = set(age)

print(f"La longitud de Age (lista) y Age (Conjunto) son iguales: {len(age) == len(age_set)}")
print(f"La longitud de Age (lista) es mayor que Age (Conjunto): {len(age) > len(age_set)}")
print(f"La longitud de Age (lista) es menor que Age (Conjunto): {len(age) < len(age_set)}\n")

# 3.2. "I am a teacher and I love to inspire and teach people". ¿Cuántas palabras únicas se han
#      usado en la oración?

s = "I am a teacher and I love to inspire and teach people"

unic = set(s.lower().split())

print(f"Palabras únicas: {unic}")
print(f"Cantidad de palabras únicas: {len(unic)}\n")
