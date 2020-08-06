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

    return matrix


def print_matrix(matrix: []):
    for row in matrix:
        for cell in row:
            print(cell, end='\t')
        print()
    print()
