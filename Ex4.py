'''
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started'
    def stop(self):
        return f'{self.name} stopped'
    def turn_right(self):
        return f'{self.name} turned right'
    def turn_left(self):
        return f'{self.name} turned left'
    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            return f'Speed of {self.name} is normal for town car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is police car'
        else:
            return f'{self.name} is not police car'


ferrari = SportCar(100, 'Red', 'Ferrari', False)
smart = TownCar(30, 'White', 'Smart', False)
chevrolet = WorkCar(70, 'Green', 'Chevrolet', True)
dodge = PoliceCar(110, 'White-Blue', 'Dodge', True)


print(chevrolet.turn_left())
print(f'When {smart.turn_right()}, then {ferrari.stop()}')
print(f'{chevrolet.go()} with speed exactly {chevrolet.show_speed()}')
print(f'{chevrolet.name} is {chevrolet.color}')
print(f'Is {ferrari.name} police car? {ferrari.is_police}')
print(f'Is {chevrolet.name}  police car? {chevrolet.is_police}')
print(ferrari.show_speed())
print(smart.show_speed())
print(dodge.police())
print(dodge.show_speed())