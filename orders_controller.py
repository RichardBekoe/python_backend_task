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

def update_order(actual_price, product_id, order_id):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE orders SET actual_price = ?, product_id = ? WHERE id = ?"
    cursor.execute(statement, [actual_price, product_id, order_id])
    db.commit()
    return True


def get_metrics():
    
    db = get_db()
    cur = db.cursor()

    statement1 = "SELECT COUNT(*) FROM products"
    cur.execute(statement1)
    products_count = cur.fetchone()
    products_count_value = products_count[0]
    discount_percentage_results = []

    for x in range(1, products_count_value + 1):

        product_id = x

        statement2 = "SELECT list_price FROM products WHERE id = ?"
        cur.execute(statement2, [product_id])
        result_list_price = cur.fetchone()
        result_list_price_value = result_list_price[0]

        statement3 = "SELECT actual_price FROM orders WHERE product_id = ?"
        cur.execute(statement3, [product_id])
        array_actual_price = cur.fetchall()

        result = 0
        for y in array_actual_price:
            number_value = y[0]
            result = result + number_value

        total_actual_price = result

        array_length_actual_price = len(array_actual_price)    

        total_list_price = array_length_actual_price * result_list_price_value

        if  total_list_price == 0 :
            discount_percentage = "N/A"
        else:
            discount_percentage = round(((1 - (total_actual_price / total_list_price) ) * 100), 3)

        discount_percentage_results.append([f'product_id {x}', f'discount_percentage {discount_percentage}'])

    return discount_percentage_results
