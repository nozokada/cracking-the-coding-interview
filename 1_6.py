def rotate(matrix: []):
    size = len(matrix[0])
    for layer in range(int(size / 2)):
        first = layer
        last = size - 1 - layer
        for i in range(first, last):
            top = matrix[first][i]
            # top <- left
            matrix[first][i] = matrix[last - (i - first)][first]
            # left <- bottom
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
            # bottom <- right
            matrix[last][last - (i - first)] = matrix[i][last]
            # right <- top
            matrix[i][last] = top


def print_matrix(matrix: []):
    for row in matrix:
        for cell in row:
            print(cell, end='\t')
        print()
    print()


test_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print_matrix(test_matrix)
rotate(test_matrix)
print_matrix(test_matrix)
