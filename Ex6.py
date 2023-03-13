'''Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие,
при котором повторение элементов списка прекратится.
'''

# Task1
from itertools import count
from itertools import cycle
def task_1(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
print(task_1(start_num=3, stop_num=10))


# Task2
def task_2(my_list, iteration):
    l = 0
    iter = cycle(my_list)
    while l < iteration:
        print(next(iter))
        l += 1
print(task_2(my_list = [1, 2], iteration = 10))