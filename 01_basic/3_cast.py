### Conversión de tipos de datos

print("Conversión de tipos de datos")

# int()
print(int(1.0))
print(int("1"))
print(int(True))
print(int(False))
print(int(b"1"))

# float()
print(float(1))
print(float("1"))
print(float(True))
print(float(False))
print(float(b"1"))

# str()
print(str(1))
print(str("1"))
print(str(True))
print(str(False))
print(str(b"1"))

# bool()
print(bool(1)) # True
print(bool(0)) # False
print(bool("")) # False
print(bool(" ")) # True
print(bool("1")) # True
print(bool("0")) # True
print(bool("False")) # True
print(bool("True")) # True
print(bool("None")) # True