def task_1():
    values = [1, 5.3, 'home', [10, 9, 8], True]
    print(type(values[0]))
    print(type(values[1]))
    print(type(values[2]))
    print(type(values[3]))
    print(type(values[4]))


task_1()


def task_2():
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(*(task_2()))


def task_3(a: int = 2) -> int:
    return a * a


print(task_3())
