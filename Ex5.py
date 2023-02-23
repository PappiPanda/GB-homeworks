n1 = int(input('Earnings: '))
n2 = int(input('Costs: '))
if n1 > n2:
    n3 = n1 - n2
    n3 = str(n3)
    print (n3 + ' - your profit')
else:
    n3 = n2 - n1
    n3 = str(n3)
    print ('-' + n3 + ' - your loss')