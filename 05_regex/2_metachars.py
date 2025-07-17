# 02 - Metachars

"""
    Los metachars son caracteres que tienen un significado especial en las expresiones regulares.
    Los metachars son:
    . -> cualquier caracter
    ^ -> inicio de la cadena
    $ -> fin de la cadena
    * -> cero o más ocurrencias
    + -> una o más ocurrencias
    ? -> cero o una ocurrencia
"""

import re

text = "Hola mundo, H0la mundo, H$la mundo"
pattern = "H.la mundo"

result = re.findall(pattern, text)
print(result)

# r expresion regular

pattern = r"\."
text_casa = "Mi casa es blanca. Y el coche es negro."
result = re.findall(pattern, text_casa)
print(result)

# \d -> cualquier dígito

text_edad = "Mi edad es 25 años"
pattern = r"\d"
result = re.findall(pattern, text_edad)
print(result)

# encontrar una cantidad de dígitos

text_edad = "Mi edad es 25 años"
pattern = r"\d{2}"
result = re.findall(pattern, text_edad)
print(result)

# \w -> cualquier letra, número o guión bajo

text_nombre = "Mi nombre es Juan"
pattern = r"\w"
result = re.findall(pattern, text_nombre)
print(result)

# \s -> cualquier espacio en blanco

text_nombre = "Mi nombre es Juan"
pattern = r"\s"
result = re.findall(pattern, text_nombre)
print(result)

# ^ -> inicio de la cadena

text_nombre = "Mi nombre es Juan"
pattern = r"^Mi"
result = re.findall(pattern, text_nombre)
print(result)

# $ -> fin de la cadena

text_nombre = "Mi nombre es Juan"
pattern = r"Juan$"
result = re.findall(pattern, text_nombre)
print(result)

# \b -> borde de palabra

text_nombre = "Mi nombre es Juan"
pattern = r"\bMi\b"
result = re.findall(pattern, text_nombre)
print(result)