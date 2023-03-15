class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        return print(self.url)

home = Page('gfgfg')
home.get()

