def set_zeros(matrix: []):
    height = len(matrix)
    width = len(matrix[0])

    row_with_zero = [False] * height
    column_with_zero = [False] * width

    for row in range(height):
        for column in range(width):
            if matrix[row][column] == 0:
                row_with_zero[row] = True
                column_with_zero[column] = True

    for row in range(height):
        for column in range(width):
            if row_with_zero[row] or column_with_zero[column]:
                matrix[row][column] = 0

    return matrix


def print_matrix(matrix: []):
    for row in matrix:
        for cell in row:
            print(cell, end='\t')
        print()
    print()

