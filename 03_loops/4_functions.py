# funciones

"""
    Definicion de una funcion

    def nombre_funcion(parametro1, parametro2, ...):
        # codigo
        return valor

    nombre_funcion(parametros)

"""

def saludar(nombre: str):
    print(f"Hola {nombre}")

saludar("Juan") # llamando a la funcion

print("---"*10)

# funcion con multiples parametros

def saludar_dos(nombre: str, apellido: str):
    print(f"Hola {nombre} {apellido}")

saludar_dos("Juan", "Perez")

print("---"*10)

# Documentar funciones con docstring

def restar(numero1: int, numero2: int):
    """
    Esta funcion resta dos numeros
    """
    return numero1 - numero2

print(restar(10, 5))
print(restar.__doc__)

print("---"*10)

# funcion con parametros por defecto

def multiplicar(numero1: int, numero2: int = 2):
    """
    Esta funcion multiplica dos numeros
    """
    return numero1 * numero2

print(multiplicar(10))
print(multiplicar(10, 5))
print(multiplicar.__doc__)

print("---"*10)

# funcion con argumentos por clave

def describir_persona(nombre: str, edad: int, ciudad: str):
    """
    Esta funcion describe una persona
    """
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

describir_persona("Juan", 30, "Madrid")
describir_persona(edad=30, nombre="Juan", ciudad="Madrid")
describir_persona(ciudad="Madrid", nombre="Juan", edad=30)

print("---"*10)

# funcion con argumentos variables

def sumar(*numeros: int):
    return sum(numeros)

print(sumar(1, 2, 3, 4, 5))

print("---"*10)

# funcion con argumentos variables y argumentos por clave

def describir_persona_dos(nombre: str, edad: int, ciudad: str, **kwargs: str):
    """
    Esta funcion describe una persona
    """
    print(f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describir_persona_dos("Juan", 30, "Madrid", color="rojo", profesion="programador")

print("---"*10)