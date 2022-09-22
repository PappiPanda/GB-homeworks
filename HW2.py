print('*' * 50)
print('задание 1')
print('*' * 50)
print(' ')
li = ['Вася', 'съел', 5, 'яблок', 'и их осталось', 4.5, True]
print(li)
print(' ')
for item in li:
    print (item, type(item))
#
#
#
print('*' * 50)
print('задание 2')
print('*' * 50)
print(' ')
li = input('введите числа: ').split()
for item in range(0, len(li)-1, 2):
    li[item], li[item+1] = li[item+1], li[item]
print (li)



print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
zim = (1, 2, 12)
ves = (3, 4, 5)
let = (6, 7, 8)
osn = (9, 10, 11)
li = int(input('введите месяц в виде числа: '))
print(' ')
if li in zim :
    print('Зима')
elif li in ves:
    print('Весна')
elif li in let:
    print('Лето')
elif li in osn:
    print('Осень')
else:
    print('Месяцев всего 12 как бы...')
#
#
#
#
vre = {'Зима':(1, 2, 12), 'Весна':(3, 4, 5), 'Лето':(6, 7, 8), 'Осень':(9, 10, 11)}
li = int(input('введите месяц в виде числа: '))
print(' ')
for el in vre:
    if li in vre[el]:
       print(el)
    elif li > 12:
       print('Месяцев всего 12 как бы...')
#
#
#
print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
li = input("Введите слова: ")
a = li.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
#
#
#
print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
number = int(input("Введите число: "))
li = [7, 4, 3, 2]
c = li.count(number)
for element in li:
    if c > 0:
        i = li.index(number)
        li.insert(i+c, number)
        break
    else:
        if number > element:
            j = li.index(element)
            li.insert(j, number)
            break
        elif number < li[len(li) - 1]:
            li.append(number)
print(li)