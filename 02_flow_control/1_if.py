### Sentencias condicionales

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("---"*10)
# elif

nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
else:
    print("Insuficiente")

print("---"*10)

# condiciones multiples

edad = 18
carnet_de_conducir = True

if edad >= 18 and carnet_de_conducir:
    print("Puedes conducir")
else:
    print("No puedes conducir")

print("---"*10)

# operador or

edad = 18
carnet_de_conducir = False

if edad >= 18 or carnet_de_conducir:
    print("Puedes conducir")
else:
    print("No puedes conducir")

print("---"*10)

# condicionales anidados

edad = 18
tiene_trabajo = True

if edad >= 18:
    if tiene_trabajo:
        print("Tienes trabajo")
    else:
        print("No tienes trabajo")
else:
    print("No tienes 18 años")

print("---"*10)

age = 17
message = "Puedes conducir" if age >= 18 else "No puedes conducir"
print(message)

print("---"*10)

age = 17
message = "Puedes conducir" if age >= 18 else "No puedes conducir"
print(message)

print("---"*10)