# Ejercicos Nivel 1

# 1.1. Iterar del 0 al 10 usando el blucle for, hacer lo mismo usando el bucle while

print("")

for i in range(10):
    print(i)

count = 0
while count < 10:
    count += 1
    print(count)

print("")

# 1.2. Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:

#
##
###
####
#####
######
#######

for i in range(1, 8):
    print("#" * i)

# 1.3. Utilizar bucles anidados para crear lo siguiente:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

print("")

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

print("")

# 1.4. Imprimir el siguiente patrón:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    print(f"{i} * {i} = {i * i}")

print("")

# 1.5. Iterar a través de la lista, ["Python", "Numpy", "Pandas", "Django", "Flask"] usando un bucle for e imprima los elementos.

ls = ["Python", "Numpy", "Pandas", "Django", "Flask"]

for i in ls:
    print(i)

print("")

# 1.6. Utilizar el bucle for para iterar de 0 a 100 e imprimir solo números pares

for i in range(101):
    if i % 2 == 0:
        print(i)

print("")

# 1.7. Utilizar el bucle for para iterar de 0 a 100 e imprimir solo números impares

for i in range(101):
    if i % 2 != 0:
        print(i)

print("")

# Ejercicios Nivel 2

# 2.1. Utilizar el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números

add = 0
for i in range(101):
    add += i

print(f"La suma de todos los números es {add}\n")

# 2.2. Utilizar el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares

add_even = 0
add_odd = 0

for i in range(101):
    if i % 2 == 0:
        add_even += i
    else:
        add_odd += i

print(f"La suma de todos los números pares es {add_even}. Y la suma de todos los números impares es {add_odd}\n")

# Ejercicios Nivel 3

# 3.1. De la siguiente lista recorrer los países y extraer todos los que contengan la palabra "land"

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
    'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon',
    'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile',
    'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
    'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
    'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland',
    'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
    'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
    'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi',
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar',
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman',
    'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
    'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
    'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
    'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
    'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
    'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam',
    'Yemen', 'Zambia', 'Zimbabwe'
]

for country in countries:
    if "land" in country:
        print(country)

print("")

# 3.2. Esta es una lista de frutas, ['banana', 'naranja', 'mango', 'limón'] invertir el orden usando un bucle

fruits = ['banana', 'naranja', 'mango', 'limón']
fruit = []

for i in range(len(fruits) - 1, -1, -1):
    fruit.append(fruits[i])

print(f"{fruit}\n")
