from setup.init_db import get_db

def insert_orders( actual_price, product_id):
    db = get_db()
    cur = db.cursor()
    statement = "INSERT INTO orders(actual_price, product_id) VALUES (?, ?)"
    cur.execute(statement, [ actual_price, product_id])
    db.commit()
    return cur.lastrowid

def list_orders():
    db = get_db()
    cur = db.cursor()
    query = "SELECT id, actual_price, product_id FROM orders"
    cur.execute(query)
    return cur.fetchall()

def filter_by_product(product_id):
    db = get_db()
    cur = db.cursor()
    statement = "SELECT id, actual_price, product_id FROM orders WHERE product_id = ?"
    cur.execute(statement, [product_id])
    return cur.fetchall()

def get_order_by_id(order_id):
    db = get_db()
    cur = db.cursor()
    statement = "SELECT id, actual_price, product_id FROM orders WHERE id = ?"
    cur.execute(statement, [order_id])
    return cur.fetchone()

def delete_order_by_id(order_id):
    db = get_db()
    cur = db.cursor()
    statement = "DELETE FROM orders WHERE id = ?"
    cur.execute(statement, [order_id])
    db.commit()
    return True
