'''
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
'''

with open('excercise_3.txt', 'r') as f:
    salaries = []
    for line in f:
        name, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            print(name)
        salaries.append(salary)

    avg_salary = sum(salaries) / len(salaries)
    print("Average salary: ", avg_salary)

