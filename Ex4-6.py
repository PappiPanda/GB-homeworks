'''
4.Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Tech_storage:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Model: ')
            unit_p = int(input(f'Price: '))
            unit_q = int(input(f'Quantity: '))
            unit_d = input(f'Department: ')
            unique = {'Model': unit, 'Price': unit_p, 'Quantity': unit_q, 'Department': unit_d}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Now on stock -\n {self.my_store}')
        except:
            return f'Error in data'

        print(f'For Exit type - Q, if continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Now on stock -\n {self.my_store_full}')
            return f'Finished'
        else:
            return Tech_storage.reception(self)




class Printer(Tech_storage):
    def to_print(self):
        return f'Printer {self.my_unit} '


class Scanner(Tech_storage):
    def to_scan(self):
        return f'Scaner {self.my_unit} '


class Copier(Tech_storage):
    def to_copier(self):
        return f'Copier {self.my_unit} '


unit_1 = Printer('Hp', 2000, 5, 10)
unit_2 = Scanner('Xerox', 1200, 5, 10)
unit_3 = Copier('Brother', 1500, 1, 15)


print(unit_1.reception())

print(unit_2.to_scan())
print(unit_3.to_copier())