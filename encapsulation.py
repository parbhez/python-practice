class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner # public attribute
        self._balance = balance #protected attribute
        self.__pin = 1234 #private attribute


    def balance(self):
        return self._balance


    def balance(self, value):
        if value < 0:
            print("Value can not be negative")
        else:
            self._balance = value

    def get_pin(self):
        return self.__pin

    def set_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed successfully!"
        else:
            return "Old pin incorrect"



# ✅ Object creation and usage
account = BankAccount("Masud", 1000)

# Accessing public and protected attributes (not recommended directly)
print("Owner:", account.owner)
print("Balance (via getter):", account.balance)

# ✅ Updating balance via setter
account.balance = 1500
print("Updated Balance:", account.balance)

# ✅ Get and Set PIN
print("Current PIN:", account.get_pin())
print(account.set_pin(1234, 4321))  # Correct old pin
print("Updated PIN:", account.get_pin())
print(account.set_pin(1111, 9999))  # Wrong old pin