from validator import validate_string, validate_float, validate_int, validate_discount
import csv
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

    @classmethod
    def read_csv(cls):
        with open("product.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)

    
    @classmethod
    def read_csv(cls, filename = r"C:\Users\masud\Herd\python\data-validator\product.csv"):
        products = []
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = cls(
                        name=row.get("name", ""),
                        price=row.get("price", 0),
                        qty=row.get("qty", 0),
                        discount=row.get("discount", 0)
                    )
                    products.append(product)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return products





# Example usage
p = Product("Apple", "10", "5", 10)  # name, price, qty, discount
products = Product.read_csv()
for p in products:
    print(f"Name: {p.name}, Total: {p.priceCalculate()}, Net: {p.getNetAmount()}")

# print(Product.all)