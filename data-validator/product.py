from validator import validate_string, validate_float, validate_int, validate_discount

class Product:
    """
    This is a Product class that handles basic product information.

    Features:
        - Validates input data such as name, price, quantity, and discount.
        - Calculates total price.
        - Applies discount and returns net price after discount.
    """

    def __init__(self, name: str, price: float, qty: int, discount=0):
        self.name = validate_string(name, "Name")
        self.price = validate_float(price, "Price")
        self.qty = validate_int(qty, "Quantity")
        self.discount = validate_discount(discount, "Discount")

    def priceCalculate(self):
        return self.price * self.qty

    def getNetAmount(self):
        discount_amount = (self.price * self.qty) * (self.discount / 100)
        return self.priceCalculate() - discount_amount


# Example usage
p = Product("Apple", "10", "5", 10)  # name, price, qty, discount
print("Total:", p.priceCalculate())         # 50
print("Net after Discount:", p.getNetAmount())  # 45

#print(Product.__dict__)
#print(Product.__doc__)
