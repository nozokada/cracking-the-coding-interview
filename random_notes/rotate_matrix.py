def rotate_matrix(matrix: list):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(m)
print(rotate_matrix(m))
