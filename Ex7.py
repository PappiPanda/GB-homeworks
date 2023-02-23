n1 = float(input("Enter current: "))
n2 = float(input("Enter max: "))
day = 1
if n1 > n2:
    print(day)
while n1 < n2:
    n1 = n1 + n1 / 10
    day += 1
print("Days to reach max -", day)