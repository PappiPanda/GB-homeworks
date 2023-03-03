number = int(input("Type number: "))
li_1 = [7, 4, 3, 2]
c = li_1.count(number)
for element in li_1:
    if c > 0:
        i = li_1.index(number)
        li_1.insert(i + c, number)
        break
    else:
        if number > element:
            j = li_1.index(element)
            li_1.insert(j, number)
            break
        elif number < li_1[len(li_1) - 1]:
            li_1.append(number)
print(li_1)