num = -1

if num >= 0:
    print('Число больше либо равно 0')

else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test_2'


if str_1 in str_2:
    print('Да')

else:
    print('Нет')


num_float =3.4

if num_float > 0:
    print('Положительное число')

elif num_float == 0:
    print('Ноль')

else:
    print('Число отрицательное')

permit_print = True



if num > 0 and permit_print:
    print('num - положительное число')

elif not permit_print:
    print('Печать запрещена')




int(input())
if num >= 0 and num <= 4:
    print('бакалавриат')

elif num >= 5 and num <= 6:
    print('магистр')

elif num >= 7 and num <= 9:
    print('аспирант')

else:
    print("Введите корректный код обучения")