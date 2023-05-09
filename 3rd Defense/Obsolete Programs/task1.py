# import the sqlite3 module in order to work with SQLite databases
import sqlite3

# Establish the connection to the database - "shopdatabase.db"
conn = sqlite3.connect('shopdatabase.db')

# Creating a cursor object using the cursor() method to execute SQL commands
c = conn.cursor()

# Create "shops" table
c.execute ("""CREATE TABLE shops (
  id INTEGER PRIMARY KEY,
  name VARCHAR(40) NOT NULL,
  address VARCHAR(100),
  items INTEGER,
  FOREIGN KEY (items) REFERENCES items(id)
)""");

# Create "items" table
c.execute("""CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  barcode VARCHAR(32) UNIQUE,
  name VARCHAR(40) NOT NULL,
  description VARCHAR(200) DEFAULT 'EMPTY',
  unit_price DECIMAL(10, 2) NOT NULL DEFAULT 1.00,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  shop_id INTEGER,
  FOREIGN KEY (shop_id) REFERENCES shops(id),
  CONSTRAINT fk_shop_items FOREIGN KEY (shop_id) REFERENCES shops(id),
  CONSTRAINT fk_items_components FOREIGN KEY (id) REFERENCES components(item_id)
)""");

# Create "components" table
c.execute("""CREATE TABLE components (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20),
  quantity DECIMAL(10, 2) DEFAULT 1.00,
  item_id INTEGER,
  FOREIGN KEY (item_id) REFERENCES items(id)
)""");

# Commit changes and close the connection
conn.commit()
conn.close()
