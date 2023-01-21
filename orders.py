from flask import Blueprint, jsonify, request
from setup.init_db import get_db
import orders_controller


orders_pages = Blueprint('orders', __name__, url_prefix='/orders')

@orders_pages.route('/', methods=['POST'])
def post():
    orders_details = request.get_json()
    actual_price = orders_details["actual_price"]
    product_id = orders_details["product_id"]
    order_id = orders_controller.insert_orders(actual_price, product_id)
    return jsonify(order_id)

@orders_pages.route('/', methods=['GET'])
def list_orders():
    orders = orders_controller.list_orders()
    if request.args:
        product_id = request.args.get('product_id')
        result = orders_controller.filter_by_product(product_id)
        return jsonify(result)
    
    return jsonify(orders)


@orders_pages.route('/<order_id>', methods=['GET'])
def get_order_by_id(order_id):
    result = orders_controller.get_order_by_id(order_id)
    return jsonify(result) 

@orders_pages.route('/<order_id>', methods=['DELETE'])
def delete_order_by_id(order_id):
    result = orders_controller.delete_order_by_id(order_id)
    return jsonify(result)


@orders_pages.route('/<order_id>', methods=['PUT'])
def update_order(order_id):
    orders_details = request.get_json()
    actual_price = orders_details["actual_price"]
    product_id = orders_details["product_id"]
    result = orders_controller.update_order(actual_price, product_id, order_id)
    return jsonify(result)

@orders_pages.route('/metrics', methods=['GET'])
def metrics():
    pass


