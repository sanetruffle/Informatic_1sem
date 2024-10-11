import numpy as np

def solve_linear_system(n, m, matrix):
    a = np.array(matrix)[:, :-1]
    b = np.array(matrix)[:, -1]
    solution = np.linalg.solve(a, b)
    return solution

n, m = map(int, input().split())
matrix = [list(map(float, input().split())) for _ in range(n)]
solution = solve_linear_system(n, m, matrix)
print(solution)