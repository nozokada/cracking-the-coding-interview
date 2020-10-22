spots = [
    ['S', 'S', 'S', '.', '.', '.', '.', '.'],
    ['.', 'S', '.', '.', '.', 'S', 'S', 'S'],
    ['.', '.', '.', '.', 'S', 'S', 'S', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'S', '.', '.', '.', '.', '.', '.'],
    ['S', 'S', '.', '.', '.', 'S', '.', 'S'],
    ['S', 'S', '.', 'S', '.', '.', 'S', '.'],
    ['.', 'S', '.', '.', '.', 'S', '.', 'S'],
]


def count_spots(spots):
    visited = [[False for _ in range(len(row))] for row in spots]
    spots_count = 0
    for i in range(len(spots)):
        for j in range(len(spots[i])):
            if spots[i][j] == 'S' and not visited[i][j]:
                traverse_spots(spots, i, j, visited)
                spots_count += 1

    return spots_count


def traverse_spots(spots, row, col, visited):
    if spots[row][col] != 'S':
        return
    visited[row][col] = True

    for r, c in (
        (row, col + 1),
        (row, col - 1),
        (row - 1, col),
        (row + 1, col),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col + 1)
    ):
        if r < 0 or r >= len(spots) or c < 0 or c >= len(spots[r]):
            continue
        if visited[r][c]:
            continue
        traverse_spots(spots, r, c, visited)


print(count_spots(spots))
