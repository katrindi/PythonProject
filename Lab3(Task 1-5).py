from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship, sessionmaker
# A declarative base class is created. It allows to associate tables with classes.
from sqlalchemy.orm import declarative_base
from datetime import datetime
# Use of text in query formation
from sqlalchemy import text
from sqlalchemy import func

# Task 1 - (Creating DB)
# Program will break if .db file already exists!
engine = create_engine('sqlite:///shop26.db', echo=True)
Base = declarative_base()


class Shop(Base):
    # Define the table name
    __tablename__ = 'shops'

    # id value which should be an integer and PK
    id = Column(Integer, primary_key=True)
    # name value which should be a string, max length - 40, not NULL
    name = Column(String(40), nullable=False)
    # address value which should be a string, max length - 100
    address = Column(String(100))
    # items value which should have a relation to Item
    items = relationship("Item", back_populates="shop")

    # __rep__ function is used to show how instances of the class should be represented
    def __repr__(self):
        return f"<Shop(name='{self.name}', address='{self.address}')>"


class Item(Base):
    # Define the table name
    __tablename__ = 'items'

    # id value which should be an integer and PK
    id = Column(Integer, primary_key=True)
    # barcode value which should be a string, max length - 32, unique
    barcode = Column(String(32), unique=True)
    # name value which should be a string, max length - 40, not NULL
    name = Column(String(40), nullable=False)
    # description value which should be a string, max length - 200, default value - EMPTY
    description = Column(String(200), default="EMPTY")
    # unit_price value which should be a decimal (10, 2), not NULL, default value 1.00
    unit_price = Column(Numeric(10,2), nullable=False, default=1.00)
    # created_at value which should be a DateTime, default value - record creation date and time
    created_at = Column(DateTime, default=datetime.now())
    # shop_id which should be an integer, FK to shops.id
    shop_id = Column(Integer, ForeignKey('shops.id'))
    # shop which should has a relation to Shop table
    shop = relationship("Shop", back_populates="items")
    # components which should has a relation to Component table
    components = relationship("Component", back_populates="item")

    # __rep__ function is used to show how instances of the class should be represented
    def __repr__(self):
        return "<Item(name='%s', barcode='%s', description='%s', unit_price='%s')>" % (
            self.name, self.barcode, self.description, self.unit_price)


class Component(Base):
    # Define the table name
    __tablename__ = 'components'

    # id value which should be an integer and PK
    id = Column(Integer, primary_key=True)
    # name value which should be a string, max length - 20
    name = Column(String(20))
    # quantity value which should be a decimal (10, 2), default value 1.00
    quantity = Column(Numeric(10,2), default=1.00)
    # item_id which should be an integer, FK to items.id
    item_id = Column(Integer, ForeignKey('items.id'))
    # item value which should has a relation to Item
    item = relationship("Item", back_populates="components")

    # __rep__ function is used to show how instances of the class should be represented
    def __repr__(self):
        return "<Component(name='%s', quantity=%s)>" % (self.name, self.quantity)


# A table creation in the database
Base.metadata.create_all(engine)

# Task 2 - (Creating records with values for DB)
# Creating a session that lets you "chat" with databases
Session = sessionmaker(bind=engine)
session = Session()

# Create records in shop table
shop1 = Shop(name='IKI', address='Kaunas, Iki street 1')
shop2 = Shop(name='MAXIMA', address='Kaunas, Maksima street 2')
# Create records in Item table
item1 = Item(barcode='112233112233', name='Žemaičių bread', unit_price=1.55, shop=shop1)
item2 = Item(barcode='33333222111', name='Klaipeda milk', description='Milk from Klaipeda', unit_price=2.69, shop=shop1)
item3 = Item(barcode='99898989898', name='Aukštaičių bread', unit_price=1.65, shop=shop2)
item4 = Item(barcode='99919191991', name='Vilnius milk', description='Milk from Vilnius', unit_price=2.99, shop=shop2)
# Create records in Component table
component1 = Component(name='Flour', quantity=1.50, item=item1)
component2 = Component(name='Water', quantity=1.00, item=item1)
component3 = Component(name='Milk', quantity=1.00, item=item2)
component4 = Component(name='Flour', quantity=1.60, item=item3)
component5 = Component(name='Water', quantity=1.10, item=item3)
component6 = Component(name='Milk', quantity=1.10, item=item4)

