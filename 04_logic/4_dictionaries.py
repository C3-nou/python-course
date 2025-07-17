"""
    Diccionarios
"""

from typing import Callable
from os import system
if system("clear") != 0: system("cls")

# ========================================
# CHEAT SHEET - DICCIONARIOS EN PYTHON
# ========================================

# ========================================
# 1. CREACIÓN DE DICCIONARIOS
# ========================================

# Forma básica
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Con dict()
persona2 = dict(nombre="Ana", edad=30, ciudad="Barcelona")

# Diccionario vacío
diccionario_vacio = {}
diccionario_vacio2: dict[str, int] = dict()

print("1. Creación:", persona)

# ========================================
# 2. ACCESO A ELEMENTOS
# ========================================

# Acceso directo (puede dar error si no existe)
nombre = persona["nombre"]

# Acceso seguro con get() (no da error si no existe)
edad = persona.get("edad")
altura = persona.get("altura", "No especificada")  # valor por defecto

print("2. Acceso:", nombre, edad, altura)

# ========================================
# 3. MODIFICACIÓN Y AGREGADO
# ========================================

# Modificar valor existente
persona["edad"] = 26

# Agregar nueva clave-valor
persona["profesion"] = "Programador"

# Con update() para múltiples elementos
persona.update({
    "telefono": "123456789",
    "email": "juan@email.com"
})

print("3. Modificación:", persona)

# ========================================
# 4. ELIMINACIÓN DE ELEMENTOS
# ========================================

# Con del (da error si no existe)
del persona["telefono"]

# Con pop() (retorna el valor eliminado)
email = persona.pop("email", "No encontrado")

# Con popitem() (elimina y retorna el último elemento)
ultimo = persona.popitem()

# Limpiar todo el diccionario
# persona.clear()

print("4. Eliminación:", persona, "Email eliminado:", email)

# ========================================
# 5. MÉTODOS PRINCIPALES
# ========================================

# keys() - obtener todas las claves
claves = persona.keys()
print("5a. Claves:", list(claves))

# values() - obtener todos los valores
valores = persona.values()
print("5b. Valores:", list(valores))

# items() - obtener pares clave-valor
items = persona.items()
print("5c. Items:", list(items))

# copy() - copia superficial
persona_copia = persona.copy()

# ========================================
# 6. ITERACIÓN EN DICCIONARIOS
# ========================================

print("6. Iteración:")

# Iterar por claves
for clave in persona:
    print(f"Clave: {clave}")

# Iterar por claves explícitamente
for clave in persona.keys():
    print(f"Clave explícita: {clave}")

# Iterar por valores
for valor in persona.values():
    print(f"Valor: {valor}")

# Iterar por clave y valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ========================================
# 7. COMPROBACIONES
# ========================================

# Verificar si existe una clave
existe_nombre = "nombre" in persona
existe_altura = "altura" in persona

print("7. Comprobaciones:", existe_nombre, existe_altura)

# ========================================
# 8. DICCIONARIOS ANIDADOS
# ========================================

estudiante = {
    "nombre": "María",
    "notas": {
        "matematicas": 9.5,
        "historia": 8.0,
        "ciencias": 9.0
    },
    "direccion": {
        "calle": "Calle Mayor 123",
        "ciudad": "Valencia"
    }
}

# Acceso a elementos anidados
nota_mate = estudiante["notas"]["matematicas"] # type: ignore
print("8. Anidado:", nota_mate)

# ========================================
# 9. COMPRENSIÓN DE DICCIONARIOS
# ========================================

# Crear diccionario con comprensión
numeros = [1, 2, 3, 4, 5]
cuadrados = {num: num**2 for num in numeros}

# Con condición
pares_cuadrados = {num: num**2 for num in numeros if num % 2 == 0}

print("9. Comprensión:", cuadrados, pares_cuadrados)

# ========================================
# 10. MÉTODOS AVANZADOS
# ========================================

# setdefault() - obtener valor o establecer si no existe
persona.setdefault("pais", "España")

# fromkeys() - crear diccionario con claves y valor por defecto
vocales = dict.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)

# merge de diccionarios (Python 3.9+)
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
dic_mergeado = dic1 | dic2  # o dict1.update(dict2)

print("10. Avanzados:", persona, vocales, dic_mergeado)

# ========================================
# 11. CASOS DE USO COMUNES
# ========================================

# Contador de elementos
texto = "hola mundo"
contador: dict[str, int] = {}
for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1

# Agrupación de datos
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona"},
    {"nombre": "Carlos", "edad": 25, "ciudad": "Madrid"}
]

# Agrupar por ciudad
por_ciudad = {}
for persona in personas:
    ciudad = persona["ciudad"]
    if ciudad not in por_ciudad:
        por_ciudad[ciudad] = []
    por_ciudad[ciudad].append(persona["nombre"]) # type: ignore

print("11. Casos de uso:", contador, por_ciudad) # type: ignore

# ========================================
# 12. TRUCOS Y CONSEJOS
# ========================================

# Diccionario como switch/case
def operacion_matematica(operacion: str, a: int, b: int) -> int | str:
    operaciones: dict[str, Callable[[int, int], int | str]] = {
        "suma": lambda x, y: x + y, # type: ignore
        "resta": lambda x, y: x - y, # type: ignore
        "multiplicacion": lambda x, y: x * y, # type: ignore
        "division": lambda x, y: x / y if y != 0 else "Error" # type: ignore
    }
    return operaciones.get(operacion, lambda x, y: "Operación no válida")(a, b) # type: ignore

# Configuración por defecto
config_default = {
    "puerto": 8080,
    "host": "localhost",
    "debug": False
}

config_usuario = {"puerto": 9000}
config_final = {**config_default, **config_usuario}  # merge con prioridad

print("12. Trucos:", operacion_matematica("suma", 5, 3), config_final)