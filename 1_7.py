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


def print_matrix(matrix: []):
    for row in matrix:
        for cell in row:
            print(cell, end='\t')
        print()
    print()


test_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
print_matrix(test_matrix)
set_zeros(test_matrix)
print_matrix(test_matrix)
