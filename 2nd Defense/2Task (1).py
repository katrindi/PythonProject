# Create a class "Item"
class Item:
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, name, quantity=1, price=10):
        # [1-EH] String Check
        if not isinstance(name, str):
            raise ValueError("Product name must be a string !")
        # [2-EH] Number Check
        if not isinstance(quantity, (int, float)):
            raise ValueError("Quantity must be a number !")
        # [3-EH] Number Check
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number !")
        # [4-EH] Number Negative Check
        if quantity < 0:
            raise ValueError("Quantity cannot be negative !")
        # [5-EH] Number Negative Check
        if price < 0:
            raise ValueError("Price cannot be negative !")
        self.name = name
        self.quantity = quantity
        self.price = price

    # Create method "get_total_price", which calculates and returns the total price of an item: item quantity * item price.
    def get_total_price(self):
        return self.quantity * self.price
    
    # Create method "full_info", which returns text consisting of item name, item price, item quantity, and total price
    def full_info(self):
        return '{} {} {} {}'.format(self.name, self.price, self.quantity, self.get_total_price())
    
    # Create method "to_dict", which returns data in the dictionary
    def to_dict(self):
        return {'name': self.name, 'quantity': self.quantity, 'price': self.price, 'total_price': self.get_total_price()}

# Create three Item objects with different parameters
i1 = Item("Carrots")
i2 = Item("Milk", 2, 1.5)
i3 = Item("Bread", price=0.5)

# Print the full information using "full_info" method
print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

# Print the data as a dictionary using "to_dict" method
print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())