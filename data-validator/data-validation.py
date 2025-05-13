class Product:
    def __init__(self, name: str, price: float, qty: int, discount = 0):
        self.name = self.validate_name(name)
        self.price = self.validate_price(price)
        self.qty = self.validate_qty(qty)
        self.discount = self.validate_discount(discount)


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
    
    def validate_discount(self, discount):
        try:
            discount = float(discount)
        except(ValueError, TypeError):
             raise TypeError("Discount must be float")
        
        if discount < 0 or discount > 100:
             raise ValueError("Discount can not be negative number")
        return discount
        

    def priceCalculate(self):
        return self.price * self.qty
    
    def getDiscount(self, price, discount):
        net_amount = price - (price * discount / 100)
        return net_amount
    


# Example usage
p = Product("Apple", 100, 10, 10) # name, price, qty, discount
print(p.getDiscount(p.price, p.discount))  # Output: 1000.0
