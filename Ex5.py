def summ():
    xr = 0
    while True:
        li = input('write numbers with spaces: ').split()
        r = 0
        for el in range(len(li)):
            if li[el] == 'q':
                return(print('final sum:', xr))
            else:
                r = r + int(li[el])
        xr = xr + r
        print('your sum:', xr, '- you can write more numbers')
summ()