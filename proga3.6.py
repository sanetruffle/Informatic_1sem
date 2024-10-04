import numpy as np

def least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return a, b

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 6, 7]
a, b = least_squares(x, y)
print(a, b)
