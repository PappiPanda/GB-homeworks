n1 = int(input('Earnings: '))
n2 = int(input('Costs: '))
n4 = int(input('Number of employees: '))
if n1 > n2:
    n3 = n1 - n2
    n3 = str(n3)
    print (n3 + ' - your profit')
    n3 = int(n3)
    n5 = n3 // n4
    n5 = str(n5)
    print (n5 + ' - profit per employee')
else:
    n3 = n2 - n1
    n3 = str(n3)
    print ('-' + n3 + ' - your loss')