class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


rectangle_1 = Rectangle(3, 9)

rectangle_2 = Rectangle(5, 8)

rectangle_3 = Rectangle(4, 7)

print(rectangle_1.square())

print(rectangle_2.square())

print(rectangle_3.square())

print(rectangle_1.perimeter())

print(rectangle_2.perimeter())

print(rectangle_3.perimeter())



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


math_1 = Math(2, 6)

print(math_1.subtraction())



class Demoqa:
    def __init__(self, text, type='Кнопка', loc=''):
        self.text = text
        self.type = type
        self.loc = loc


    def click(self):
        return f'Клик по кнопке {self.text}'

text_box = Demoqa('Text Box')
check_box = Demoqa('Check Box')
radio_button = Demoqa('Radio Button')
web_tables = Demoqa('Web Tables')

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())






