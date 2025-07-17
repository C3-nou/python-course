# Fechas y horas en Python

"""
    Las fechas y horas en Python se manejan con el módulo datetime.
    El módulo datetime proporciona clases para manipular fechas y horas.
"""

import datetime

# Fecha actual
print(datetime.date.today())

# Fecha actual con hora
print(datetime.datetime.now())

# Fecha actual con hora y zona horaria
print(datetime.datetime.now(datetime.timezone.utc))

# crear una fecha
fecha = datetime.date(2025, 1, 1)
print(fecha)

# crear una fecha y hora
fecha_hora = datetime.datetime(2025, 1, 1, 12, 0, 0)
print(fecha_hora)

# crear una fecha y hora con zona horaria
fecha_hora_utc = datetime.datetime(2025, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
print(fecha_hora_utc)

# formatear una fecha
print(fecha.strftime("%d/%m/%Y"))

# formatear una fecha y hora
print(fecha_hora.strftime("%d/%m/%Y %H:%M:%S"))

# formatear una fecha y hora con zona horaria
print(fecha_hora_utc.strftime("%d/%m/%Y %H:%M:%S %Z"))

# operaciones con fechas

# sumar 1 dia a la fecha
fecha_mas_1_dia = fecha + datetime.timedelta(days=1)
print("fecha_mas_1_dia: ", fecha_mas_1_dia)

# restar 1 dia a la fecha
fecha_menos_1_dia = fecha - datetime.timedelta(days=1)
print("fecha_menos_1_dia: ", fecha_menos_1_dia)

# sumar 1 hora a la fecha y hora
fecha_hora_mas_1_hora = fecha_hora + datetime.timedelta(hours=1)
print("fecha_hora_mas_1_hora: ", fecha_hora_mas_1_hora)

# restar 1 hora a la fecha y hora
fecha_hora_menos_1_hora = fecha_hora - datetime.timedelta(hours=1)
print("fecha_hora_menos_1_hora: ", fecha_hora_menos_1_hora)

# usar locale para formatear la fecha
import locale

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
print(fecha.strftime("%A %d de %B de %Y"))

# usar locale para formatear la fecha y hora
print(fecha_hora.strftime("%A %d de %B de %Y %H:%M:%S"))