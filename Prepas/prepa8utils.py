class product():
    def __init__(self, id, name, stock, colors):
        self.id = id
        self.name = name
        self.stock = stock
        self.colors = colors

class flower(product):
    def __init__(self, id, name, stock, colors):
        product().__init__(id, name, stock, colors)

class seed(product):
   def __init__(self, id, name, stock, colors):
        product().__init__(id, name, stock, colors)



def new_db(db):
    fixdb = []
    for i in range(len(db)):
        if db[i].__getitem__("type") == "flower":
            pass

        else:
            pass