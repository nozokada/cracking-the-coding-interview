def fibonacci_g(n: int):
    i = 0
    for f in fibonacci_gen():
        if i == n:
            return f
        i += 1


def fibonacci_gen():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def fibonacci_r(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_r(n-1) + fibonacci_r(n-2)


# Return a list of specified number of Fibonacci numbers
# which come after a certain Fibonacci number
def fibonacci_check(number: int, count: int) -> list:
    fibonacci_generator = fibonacci_gen()
    fibonacci_list = []
    for n in fibonacci_generator:
        if n > number:
            print(f'{number} is not a fibonacci number')
            return []
        if n == number:
            fibonacci_list.append(n)
            break

    i = 1
    for n in fibonacci_generator:
        fibonacci_list.append(n)
        i += 1
        if i == count:
            break
    return fibonacci_list


print(fibonacci_g(10))
print(fibonacci_r(10))
print(fibonacci_check(55, 10))
