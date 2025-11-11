class Product:
   """Product class"""
def __ini__(self, name = "", price = 0.0):
    """Initialize product"""
    self.name = name
    self.price = price

def __str__(self):
    """String representation of product"""
    return f"{self.name}, ${self.price:,2f}"

