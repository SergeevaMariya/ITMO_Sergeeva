class Soda:
    def __init__(self, gor):
        self.gor = gor

    def show_my_drink(self):
        if self.gor == '':
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.gor}')

water = Soda('лимон')
water2 = Soda('')
water.show_my_drink()
water2.show_my_drink()

