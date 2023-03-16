'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''


my_list = []
while True:
    line = input("Enter text, tap Enter for exit: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("excercise_1.txt", "w") as f_obj:
        f_obj.writelines(my_list)