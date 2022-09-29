print('*' * 50)
print('задание 1')
print('*' * 50)
print(' ')
from sys import argv
name, time, salary, bonus = argv
zarplata = (int(time) * int(salary)) + int(bonus)
print(f'Зарплата сотрудника: {zarplata}')
#
#
#
print('*' * 50)
print('задание 2')
print('*' * 50)
print(' ')
spisok = [30, 95,4, 5, 85, 74, 34, 54, 32, 1, 3, 45]
itog = [el for el in spisok if el > spisok[spisok.index(el)-1]]
print('начальный список: ', spisok)
print(' ')
print('итоговый список: ', itog)
#
#
#
print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
print(f'Числа от 20 до 240 кратные 20 или 21: \n{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
#
#
#
print('*' * 50)
print('задание 4')
print('*' * 50)
print(' ')
spisok = [30, 95,4, 4, 34, 74, 34, 54, 32, 1, 3, 95]
itog = [el for el in spisok if spisok.count(el)==1]
print(itog)
#
#
#
print('*' * 50)
print('задание 5')
print('*' * 50)
print(' ')
from functools import reduce
spisok = [el for el in range(99, 1001) if el % 2 == 0]
def formirovanie(prev_el, el):
    return prev_el * el
print(reduce(formirovanie, spisok))
#
#
#
print('*' * 50)
print('задание 6')
print('*' * 50)
print(' ')
from itertools import count
from itertools import cycle
def zadan1(start_num=3, stop_num=20):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
zadan1()


def zadan2(my_list = [1, 2], iteration = 10):
    l = 0
    iter = cycle(my_list)
    while l < iteration:
        print(next(iter))
        l += 1
zadan2()
#
#
#
print('*' * 50)
print('задание 7')
print('*' * 50)
print(' ')
def factorial_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
result = []
for el in factorial_gen(5):
    if i > 10:
        break
    else:
        result.append(el)
        i += 1
print(result)