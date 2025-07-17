# while loop

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

print("Fin del loop de numeros del 1 al 10")

print("---"*10)

# while loop con True

count = 1

while True:
    print(f"Hola {count}")
    if count == 5:
        break
    count += 1

print("Fin del loop de True")

print("---"*10)

# while loop con continue

count = 1

while count <= 10:
    if count == 5:
        count += 1
        continue
    print(f"Hola {count}")
    count += 1

print("Fin del loop de continue")

print("---"*10)

# while loop con else

count = 1

while count <= 5:
    print(f"Hola {count}")
    count += 1
else:
    print("Fin del loop de else")


# while loop con break y else

count = 1

while count <= 10:
    print(f"Hola {count}")
    if count == 5:
        break
    count += 1
else:
    print("Fin del loop de else")

print("---"*10)

# try except and while loop pidiendo numero positivo al usuario

number = 0

while number <= 0:
    try:
        number = int(input("Introduce un numero positivo: "))
        if number <= 0:
            print("El numero debe ser positivo")
        else:
            print(f"El numero es {number}")
    except ValueError:
        print("El numero debe ser un numero entero")

print("Fin del loop")