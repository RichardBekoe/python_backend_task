from setup.init_db import get_db

def insert_orders( actual_price, product_id):
    db = get_db()
    cur = db.cursor()
    statement = "INSERT INTO orders(actual_price, product_id) VALUES (?, ?)"
    cur.execute(statement, [ actual_price, product_id])
    db.commit()
    return cur.lastrowid