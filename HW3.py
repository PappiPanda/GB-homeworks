print('*' * 50)
print('задание 1')
print('*' * 50)
print(' ')
print('разделим 2 числа))')
def delenie(num1, num2):
    if num2 == 0:
        print (0)
    else:
        print(num1 / num2)
delenie(int(input('введите первое число: ')), int(input('введите второе число: ')))
#
#
#
print('*' * 50)
print('задание 2')
print('*' * 50)
print(' ')
name = input('введите имя: ')
surname = input('введите фамилию: ')
birth = input('введите дату рождения: ')
city = input('введите город проживания: ')
mail = input('введите адрес электронной почты: ')
phone = input('введите номер телефона: ')

def vivod_stroki(name, surname, birth, city, mail, phone):
    print(f'имя:, {name}, Фамилия: {surname}, дата рождения: {birth}, город проживания: {city}, электронная почта: {mail}, телефон: {phone}')
vivod_stroki(name, surname, birth, city, mail, phone)
#
#
#
print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
print('а сейчас вычислим суумму 2х наибольших чисел из 3х')
n1 = int(input('введите первое число: '))
n2 = int(input('введите второе число: '))
n3 = int(input('введите третье число: '))
def my_func(n1, n2, n3):
    x = [n1, n2, n3]
    x.sort()
    x = x[-2] + x[-1]
    print('результат:', x)
my_func(n1, n2, n3)
#
#
#
print('*' * 50)
print('задание 4')
print('*' * 50)
print(' ')
def my_func(num1, num2):
    return 1 / num1 ** abs(num2)
print(my_func(12, -2))
#
#
#
print('*' * 50)
print('задание 5')
print('*' * 50)
print(' ')
print('программа которая складывает чилса')
def chisla():
    xr = 0
    while True:
        li = input('введиче числа через пробел: ').split()
        for item in li:
            if item == '+':
                return(print('финальная сумма:', xr))
            else:
                li = [x for x in map(int, li)]
                r = sum(li)
        xr = xr + r
        print('ваша сумма:', xr, '- можете добавить ещё число')
chisla()
#
#
#
print('*' * 50)
print('задание 6')
print('*' * 50)
print(' ')
print('А сейчас введенные слова будут писаться с большой буквы')
def int_func(*args):
    word = input("Введите слова: ")
    print(word.title())
    return
int_func()