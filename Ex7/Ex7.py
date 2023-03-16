'''Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''


import json
import codecs

with codecs.open('excercise_7.json', 'w') as jf:
    with open('excercise_7.txt') as f:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = f.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["average_profit"] = k / o
        all_list = [subjects, middle]
        json.dump(all_list, jf, ensure_ascii=False, indent=4)

print(f'Average profit for all firms:\n{all_list}')