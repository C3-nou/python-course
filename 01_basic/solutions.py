from typing import Any

def exercise_1():
    name = input("Ingrese su nombre: \n")
    age = int(input("Ingrese su edad: \n"))
    city = input("Ingrese su ciudad: \n")
    print(f"Hola, {name}!, encantado de conocerte")
    print(f"Tu edad es {age} y vives en {city} \n")
    return

def exercise_2(*args: Any):
    for arg in args:
        print(f"El tipo de {arg} es {type(arg)}")
    return

def exercise_3(a: str, b: float):
    print(f"El valor {a} convertido a entero es {int(a)}")
    print(f"El valor {a} converido a float es {float(a)}")
    print(f"El valor {b} convertido a entero es {int(b)}")
    return

def exercise_4():
    name = input("Ingrese su nombre: \n")
    age = input("Ingrese su edad: \n")
    height = input("Ingrese su altura: \n")
    print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros")
    return

def exercise_5():
    PI = 3.141592653589793
    print(f"El número PI es {PI}")
    print(f"El número PI redondeado es {round(PI)}")
    print(f"La división entera entre el número PI y 2 es {PI // 2}")
    return