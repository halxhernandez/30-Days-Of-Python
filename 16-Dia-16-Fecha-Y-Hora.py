# Ejercicios Dia 16

# 1. Obtener el día, mes, año, hora, minuto y marca de tiempo actuales del módulo datetime

from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"\nDía: {day}")
print(f"Mes: {month}")
print(f"Año: {year}")
print(f"Hora: {hour}")
print(f"Minuto: {minute}")
print(f"Marca de timepo: {timestamp}\n")

# 2. Formatear la fecha actual utilizando este formato: "%m/%d/%Y, %H:%M:%S"

formatted_date = datetime.strftime(now, "%m/%d/%Y, %H:%M:%S")

print(f"Fecha formateada: {formatted_date}\n")

# 3. Hoy es 14 de Octubre del 2025. Cambiar esta cadena de tiempo a hora

date_string = "14 October, 2025"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print(f"Cadena de texto cambiada: {date_object}\n")

# 4. Calcular la diferencia horaria entre ahora y el año nuevo

new_year = datetime(2026, 1, 1)
date_difference = new_year - now

print(f"Diferencia horaria: {date_difference}\n")

# 5. Calcular la diferencia horaria entre el 1 de enero de 1970 y la actualidad

last_date = datetime(1970, 1, 1)
date_difference = now - last_date

print(f"Diferencia horaria: {date_difference}\n")
