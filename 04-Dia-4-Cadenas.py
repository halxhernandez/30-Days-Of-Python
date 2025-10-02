# Ejercicios Dia 4

# 4.1. Concatenar las cadenas 'Thirty', 'Days', 'Of', 'Python' en una sola cadena: 'Thirty Days Of Python'

word1, word2, word3, word4 = "Thirty", "Days", "Of", "Python"
print("")
print(word1, word2, word3, word4, "\n")

# 4.2. Concatenar las cadenas 'Codificación', 'Para', 'Todos' en una sola cadena: 'Codificación Para Todos'

word5, word6, word7 = "Codificación", "Para", "Todos"
print(word5, word6, word7, "\n")

# 4.3. Declarar una variable llamada empresa y asignarle el valor inicial "Codificación Para Todos"

company = "Codificación Para Todos"

# 4.4. Imprimir la variable empresa utilizando print()

print(company, "\n")

# 4.5. Imprimir la longitud de la cadena almacenada en la variable empresa utilizando el método len() y print()

print(len(company), "\n")

# 4.6. Convertir todos los caracteres de la cadena a letras mayúsculas utilizando el método upper()

upper_company = company.upper()

# 4.7. Convertir todos los caracteres de la cadena a letras minúsculas utilizando el método lower()

lower_company = company.lower()

# 4.8. Aplicar los métodos capitalize(), title() y swapcase() para formatear el valor de la cadena "Codificación Para Todos"

capitalize_company = company.capitalize()
title_company = company.title()
swapcase_company = company.swapcase()

print(upper_company)
print(lower_company)
print(capitalize_company)
print(title_company)
print(swapcase_company, "\n")

# 4.9. Cortar la primera palabra de la cadena "Codificación Para Todos"

print(company.split(" ")[0], "\n")

# 4.10. Comprobar si la cadena "Codificación Para Todos" contiene la palabra "Codificación" utilizando índice, búsqueda u otros métodos

print("Codificación" in company)
print(company.split(" ")[0] == "Codificación")
print(company[:12] == "Codificación", "\n")

# 4.11. Reemplazar la palabra "Codificación" en la cadena "Codificación Para Todos" por "Python"

company = "Python" + company[12:]
print(company, "\n")

# 4.12. Cambiar "Python para todos" a "Python para TODOS" utilizando el método de reemplazo u otros métodos

company = company.replace("Todos", "TODOS")
print(company, "\n")

# 4.13. Dividir la cadena "Python Para TODOS" usando el espacio como separador con split()

split_company = company.split(" ")
print(split_company, "\n")

# 4.14. Dividir la cadena "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" utilizando la coma como separador

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(",")

print(split_companies, "\n")

# 4.15. Identificar el carácter en el índice 0 en la cadena "Python Para TODOS"

print(company[0], "\n")

# 4.16. Identificar el último índice de la cadena "Python Para TODOS"

print(company[-1], "\n")

# 4.17. Determinar qué carácter está en el índice 10 en la cadena "Python Para TODOS"

print(company[9], "\n")

# 4.18. Crear un acrónimo o abreviatura para el nombre "Python Para TODOS".

acronym = split_company[0][0].upper() + split_company[1][0].upper() + split_company[2][0].upper()
print(acronym, "\n")

# 4.19. Crear un acrónimo o abreviatura para el nombre "Python Para Algunos"

text = "Python Para Algunos"
acronym = text.split(" ")[0][0].upper() + text.split(" ")[1][0].upper() + text.split(" ")[2][0].upper()

print(acronym, "\n")

# 4.20. Utilizar el método index para determinar la posición de la primera aparición de "T" en "Python Para TODOS"

print(company.index("T"), "\n")

# 4.21. Utilizar el método index para determinar la posición de la primera aparición de "a" en "Python Para TODOS"

print(company.index("a"), "\n")

# 4.22. Utilizar rfind para determinar la posición de la última aparición de "l" en "Coding For All People"

text = "Coding For All People"
print(text.rfind("l"), "\n")

# 4.23. Utilizar index o find para encontrar la posición de la primera aparición de la palabra "because" en la oración:
#      "No puedes terminar una oración con 'because' porque 'because' es una conjunción"

text2 = "No puedes terminar una oración con because porque because es una conjunción"
print(text2.find("because"), "\n")

# 4.24. Utilizar rindex para encontrar la posición de la última aparición de la palabra "because" en la oración:
#       "No puedes terminar una oración con because porque because es una conjunción"

print(text2.rindex("because"), "\n")

# 4.25. Eliminar la frase "porque, porque, porque" en la oración:
#       "No puedes terminar una oración con porque, porque, porque es una conjunción"

text3 = "No puedes terminar una oración con porque, porque, porque es una conjunción"
print(text3.replace("porque, porque, porque", ""), "\n")

# 4.26. Encontrar la posición de la primera aparición de la palabra "porque" en la oración:
#       "No puedes terminar una oración con porque porque porque es una conjunción"

print(text3.find("porque"), "\n")

# 4.27. Verificar si la cadena "Coding For All" comienza con la subcadena "Coding"

text4 = "Coding For All"
print(text4.startswith("Coding"), "\n")

# 4.28. Verificar si la cadena "Coding For All" termina con la subcadena "coding"

print(text4.endswith("Coding"), "\n")

# 4.29. Eliminar los espacios finales izquierdo y derecho de la cadena " Coding For All "

text5 = " Coding For All "
print(text5.strip(), "\n")

# 4.30. Evaluar cuál de las siguientes variables devuelve True con el método isidentifier():
#       "30 Days de Python" y  "Thirty_Days_de_python"

word8, word9 = "30 Days de Python", "Thirty_Days_de_python"

print(word8.isidentifier())
print(word9.isidentifier(), "\n")

# 4.31. Unir la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] con el carácter hash (#) y espacios como separadores

list_frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "#" + list_frameworks[0] + "_" + list_frameworks[1] + "_" + list_frameworks[2] + "_" + list_frameworks[3] + "_" + list_frameworks[4]
print(result, "\n")
