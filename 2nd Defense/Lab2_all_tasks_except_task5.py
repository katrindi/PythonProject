class Customer:
    # Class's variable to track the number of customers
    identifier = 0

    # "Customer" class constructor
    def __init__(self, customer_name, item_list=None):
        try:
            # Checking the customer_name value, it should be a string
            if not isinstance(customer_name, str):
                raise ValueError("Customer name must be a string !")
            # .__ makes the customer name private
            self.__customer_name = customer_name
            # Increment the value by one when creating customers
            Customer.identifier += 1
            # customer_identifier will store the customer identifier
            self.customer_identifier = Customer.identifier
            # Create an item_list parameter
            if item_list is None:
                item_list = []
            self.item_list = item_list
        except Exception as err:
            print("An error occurred while creating a new customer:", str(err))

    # Method which returns the customer identifier.
    def get_identifier(self):
        try:
            return "\n{}".format(self.customer_identifier)
        except Exception as err:
            print("An error occurred while updating the customer name:", str(err))

    # Method which returns text consisting of customer identifier + customer name.
    def full_info(self):
        try:
            return "\n{} {}".format(self.customer_identifier, self.__customer_name)
        except Exception as err:
            print("An error occurred while updating the customer name:", str(err))

    def add_item(self, item):
        # Checking the type of the item, if it is correct
        if isinstance(item, (Food, Drink)):
            # Add the item to the item_list
            self.item_list.append(item)

    def get_items(self):
        whole_list = []
        for item in self.item_list:
            whole_list.append(item.full_info().strip())
        return whole_list

    def remove_item(self, index):
        try:
            self.item_list.pop(index)
        except IndexError:
            print("Error removing item")


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
        return "{} {} {} {} \n".format(self.item_name, self.price, self.quantity, self.get_total_price())

    # Method which returns data in the dictionary.
    def to_dict(self):
        item_dict = {'name': self.item_name,
                     'quantity': self.quantity,
                     'price': self.price,
                     'total_price': self.get_total_price()}
        return "{} \n".format(item_dict)


class Food(Item):
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    # Rewriting the method "full_info"
    def full_info(self):
        return "{} {} {} {} {} \n".format("Food", self.item_name, self.price, self.quantity, self.get_total_price())


class Drink(Item):
    def __init__(self, item_name, quantity=1, price=10):
        super().__init__(item_name, quantity, price)

    # Rewriting the method "full_info"
    def full_info(self):
        return "{} {} {} {} {} \n".format("Drink", self.item_name, self.price, self.quantity, self.get_total_price())


c1 = Customer("Jonas Jonaitis", [Food("Bread", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c2 = Customer("Petras Petraitis", [Food("Butter", 1, 1.3), Drink("Sprite", 2, 1.7)])

print(c1.get_items())
print(c2.get_items())

c1.add_item(Drink("Fanta", 10, 1.7))
print(c1.get_items())

c2.remove_item(2)
c2.remove_item(1)
print(c2.get_items())
