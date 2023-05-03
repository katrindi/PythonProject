# import the sqlite3 module in order to work with SQLite databases
import sqlite3

# Establish the connection to the database - "shopdatabase.db"
conn = sqlite3.connect('shopdatabase.db')

# Creating a cursor object using the cursor() method to execute SQL commands
c = conn.cursor()

# Create the records in "shops" table
c.execute("INSERT INTO shops (name, address) VALUES (?, ?)", ('IKI', 'Kaunas, Iki street 1'))
c.execute("INSERT INTO shops (name, address) VALUES (?, ?)", ('MAXIMA', 'Kaunas, Maksima street 2'))

# Create the records in "items" table
c.execute("INSERT INTO items (barcode, name, unit_price, shop_id) VALUES (?, ?, ?, ?)", ('112233112233', 'Žemaičių bread', 1.55, 1))
c.execute("INSERT INTO items (barcode, description, name, unit_price, shop_id) VALUES (?, ?, ?, ?, ?)", ('33333222111', 'Milk from Klaipeda', 'Klaipeda milk', 2.69, 1))
c.execute("INSERT INTO items (barcode, name, unit_price, shop_id) VALUES (?, ?, ?, ?)", ('99898989898', 'Aukštaičių bread', 1.65, 2))
c.execute("INSERT INTO items (barcode, description, name, unit_price, shop_id) VALUES (?, ?, ?, ?, ?)", ('99919191991', 'Milk from Vilnius', 'Vilnius milk', 2.99, 2))

# Create the records in "components" table
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Flour', 1.50, 1))
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Water', 1.00, 1))
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Milk', 1.00, 2))
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Flour', 1.60, 3))
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Water', 1.10, 3))
c.execute("INSERT INTO components (name, quantity, item_id) VALUES (?, ?, ?)", ('Milk', 1.10, 4))

# Commit changes and close the connection
conn.commit()
conn.close()
