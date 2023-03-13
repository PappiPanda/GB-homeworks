'''
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''


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