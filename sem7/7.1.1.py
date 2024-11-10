def center_of_mass(vectors):
    total_vector = sum(vectors, Vector(0, 0, 0))
    n = len(vectors)
    return Vector(total_vector.x / n, total_vector.y / n, total_vector.z / n)