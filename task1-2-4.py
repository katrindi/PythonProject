from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Task 1 (Creating DB) 
# Program will break if .db file already exists!
engine = create_engine('sqlite:///shop.db', echo=True)
Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    address = Column(String(100))
    items = relationship("Item", back_populates="shop")

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    barcode = Column(String(32), unique=True)
    name = Column(String(40), nullable=False)
    description = Column(String(200), default="EMPTY")
    unit_price = Column(Numeric(10,2), nullable=False, default=1.00)
    created_at = Column(DateTime, default=datetime.now())
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shop = relationship("Shop", back_populates="items")
    components = relationship("Component", back_populates="item")

class Component(Base):
    __tablename__ = 'components'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    quantity = Column(Numeric(10,2), default=1.00)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship("Item", back_populates="components")

Base.metadata.create_all(engine)

# Task 2 (Creating records with values for DB)
Session = sessionmaker(bind=engine)
session = Session()

shop1 = Shop(name='IKI', address='Kaunas, Iki street 1')
shop2 = Shop(name='MAXIMA', address='Kaunas, Maksima street 2')

item1 = Item(barcode='112233112233', name='Žemaičių bread', unit_price=1.55, shop=shop1)
item2 = Item(barcode='33333222111', description='Milk from Klaipeda', name='Klaipeda milk', unit_price=2.69, shop=shop1)
item3 = Item(barcode='99898989898', name='Aukštaičių bread', unit_price=1.65, shop=shop2)
item4 = Item(barcode='99919191991', description='Milk from Vilnius', name='Vilnius milk', unit_price=2.99, shop=shop2)

comp1 = Component(name='Flour', quantity=1.50, item=item1)
comp2 = Component(name='Water', quantity=1.00, item=item1)
comp3 = Component(name='Milk', quantity=1.00, item=item2)
comp4 = Component(name='Flour', quantity=1.60, item=item3)
comp5 = Component(name='Water', quantity=1.10, item=item3)
comp6 = Component(name='Milk', quantity=1.10, item=item4)

session.add_all([shop1, shop2, item1, item2, item3, item4, comp1, comp2, comp3, comp4, comp5, comp6])
session.commit()

# Unfinished
# Print the items of all shops, as well as the components of those
#for shop in session.query(Shop):
#    print(f"Shop name: {shop.name}, address: {shop.address}")
#    for item in shop.items:
#        print(f"Item name: {item.name}, barcode: {item.barcode}, price: {item.unit_price}")
#        for component in item.components:
#            print(f"Component name: {component.name}, quantity: {component.quantity}")
