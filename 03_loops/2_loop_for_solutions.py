def exercise1():
    for i in range(2, 21, 2):
        print(i)

def exercise2():
    numbers = [10, 20, 30, 40, 50]
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def exercise3():
    numbers = [15, 5, 25, 10, 20]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def exercise4():
    words = ["casa", "arbol", "sol", "elefante", "luna"]
    new_words = [word for word in words if len(word) > 5]
    return new_words

def exercise5():
    words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
    letter = input("Introduce una letra: ")
    count = 0
    for word in words:
        if word[0].lower() == letter.lower():
            count += 1
    return count