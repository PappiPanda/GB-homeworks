li_1 = input('type numbers with spaces: ').split()
for item in range(0, len(li_1) - 1, 2):
    li_1[item], li_1[item + 1] = li_1[item + 1], li_1[item]
print (li_1)