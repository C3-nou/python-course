# Clases
# Las clases son una plantilla para crear objetos. Un objeto es una instancia de una clase.
# Las clases se definen con la palabra reservada class

# Ejemplo de una clase tipo coche

class Coche:
    def __init__(self, marca: str, modelo: str, color: str, precio: int):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def acelerar(self):
        print(f"El coche {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El coche {self.marca} {self.modelo} está frenando")

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo} - {self.color} - {self.precio}"

# Crear un objeto de la clase Coche

coche1 = Coche("Toyota", "Corolla", "Rojo", 10000)
print(coche1.acelerar())
print(coche1.frenar())
print(coche1)

print("---"*10)