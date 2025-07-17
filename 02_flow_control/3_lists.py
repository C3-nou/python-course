# Listas

lista = [1, 2, 3, 4, 5]
print(lista)

print("---"*10)

# Acceder a los elementos de la lista

print(lista[0])
print(lista[1])

# lista de strings

lista_de_strings = ["Hola", "Mundo", "Python"]
print(lista_de_strings)

print("---"*10)

# lista de tipos mixtos

lista_de_numeros = [1, 2, 3, 4, 5]
lista_de_strings = ["Hola", "Mundo", "Python"]
lista_de_booleanos = [True, False, True]
lista_de_mixta = [1, "Hola", True]

print(lista_de_mixta)

print("---"*10)

# lista de tipos mixtos

lista_de_mixta = [1, "Hola", True, 3.14, [1, 2, 3]]

print(lista_de_mixta)

print("---"*10)

# lista de listas

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_de_listas)

print("---"*10)

# lista de diccionarios

lista_de_diccionarios = [{"nombre": "Juan", "edad": 20}, {"nombre": "Maria", "edad": 25}]

print(lista_de_diccionarios)

# uso de indices negativos

print(lista_de_listas[-1])

print("---"*10)

# slicing

print(lista_de_listas[0:2])

print("---"*10)

# slicing con pasos

print(lista_de_listas[0:2:2])

print("---"*10)

print(lista_de_listas[:2])

print("---"*10)

# tercer parametro sirve para invertir la lista o saltar elementos

lista_con_saltos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_con_saltos[::2])

lista_para_invertir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_para_invertir[::-1])

print("---"*10)

# agregar elementos a la lista

lista_para_agregar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_agregar.append(11)

print(lista_para_agregar)

lista_agregada = lista_para_agregar + [12, 13, 14, 15]

print(lista_agregada)

print("---"*10)

# obtener la longitud de la lista

print(len(lista_para_agregar))

print("---"*10)

# eliminar elementos de la lista

lista_para_eliminar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_eliminar.remove(1)

print(lista_para_eliminar)

print("---"*10)