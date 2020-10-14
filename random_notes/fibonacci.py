def fibonacci_gen(n):

    def fibonacci():
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    i = 0
    for f in fibonacci():
        if i == n:
            return f
        i += 1


def fibonacci_r(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_r(n-1) + fibonacci_r(n-2)


f_gen = fibonacci_gen(10)
print(f_gen)
f_r = fibonacci_r(10)
print(f_r)
