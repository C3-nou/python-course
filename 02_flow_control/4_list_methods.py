# metodos de listas

lista_para_agregar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_agregar.append(11)

print(lista_para_agregar)

print("---"*10)

# eliminar elementos de la lista

lista_para_eliminar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_eliminar.remove(1)

print(lista_para_eliminar)

print("---"*10)

# insertar elementos en la lista

lista_para_insertar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_insertar.insert(0, 0)

print(lista_para_insertar)

print("---"*10)

# eliminar el ultimo elemento de la lista

lista_para_eliminar_ultimo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_eliminar_ultimo.pop()

print(lista_para_eliminar_ultimo)

print("---"*10)

# contar elementos en la lista

lista_para_contar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_para_contar.count(1))

print("---"*10)

# ordenar la lista

lista_para_ordenar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_ordenar.sort()

print(lista_para_ordenar)

print("---"*10)

# invertir la lista

lista_para_invertir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_invertir.reverse()

print(lista_para_invertir)

print("---"*10)

# extender la lista

lista_para_extender = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_extender.extend([11, 12, 13, 14, 15])

print(lista_para_extender)

print("---"*10)

# clear la lista

lista_para_clear = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_para_clear.clear()

print(lista_para_clear)

print("---"*10)

# eliminar en un rango

lista_para_eliminar_rango = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del lista_para_eliminar_rango[0:2]

print(lista_para_eliminar_rango)

print("---"*10)

# buscar un elemento con in

lista_para_buscar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(1 in lista_para_buscar)

print("---"*10)

# buscar un elemento con in
