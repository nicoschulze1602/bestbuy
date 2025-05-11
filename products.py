class Product:

    active = True

    def __init__(self, name, price, quantity, active=True):
        if not name:
            raise ValueError('Name can not be empty.')
        if price < 0:
            raise ValueError('Price can not be negative.')
        if quantity < 0:
            raise ValueError('Quantity can not be empty.')

        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Quantity can not be negative.')
        self.quantity = quantity

        if quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity) -> float:
        if not self.active == True:
            raise ValueError('You can not buy this product.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')
        if quantity > self.quantity:
            raise ValueError('Not enough in stock.')

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return self.quantity * self.price



bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())