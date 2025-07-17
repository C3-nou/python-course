# Bucle for
# Permite iterar sobre una secuencia de elementos

# Ejemplo 1: Iterar sobre una lista

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

print("---"*10)

# Ejemplo 2: Iterar sobre un string

cadena = "Hola"

for letra in cadena:
    print(letra)

print("---"*10)

# recuperar el indice de cada elemento

frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"El indice de la fruta {fruta} es {indice}")

print("---"*10)


# bucles anidados

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

print("---"*10)

# bucles con break

animales = ["perro", "gato", "pez", "pajaro"]

for animal in animales:
    print(animal)
    if animal == "pez":
        break

print("---"*10)

# bucles con continue

for idx, animal in enumerate(animales):
    if animal == "pez":
        continue
    print(f"El animal {animal} esta en el indice {idx}")

print("---"*10)

# comprension de listas

animales_mayusculas = [animal.upper() for animal in animales]

print(animales_mayusculas)

print("---"*10)

# comprension de listas con condicion

animales_mayusculas_condicion = [animal.upper() for animal in animales if animal == "perro"]
print(animales_mayusculas_condicion)

print("---"*10)

# comprension de listas con condicion y else

animales_mayusculas_condicion_else = [animal.upper() if animal == "perro" else animal for animal in animales]

print(animales_mayusculas_condicion_else)

print("---"*10)