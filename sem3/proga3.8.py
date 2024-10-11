import random
import numpy as np

def generate_data(n, a, b):
    x = np.arange(n)
    y = a * x + b + np.array([random.gauss(0, 1) for _ in range(n)])
    return x, y

n = int(input("Введите количество данных: "))
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))

x, y = generate_data(n, a, b)
print("x:", x)
print("y:", y)