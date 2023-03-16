'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''


with open("excercise_5.txt", "w") as file:
    numbers = [12, 65, 23, 86, 125]
    file.write(" ".join(str(num) for num in numbers))
with open("excercise_5.txt", "r") as file:
    numbers = file.read().split()
    sum = 0
    for num in numbers:
        sum += int(num)
print("Sum of numbers in file: ", sum)