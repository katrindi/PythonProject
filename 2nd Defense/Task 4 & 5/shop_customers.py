from shop_items import Food, Drink
import json


class Customer:
    # Class's variable to track the number of customers
    identifier = 0

    # "Customer" class constructor
    def __init__(self, customer_name, item_list=None):
        try:
            # Checking the customer_name value which should be a string
            if not isinstance(customer_name, str):
                raise ValueError("Customer name must be a string !")
            # The '.__' makes the customer name private
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

    # Method which adds item to the list.
    def add_item(self, item):
        # Checking the type of the item, if it is correct
        if isinstance(item, (Food, Drink)):
            # Add the item to the item_list
            self.item_list.append(item)
        else print("There is a problem with the item type.")

    def get_items(self):
        whole_list = []
        for item in self.item_list:
            whole_list.append(item.full_info().strip())
        return whole_list

    # Method which removes an item in specific index
    def remove_item(self, index):
        try:
            self.item_list.pop(index)
        except IndexError:
            print("Error removing item")

    # Method which accepts a file path to save the data to.
    def export_to_json(self, path):
        items = []
        for item in self.item_list:
            item_dicts = item.to_dict().copy()
            item_dicts['full'] = (item.full_info())
            items.append(item_dicts)

        whole_list = {
            "name": self.__customer_name,
            "identifier": self.customer_identifier,
            "items": items
        }

        with open(path, "w", encoding="utf8") as file_obj:
            json.dump(whole_list, file_obj, ensure_ascii=False, indent=4)

    # Method which allows importing the customer with its items from the json file
    def from_json(cls, path):
        with open(path, "r", encoding="utf8") as file_obj:
            json_data = json.load(file_obj)
            customer_name = json_data['name']
            Customer.identifier = json_data['identifier']
            item_list = []
            for item_data in json_data['items']:
                full_value = item_data['full']
                item_type = full_value.split()[0]
                if item_type == "Food":
                    item = Food(item_data['name'], item_data['quantity'], item_data['price'])
                elif item_type == "Drink":
                    item = Drink(item_data['name'], item_data['quantity'], item_data['price'])
                else:
                    raise ValueError("Invalid item type found in the JSON file!")
                item_list.append(item)
            return cls(customer_name, item_list)


