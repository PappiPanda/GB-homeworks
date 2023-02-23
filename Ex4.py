n1 = int(input('Write any number: '))
ls = []
while n1 > 10:
    ls.append(n1 % 10)
    n1 //= 10
r = max(ls)
print(' ')
print(r)