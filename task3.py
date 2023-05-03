# import the sqlite3 module in order to work with SQLite databases
import sqlite3

# Establish the connection to the database - "shopdatabase.db"
conn = sqlite3.connect('shopdatabase.db')

# Creating a cursor object using the cursor() method to execute SQL commands
c = conn.cursor()

# Replace component 'Water' quantity from 1.00 to 1.45 of 'Žemaičių bread', which is in the 'IKI' shop
c.execute("UPDATE components SET quantity = ? WHERE name = ? AND item_id IN (SELECT id FROM items WHERE name = ? AND shop_id IN (SELECT id FROM shops WHERE name = ?))", (1.45, 'Water', 'Žemaičių bread', 'IKI'))

# Delete component 'Milk' from 'Vilnius milk', which is in the 'MAXIMA' shop
c.execute("DELETE FROM components WHERE name = ? AND item_id IN (SELECT id FROM items WHERE name = ? AND shop_id IN (SELECT id FROM shops WHERE name = ?))", ('Milk', 'Vilnius milk', 'MAXIMA'))

# Commit changes and close the connection
conn.commit()
conn.close()
