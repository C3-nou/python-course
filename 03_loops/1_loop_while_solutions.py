def exercise1():
    i = 10
    while i >= 1:
        print(i)
        i -= 1

def exercise2():
    i = 1
    sum = 0
    while i <= 20:
        if i % 2 == 0:
            sum += i
        i += 1
    return sum

def exercise3():
    number = int(input("Introduce un número entero positivo: "))
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
    return factorial

def exercise4():
    password = input("Introduce una contraseña: ")
    while len(password) < 8:
        password = input("La contraseña debe tener al menos 8 caracteres. Introduce una contraseña: ")
    return "Contraseña válida"

def exercise5():
    number = int(input("Introduce un número: "))
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

def exercise6():
    number = int(input("Introduce un número: "))
    i = 2
    while i <= number:
        if number % i == 0:
            print(f"{number} no es primo")
            break
        i += 1
    else:
        print(f"{number} es primo")