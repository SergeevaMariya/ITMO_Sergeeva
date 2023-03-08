def max_num(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)


def varios_num(num_1, num_2):
    number = num_1 - num_2
    if number == 135 or number == -135:
        print('yes')
    else:
        print('no')


varios_num(10, 140)


def number_month(month):
    if month == 12 or month == 1 or month == 2:
        print('зима')
    elif month >= 3 and month <= 5:
        print('весна')
    elif month >= 6 and month <= 8:
        print('лето')
    elif month >= 9 and month <= 11:
        print('осень')
    else:
        print('введите корректный номер')


number_month(8)


def check(num_1, num_2, num_3):
    if num_1 > 10 and num_2 > 10 and num_3 > 10:
        print('yes')
    else:
        print('no')


check(12, 8, 16)

a = [1, 2, 3]


def pozitive_numbers(list):
    numbers = []
    for num in list:
        if num > 0:
            numbers.append(num)
    print(len(numbers))


pozitive_numbers([1, 2, 3, -3, -5])
