def dot_product(N, vector1, vector2):
    scalar = 0
    for i in range(N):
        scalar += vector1[i] * vector2[i]
    return scalar

print(dot_product(3, [1, 2, 3], [4, 5, 6]))