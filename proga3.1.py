def fibonacci(n):
    fib_numbers = [0, 1]
    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers[n]

n = int(input("Введите N: "))
print(fibonacci(n))
