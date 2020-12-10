import re


def calc(s: str) -> int:
    numbers_str = re.findall('[+|-]?[0-9]+', s)
    print(numbers_str)
    return sum((int(number) for number in numbers_str))


print(calc('105+2+3-4+20'))
