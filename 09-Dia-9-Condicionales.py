# Ejercicios Nivel 1

# 1.1. Obtener la información del usuario mediante input(“Ingrese su edad:”). Si el usuario tiene 18 años o más, indique:
#      Tiene edad suficiente para conducir. Si es menor de 18 años, indique que espere los años que faltan

age = int(input("\nIngrese su edad: "))

if age >= 18:
    print("Tiene edad suficiente para conducir\n")
else:
    diff = 18 - age
    print(f"Necesitas {diff} años más para poder conducir\n")

# 1.2. Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad:”)
#      para obtener la edad como entrada. Puedes usar una condición anidada para imprimir "año" si hay una diferencia de edad de 1 año,
#      "años" si la diferencia es mayor y un texto personalizado si my_age = your_age

my_age = 30
your_age = int(input("Ingresa tu edad: "))

if my_age > your_age:
    diff = my_age - your_age
    print(f"Eres {diff} menor que yo")

elif my_age < your_age:
    diff = your_age - my_age
    print(f"Eres {diff} mayor que yo")

else:
    print("Tenemos la misma edad")

# 1.3. Obtener dos números del usuario mediante la solicitud de entrada. Si a es mayor que b, devuelve a mayor que b; si a es menor que b,
#      devuelve a menor que b; de lo contrario, a es igual a b

a = int(input("\nIngrese el número 1: "))
b = int(input("Ingrese el número 2: "))

if a > b:
    print(f"{a} es mayor que {b}\n")

elif a < b:
    print(f"{a} es menor que {b}\n")

else:
    print(f"{a} y {b} son iguales\n")

# Ejercicios Nivel 2

# 2.1. Escriba un código que califique a los estudiantes según sus puntuaciones
#      80-100 -> A, 70-89 -> B, 60-69 -> C, 50-59 -> D y 0-49 -> F

score = int(input("Ingrese la puntuación: "))

if score >= 80 and score <= 100: print("La calificación es A\n")
elif score >= 70 and score < 80: print("La calificación es B\n")
elif score >= 60 and score < 70: print("La calificación es C\n")
elif score >= 50 and score < 60: print("La calificación es D\n")
else: print("La calificación es F\n")

# 2.2. Comprueba si la temporada es otoño, invierno, primavera o verano. Si el usuario introduce: septiembre, octubre o noviembre, la temporada es otoño.
#      Diciembre, enero o febrero, la temporada es invierno. Marzo, abril o mayo, la temporada es primavera. Junio, julio o agosto, la temporada es verano.

month = input("Ingrese el mes: ").lower()

if month == "septiembre" or month == "octubre" or month == "noviembre": print("La temporada es otoño\n")
elif month == "diciembre" or month == "enero" or month == "febrero": print("La temporada es invierno\n")
elif month == "marzo" or month == "abril" or month == "mayo": print("La temporada es primavera\n")
else: print("la temporada es verano\n")

# 2.3. La siguiente lista contiene algunas frutas

fruits = ["platano", "naranja", "mango", "limon"]

fruit = input("Ingrese una fruta: ")

if fruit in fruits:
    print("Esa fruta ya existe en la lista\n")
else:
    fruits.append(fruit)
    print(f"{fruits}\n")

# Ejercicio Nivel 3

# 3.1. Se tiene un diccionario de personas.

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street','zipcode': '02210'}
}

# -> Verificar si el diccionario de personas tiene la clave de habilidades; de ser así, imprimir la habilidad intermedia en la lista de habilidades.

if "skills" in person.keys():
    skills = person["skills"]
    middle_index = len(skills) // 2
    print(f"Habilidad intermedia: {skills[middle_index]}\n")

# -> Verificar si el diccionario de personas tiene la clave de habilidades; de ser así, verificar si la persona tiene la habilidad "Python" e imprimir el resultado.

if "skills" in person:
    has_python = "Python" in person["skills"]
    print(f"Tiene la habilidad 'Python': {has_python}\n")

# -> Clasificación según habilidades
if "skills" in person.keys():
    skills = set(person["skills"])

    if skills == {"JavaScript", "React"}:
        print("Es desarrollador front-end\n")
    elif {"Node", "Python", "MongoDB"}.issubset(skills):
        print("Es desarrollador back-end\n")
    elif {"React", "Node", "MongoDB"}.issubset(skills):
        print("Es desarrollador full-stack\n")
    else:
        print("Título desconocido\n")

# -> Si la persona está casada y reside en Finlandia, imprimir la información en el siguiente formato:
#    Asabeneh Yetayeh vive en Finlandia. Está casado(a).

if person.get("is_marred") and person.get("country") == "Finland":
    print(f"{person['first_name']} {person['last_name']} vive en {person['country']}. Está casado(a)\n")