# New Shop, Item, Component objects are written to the session add_all([])
session.add_all([shop1, shop2, item1, item2, item3, item4, component1, component2, component3, component4, component5, component6])
# Initiating the writing data into the database
session.commit()

# Task 3 - (Updating and deleting data)

# Replace component 'Water' quantity from 1.00 to 1.45 of 'Žemaičių bread', which is in the 'IKI' shop.
# Search the item query with the name 'Žemaičių bread' from shop 1(Iki)
item1_iki = session.query(Item).filter_by(name='Žemaičių bread').filter_by(shop=shop1).one()
# Search the component query with the name 'Water' from item1_iki
component2_iki = session.query(Component).filter_by(name='Water').filter_by(item=item1_iki).one()
# Update it's quantity
component2_iki.quantity = 1.45

# Delete component 'Milk' from 'Vilnius milk', which is in the 'MAXIMA' shop.
# Search the item query with the name 'Vilnius milk' from shop 2(Maxima)
item4_maxima = session.query(Item).filter_by(name='Vilnius milk').filter_by(shop=shop2).one()
# Search the component query with the name 'Milk' from item4_maxima
component_maxima = session.query(Component).filter_by(name='Milk').filter_by(item=item4_maxima).one()
# Delete the component from the session
session.delete(component_maxima)
# Initiating the writing data into the database
session.commit()

# Task 4 - (Printing data)
# Print the items of all shops, as well as the components of those items.

# Query to get all items, their components from all shops
all_queries = session.query(Shop.name, Item.name, Component.name)\
              .join(Item, Shop.id == Item.shop_id)\
              .join(Component, Item.id == Component.item_id)

# Iterate over the results and print the data by using .all() which returns all objects as a list
for result in all_queries.all():
    print(f"Shop: {result[0]}, Item: {result[1]}, Component: {result[2]}")


# Task 5 - (Creating queries)

# Select items that have related components
print("The items with related components:")
items_with_components = session.query(Item).join(Component).all()
print(items_with_components)

# Select items, which name contains 'ien'
# First way
query_ien = session.query(Item).from_statement(text("SELECT * FROM items WHERE name LIKE :name")).\
    params(name='%ien%').all()
# If the len of the query_name_ien is equal to 0,
# It means that there are no matching items
if len(query_ien) == 0:
    print("Didn't find any matching items")
#  If the len is not equal to 0, it means there are matching items
#  Then it will print them
else:
    print("The items which contain 'ien' are:")
    for matched_item in query_ien:
        print("{} {} {} {}".format(matched_item.name,
                                   matched_item.barcode, matched_item.description, matched_item.unit_price))
# Second way
query_name_ien = session.query(Item).filter(Item.name.like("%ead%"))
# If the len of the query_name_ien is equal to 0,
# It means that there are no matching items
if len(query_name_ien.all()) == 0:
    print("Didn't find any items")
else:
    # If the len is not equal to 0, it means there are matching items
    # Then it will print them
    print("The items which contain 'ead' are : {}".format(query_name_ien.all()))


# Count how many components each item consists of
number_components = session.query(Item.name, func.count(Component.id)).join(Component).group_by(Item.id).all()
print(number_components)

# Calculate the quantity of components for each item
sum_components = session.query(Item.name, func.sum(Component.quantity)).join(Component).group_by(Item.id).all()
print(sum_components)


# At your discretion, form a query for the selected data and describe it.
# At your discretion, form a query for the selected data and describe it.
# Query the Component table and filter the records based on quantity -> In which the "quantity is greater than 1"
components = session.query(Component).filter(Component.quantity > 1)

# Print the names and quantities of the components
print("Components with quantity > 1:")
for component in components:
    print(f"{component.name} - {component.quantity}")
