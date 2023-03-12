class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def starting(self):
        return 'Автомобиль заведен'

    def disconnection(self):
        return 'Автомобиль заглушен'

    def year_of_manufacture(self, year2):
         self.year = year2

    def type_of_car(self,type2 ):
         self.type = type2

    def color_of_car(self, color2):
         self.color = color2



haval = Car('2021', 'хэчбэк', 'белая')
haval.type_of_car('внедорожник')
print(haval.starting())
