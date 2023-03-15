class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.linl = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home ')

print(home_two.click())


class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text




search = Input('input#search', 'texx')
print(search.loc)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Linc:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

lincs = Linc('loc_1', 'text_1')
print(lincs.text)

titles = Title('loc_1', 'text_1')
print(titles.text)

button = Button('loc_1', 'text_1')
print(button.text)

