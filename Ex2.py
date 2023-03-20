'''
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
oпределить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculation(self):
        self.weigth = 25
        self.tickness = 0.05
        calculation = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {calculation} ton of asphalt for road creation')

road_calc = road(20000, 6)
road_calc.calculation()