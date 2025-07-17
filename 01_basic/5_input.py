### input()

nombre = input("Ingrese su nombre: \n")
print(f"Hola, {nombre}!, encantado de conocerte")

age = int(input("Ingrese su edad: \n"))
print(f"Tu edad es {age}")

# type conversion
age = input("Ingrese su edad: \n")
print(f"Tu edad es {age}")

print("Dentro de 20 años, tu edad será", int(age) + 20)

country, city = input("Ingrese su país y ciudad: \n").split()
print(f"Tu país es {country} y tu ciudad es {city}")

# type conversion
country, city = input("Ingrese su país y ciudad vives ? \n").split()
print(f"Tu país es {country} y tu ciudad es {city}")
