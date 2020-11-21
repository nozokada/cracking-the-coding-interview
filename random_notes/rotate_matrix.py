def rotate_matrix_clockwise(matrix: list):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def rotate_matrix_counterclockwise(matrix: list):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            i_ = len(matrix) - 1 - i
            j_ = len(matrix) - 1 - j
            matrix[i][j], matrix[j_][i_] = matrix[j_][i_], matrix[i][j]
    return matrix


def print_matrix(matrix: list):
    for row in matrix:
        for val in row:
            print(val, end='\t')
        print()
    print()


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 1, 2],
     [3, 4, 5, 6]]

print_matrix(m)
print_matrix(rotate_matrix_clockwise(m))
print_matrix(rotate_matrix_counterclockwise(m))
