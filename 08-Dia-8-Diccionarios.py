# Ejercicios Dia 8

# 1. Crear un diccionario vacío llamado dog

dog = dict()

# 2. Añadir nombre, color, raza, patas, edad al diccionario dog

dog["name"] = "Halx"
dog["color"] = "Black"
dog["breed"] = "Fresch Pool"
dog["age"] = 5

print(f"\n{dog}\n")

# 3. Crear un diccionario de estudiantes y agregar nombre, apellido, edad, estado civil, habilidades,
#    país, ciudad y dirección como claves para el diccionario

student = {
    "name": "Alejandro",
    "last_name": "Hernández",
    "age": 30,
    "marital_status": "Single",
    "skills": ["Python", "Power BI", "SQL", "Excel"],
    "country": "Mexico",
    "addres": "NA"
}

print(f"{student}\n")

# 4. Obtener la longitud del diccionario del estudiante

print(f"{len(student)}\n")

# 5. Obtener el valor de la habilidades y verificar el tipo de datos, debe ser una lista

skills_value = student.get("skills")

print(f"{skills_value}")
print(f"Tip de dato: {type(skills_value)}\n")

# 6. Modificar los valores de las habilidades agregando una o dos habilidades

student["skills"].extend(["Tableau", "Big Query"])

print(f"{student}\n")

# 7. Obtener las claves de diccionario como una lista

print(f"{list(student.keys())}\n")

# 8. Obtener los valores del diccionario como una lista

print(f"{list(student.values())}\n")

# 9. Cambiar el diccionario a una lista de tuplas usando el método items()

print(f"{tuple(student.items())}\n")

# 10. Eliminar uno de los elementos del diccionario

del student["skills"]

print(f"{student}\n")

# 11. Eliminar uno de los diccionario

del student
