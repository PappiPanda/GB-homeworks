winter = (1, 2, 12)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)
li_1 = int(input('Type mounth number: '))
print(' ')
if li_1 in winter :
    print('Winter')
elif li_1 in spring:
    print('Spring')
elif li_1 in summer:
    print('Summer')
elif li_1 in autumn:
    print('Autumn')
else:
    print('number is out of range')
#
#
#
#
vre = {'Winter':(1, 2, 12), 'Spring':(3, 4, 5), 'Summer':(6, 7, 8), 'Autumn':(9, 10, 11)}
li_2 = int(input('Type mounth number: '))
print(' ')
for el in vre:
    if li_2 in vre[el]:
       print(el)
    elif li_2 > 12:
       print('number is out of range')