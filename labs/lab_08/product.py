class Product:
    def __init__(self, name, price, quantity):
        # Includes all info about a single product
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self, count):
        # Takes an integer count and determines whether that many of the product are in stock
        if count <= self.quantity:
            return True
        else:
            return False

    def totalCost(self, count):
        # Takes a count and returns the total cost to buy that many of the product
        return count * self.price

    def removeFromStock(self, count):
        # Takes a count and removes that many of a product from stock
        self.quantity -= count
