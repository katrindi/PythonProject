from shop_items import *
from shop_customers import *

# Change DIR according to user account.
c1 = Customer.from_json(r"C:\Users\[...]\[...]\Task 4 & 5\c1.json")
print(c1.full_info())
print(c1.get_items())

