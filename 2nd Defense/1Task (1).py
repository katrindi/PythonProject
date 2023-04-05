# Create a class "Customer" 
class Customer:
    # Create a variable "identifier" inside the "Customer" class 
    identifier = 0

    # Create "Customer" class constructor 
    def __init__(self, customername):
        try:
            # [1-EH] String Check
            if not isinstance(customername, str):
                raise ValueError("Customer name must be a string !")
            # Increment the value (variable "identifier") by one when creating customers 
            Customer.identifier += 1
            # Store the customer name private 
            self.__customername = customername
            # Store the customer identifier 
            self.ident = Customer.identifier
        # Catch error in customer creation process
        # [2-EH] Exception Check
        except Exception as err:
            print("An error occurred while creating a new customer:", str(err))

    # Create a function using the property to retrieve the customer name
    @property
    def customername(self):
        return self.__customername

    # Create a setter method to assign the customer name
    @customername.setter
    def customername(self, value):
        try:
            # [1-EH] String Check
            if not isinstance(value, str):
                raise ValueError("Customer name must be a string !")
            self.__customername = value
        # Catch error in customer name update process
        # [2-EH] Exception Check
        except Exception as err:
            print("An error occurred while updating the customer name:", str(err))

    # Create "get_identifier" method which returns the customer identifier 
    def get_identifier(self):
        try:
            return self.ident
        # Catch error in customer identifier retrieval process
        # [2-EH] Exception Check
        except Exception as err:
            print("An error occurred while updating the customer name:", str(err))
        

    # Create method "full_info" which returns the customer's full information: customer identifier + customer name
    def full_info(self):
        try:
            return '{} {}'.format(self.ident, self.customername)
        # Catch error in customer full info retrieval process
        # [2-EH] Exception Check
        except Exception as err:
            print("An error occurred while updating the customer name:", str(err))

# Create instances of the "Customer" class
c1 = Customer("Jonas Jonaitis")
c2 = Customer("Petras Petraitis")
c3 = Customer("Lukas Lukauskas")

# Print the current value of the "identifier" variable
print(Customer.identifier)

# Print the customers' identifier
print(c1.get_identifier())
print(c2.get_identifier())
print(c3.get_identifier())

# Print the current value of the "identifier" variable
print(Customer.identifier)

# Print the customers' full information
print(c1.full_info())
print(c2.full_info())
print(c3.full_info())
