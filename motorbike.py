class Motorbike:

    def __init__(self, brand, maxspeed, speed, color):
        self.brand = brand
        self.speed = speed
        self.color = color
        self.maxspeed = maxspeed

    def speed_up(self, value):
        if self.speed + value > self.maxspeed:
            self.speed = self.maxspeed
        else:
            self.speed += value

    def speed_down(self, value):
        if self.speed < value:
            self.speed = 0
        else:
            self.speed -= value

    def __str__(self):
        return f'Марка мотоцикла: {self.brand}, Максимальная скорость: {self.maxspeed}, Цвет: {self.color}, Скорость: {self.speed}'


Jawa_360 = Motorbike('Jawa 360', 180, 0, 'Красный')
KAWASAKI_VN900 = Motorbike('Kawasaki VN900', 200, 0, 'Желтый')

Jawa_360.speed_up(100)
KAWASAKI_VN900.speed_up(150)
print(Jawa_360)
print(KAWASAKI_VN900)