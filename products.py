class Product:
    """Represents a single product in the store."""

    def __init__(self, name: str, price: float, quantity: int, active: bool=True):
        if not name:
            raise ValueError('Name can not be empty.')
        if price < 0:
            raise ValueError('Price can not be negative.')
        if quantity < 0:
            raise ValueError('Quantity can not be empty.')

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets the product quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError('Quantity can not be negative.')
        self.quantity = quantity

        if quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        """Returns a formatted string representing the product."""
        return f'{self.name}, Price: {self.price:.2f} $, Quantity: {self.quantity}'

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Args:
            quantity: The amount to buy.

        Returns:
            The total price for the purchase.

        Raises:
            ValueError: If product is inactive, quantity is non-positive,
                        or there is not enough in stock.
        """

        if not self.active == True:
            raise ValueError('You can not buy this product.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')
        if quantity > self.quantity:
            raise ValueError('Not enough in stock.')

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return quantity * self.price
