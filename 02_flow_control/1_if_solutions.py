def exercise1():
    number1 = int(input("Introduce el primer número: "))
    number2 = int(input("Introduce el segundo número: "))

    if number1 > number2:
        print(f"El número {number1} es mayor que el número {number2}")
    elif number1 < number2:
        print(f"El número {number1} es menor que el número {number2}")
    else:
        print(f"Los números {number1} y {number2} son iguales")

def exercise2():
    number1 = int(input("Introduce el primer número: "))
    number2 = int(input("Introduce el segundo número: "))
    operation = input("Introduce la operación (+, -, *, /): ")

    if operation == "+":
        print(f"El resultado de la suma es {number1 + number2}")
    elif operation == "-":
        print(f"El resultado de la resta es {number1 - number2}")
    elif operation == "*":
        print(f"El resultado de la multiplicación es {number1 * number2}")
    elif operation == "/":
        if number2 == 0:
            print("Error: División por cero")
        else:
            print(f"El resultado de la división es {number1 / number2}")
    else:
        print("Operación no válida")

def exercise3():
    year = int(input("Introduce un año: "))

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print(f"El año {year} no es bisiesto")
        else:
            print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")

def exercise4():
    age = int(input("Introduce tu edad: "))

    if age >= 0 and age <= 2:
        print("Eres un bebé")
    elif age >= 3 and age <= 12:
        print("Eres un niño")
    elif age >= 13 and age <= 17:
        print("Eres un adolescente")
    elif age >= 18 and age <= 64:
        print("Eres un adulto")
    else:
        print("Eres un adulto mayor")