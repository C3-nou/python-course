""" 
    Las expresiones regulares son una secuencia de caracteres que forma un patrón 
    de búsqueda, principalmente utilizada para la búsqueda de patrones de cadenas
    de caracteres, validaciones de datos, extracción de información, etc.
"""

import re

pattern = "Hola"
text = "Hola mundo"
result = re.search(pattern, text)

if result:
    print("Se encontró el patrón")
else:
    print("No se encontró el patrón")

# .group() -> devuelve el texto que coincide con el patrón
# .start() -> devuelve el índice de inicio de la coincidencia
# .end() -> devuelve el índice de fin de la coincidencia
# .span() -> devuelve una tupla con el índice de inicio y fin de la coincidencia
# .string -> devuelve el texto sobre el que se realizó la búsqueda

if result:
    print(result.group()) # Hola
    print(result.start()) # 0
    print(result.end()) # 4
    print(result.span()) # (0, 4)
    print(result.string) # Hola mundo

# findall() -> devuelve una lista con todas las coincidencias
# finditer() -> devuelve un iterador con todas las coincidencias

text = "Hola mundo, hola mundo"
result = re.findall(pattern, text)
print(result)

result = re.finditer(pattern, text)
for match in result:
    print(match.group())

# re.IGNORECASE -> ignora mayúsculas y minúsculas

pattern = "hola"
text = "Hola mundo"
result = re.search(pattern, text, re.IGNORECASE)
print(result)

# .sub() -> reemplaza el texto que coincide con el patrón

pattern = "Hola"
text = "Hola mundo"
replacement = "Adios"
result = re.sub(pattern, replacement, text)
print(result)
