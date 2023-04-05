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

# Create a class: "Food", which inherits from the "Item" class
class Food(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price)

    # Rewrite method "full_info" to include "Food" before the item information
    def full_info(self):
        return 'Food ' + super().full_info()

# Create a class: "Drink", which inherits from the "Item" class
class Drink(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price)

    # Rewrite method "full_info" to include "Drink" before the item information
    def full_info(self):
        return 'Drink ' + super().full_info()


# Create instances of Food object
f1 = Food("Bread", 2, 1.3)
f2 = Food("Butter", 1, 1.3)
# Create instances of Drink object
d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

# Print the full information using "full_info" method
print(f1.full_info())
print(f2.full_info())  
print(d1.full_info())  
print(d2.full_info()) 
