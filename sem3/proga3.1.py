def f(n):
    fn = [0, 1]
    for i in range(2, n+1):
        fn.append(fn[-1] + fn[-2])
    return fn[n]

n = int(input("Введите N: "))
print(f(n))