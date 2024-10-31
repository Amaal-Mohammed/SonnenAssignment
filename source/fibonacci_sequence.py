def fibonacci(range):
    num1 = 0
    num2 = 1
    i = 0
    while i < range:
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i += 1


fibonacci(9)
