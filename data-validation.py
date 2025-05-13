class Product:
    def __init__(self, name: str, price: float, qty: int):
        self.name = self.validate_name(name)
        self.price = self.validate_price(price)
        self.qty = self.validate_qty(qty)


    def validate_name(self, name):
            if not isinstance(name, str):
                raise TypeError("Name must be string")
            return name
        
    def validate_price(self, price):
            try:
                price = float(price)
            except (ValueError, TypeError):
                raise TypeError("Price must be float")
            
            if price < 0:
                 raise ValueError("Price must be positive")
            return price

    def validate_qty(self, qty):
            try:
                 qty = int(qty)
            except (ValueError, TypeError):
                 raise TypeError("Qty must be integer")
                 
            if qty < 0:
                 raise ValueError("Qty must be positive")
            return qty
    

    def priceCalculate(self):
        return self.price * self.qty


# Example usage
p = Product("Apple", "10", "10")
print(p.priceCalculate())  # Output: 1000.0
