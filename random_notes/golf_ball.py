x = 500
highest_floor = 1000
lowest_floor = 1


def drop_first_ball(low: int, high: int, cost: int):
    cost += 1
    drop_from = (low + high) // 2

    if drop_from >= x:
        return low, drop_from, cost

    return drop_first_ball(drop_from + 1, high, cost)


def drop_second_ball(low: int, high: int, cost: int):
    for floor in range(low, high + 1):
        cost += 1
        if x == floor:
            return floor, cost


safe, not_safe, total_cost = drop_first_ball(lowest_floor, highest_floor, 0)
print(f'X is somewhere between {safe} and {not_safe}')
answer, total_cost = drop_second_ball(safe, not_safe, total_cost)
print(f'X: {answer}\nTotal Cost: {total_cost}')
