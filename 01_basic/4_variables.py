### Variables

# Variables globales
x = 1
print(x)

# Variables locales
def f():
    x = 2
    print(x)
f()

# Variables reasignables
x = 1
print(x)
x = 2
print(x)

# Cambio de tipo de variable
x = 1
print(x)
x = "1"
print(x)
x = True
print(x)
x = 1.0
print(x)

# Constantes
PI = 3.141592653589793
print(PI)

#types annotations
integer: int = 1
print(integer)
string: str = "1"
print(string)
boolean: bool = True
print(boolean)
float: float = 1.0
print(float)

### Configurar typecheck en el IDE