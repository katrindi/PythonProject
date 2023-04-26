class Item:
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        # Checking the item_name value which should be a string
        if not isinstance(item_name, str):
            raise ValueError("Product name must be a string !")
        # Checking the quantity value which should be an int or float
        if not isinstance(quantity, (int, float)):
            raise ValueError("Quantity must be a number !")
        # Checking the price value which should be an int or float
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number !")
        # Checking the quantity value which should be a positive number
        if quantity < 0:
            raise ValueError("Quantity cannot be negative !")
        # Checking the price value which should be a positive number
        if price < 0:
            raise ValueError("Price cannot be negative !")
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    # Method which returns item quantity * item price.
    def get_total_price(self):
        return self.quantity * self.price

    # Method which returns text consisting of item name + item price + item quantity + get_total_price().
    def full_info(self):
        return "{} {} {} {}\n".format(self.item_name, self.price, self.quantity, self.get_total_price())

    # Method which returns data in the dictionary.
    def to_dict(self):
        item_dict = {'name': self.item_name,
                     'quantity': self.quantity,
                     'price': self.price,
                     'total_price': self.get_total_price()}
        return item_dict


class Food(Item):
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    # Rewriting the method "full_info"
    def full_info(self):
        return "{} {} {} {} {}\n".format("Food", self.item_name, self.price, self.quantity, self.get_total_price())


class Drink(Item):
    # Constructor accepts three parameters: item name, quantity (default value 1), price (default value 10).
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    # Rewriting the method "full_info"
    def full_info(self):
        return "{} {} {} {} {}\n".format("Drink", self.item_name, self.price, self.quantity, self.get_total_price())

