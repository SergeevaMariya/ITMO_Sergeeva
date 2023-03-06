a: int = 5
b: str = 'строка'
с: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s



print(indent('123', 123))


def redent(s: str = '') -> int:
    return len(s)


print(redent())


def pident(a: list, b: list) -> int:

    return max(len(a), len(b))

print(pident[1,2], [1, 2, 3, 4]))
