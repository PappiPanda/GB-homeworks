print('*' * 50)
print('задание 1')
print('*' * 50)
k1 = 'Hello'
k2 = 'World'
print(k1 + ' ' + k2)
print ('And now tell us your name and age')
n1 = input('Name: ')
n2 = input('Age: ')
##n2 = int(n2) # перевод из строки в число
print ('Hello ' + n1 + ' you are looks good for ' + n2)
#
#
#
print('*' * 50)
print('задание 2')
print('*' * 50)
print(' ')
print('How about to write what time is now')
print('write in seconds, please')
import time
sec = input('And what time is now: ')
sec = int(sec)
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S",ty_res)
print('So you mean ' + res)
#
#
#
#
print('*' * 50)
print('задание 3')
print('*' * 50)
print(' ')
n1 = input('Write to us any number: ')
n2 = (n1 + n1)
n3 = (n1 + n1 + n1)
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
print ('And after the magic there is ')
print (n1 + n2 + n3)
#
#
#
#
print('*' * 50)
print('задание 4')
print('*' * 50)
print(' ')
n1 = int(input('And write any number again: '))
ls = []
while n1 > 10:
    ls.append(n1 % 10)
    n1 //= 10
r = max(ls)
print('And here is the biggest num your number')
print(r)
#
#
#
print('*' * 50)
print('задание 5-6')
print('*' * 50)
print(' ')
n1 = int(input('Выручка фирмы за месяц: '))
n2 = int(input('Расходы фирмы за месяц: '))
if n1 > n2:
    n3 = n1 - n2
    n3 = str(n3)
    print (n3 + ' - ваша выручка')
    n3 = int(n3)
    n4 = int(input('а сколько у вас сотрудников: '))
    n5 = n3 // n4
    n5 = str(n5)
    print (n5 + ' - от столько прибыли приносит каждый сотрудник')
else:
    n3 = n2 - n1
    n3 = str(n3)
    print ('-' + n3 + ' - ваш овердрафт')