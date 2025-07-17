def exercise1(message: list[str]) -> str:
    return "".join(message[7:])

def exercise2(numbers: list[int]) -> list[int]:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers

def exercise3(pan: list[str], ingredientes: list[str], pan_abajo: list[str]) -> list[str]:
    return pan + ingredientes + pan_abajo

def exercise4(lista: list[int]) -> list[int]:
    return lista * 2

def exercise5(lista: list[int]) -> int:
    return lista[len(lista) // 2]

def exercise6(lista: list[int]) -> list[int]:
    return lista[len(lista) // 2:] + lista[:len(lista) // 2]