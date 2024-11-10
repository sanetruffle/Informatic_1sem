import itertools
from math import sqrt

def triangle_area(v1, v2, v3):
    a = abs(v2 - v1)
    b = abs(v3 - v2)
    c = abs(v1 - v3)
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def max_area_triangle(vectors):
    max_area = 0
    max_points = ()
    for v1, v2, v3 in itertools.combinations(vectors, 3):
        area = triangle_area(v1, v2, v3)
        if area > max_area:
            max_area = area
            max_points = (v1, v2, v3)
    return max_area, max_points
