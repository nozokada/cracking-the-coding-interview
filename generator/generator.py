def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


n = 0
for f in fibonacci():
    print(f)
    if n == 10:
        break
    n += 1
