# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
def exercise1(lista: list[int]) -> list[int]:
    lista.append(6)
    lista.insert(2, 10)
    lista[0] = 0
    return lista

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
def exercise2(lista_a: list[int], lista_b: list[int]) -> list[int]:
    lista_a.extend(lista_b)
    lista_a.remove(1)
    lista_a.pop(3)
    lista_b.clear()
    return lista_a

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
def exercise3(lista: list[int]) -> list[int]:
    del lista[2:5]
    return lista

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
def exercise4(lista: list[int]) -> tuple[list[int], int, bool]:
    lista.sort()
    count = lista.count(2)
    return lista, count, 7 in lista

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
def exercise5(lista: list[int]) -> tuple[list[int], list[int]]:
    original = lista
    referencia = lista
    referencia[0] = 10
    return original, referencia

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
def exercise6(lista: list[str]) -> list[str]:
    return sorted(lista, key=lambda x: x.lower())