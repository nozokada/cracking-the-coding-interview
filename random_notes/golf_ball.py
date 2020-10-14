x = 1000
highest = 1000
lowest = 1


def drop_first_ball(low: int, high: int, cost: int):
    cost += 1
    current = (low + high) // 2

    if current >= x:
        return low, current, cost

    return drop_first_ball(current + 1, high, cost)


def drop_second_ball(low: int, high: int, cost: int):
    for floor in range(low, high + 1):
        cost += 1
        if x == floor:
            return floor, cost


safe, not_safe, cost = drop_first_ball(lowest, highest, 0)
answer, cost = drop_second_ball(safe, not_safe, cost)
print(f'X: {answer}\nTotal Cost: {cost}')
