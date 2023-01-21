"""
This script creates the database (Products and Orders table) which requires for the task
and populates the Products table with the default data.
"""

import sqlite3
import os

current_folder = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.dirname(current_folder)

# schema file
schema_sql = os.path.join(current_folder, 'schema.sql')
# sqlite
db_speedyboats = os.path.join(db_path, 'db.sqlite3')

def get_db():
    connection = sqlite3.connect(db_speedyboats)
    return connection

db = get_db()
cur = db.cursor()

# create the schema
with open(schema_sql) as f:
    db.executescript(f.read())


# product data
cur.execute("INSERT INTO products (name, list_price) VALUES (?, ?)", ('Catamaran', 1000))
cur.execute("INSERT INTO products (name, list_price) VALUES (?, ?)", ('Dinghy', 150))
cur.execute("INSERT INTO products (name, list_price) VALUES (?, ?)", ('Narrowboat', 500))
cur.execute("INSERT INTO products (name, list_price) VALUES (?, ?)", ('Submarine', 2000))

db.commit()
db.close()