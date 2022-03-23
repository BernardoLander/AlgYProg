class Bebidas():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.buy_count = 0


class Alcholicas(Bebidas):
    def __init__(self, name, price, grado):
        super().__init__(name, price)

        self.grado = grado



class Virgenes(Bebidas):
    def __init__(self, name, price, temperatura):
        super().__init__(name, price)

        self.temperatura = temperatura



class Cliente():
    def __init__(self, name, age, dni):

        self.name = name
        self.age = age
        self.dni = dni
        self.compras = []

        if age < 18:
            self.minor = True
        else:
            self.minor = False
        