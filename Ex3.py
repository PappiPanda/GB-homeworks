n1 = int(input('write first number: '))
n2 = int(input('write second number: '))
n3 = int(input('write third number: '))
def my_func(n1, n2, n3):
    x = [n1, n2, n3]
    x.sort()
    x = x[-2] + x[-1]
    print('result:', x)
my_func(n1, n2, n3)