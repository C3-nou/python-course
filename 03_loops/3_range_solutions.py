def exercise1():
    for i in range(1, 11):
        print(i)

def exercise2():
    for i in range(1, 21, 2):
        print(i)

def exercise3():
    for i in range(5, 51, 5):
        print(i)

def exercise4():
    for i in range(10, 0, -1):
        print(i)

def exercise5():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

def exercise6():
    number = int(input("Introduce un número: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")