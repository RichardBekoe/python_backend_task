# Backend Test #

## Deliverables

### To Run ###

- Run
```
python3 setup/init_db.py
python3 -m venv env
python3 -m pip install --requirement requirements.txt
flask --app main run
```

Examples
```
- post order
POST
http://127.0.0.1:5000/orders
json:
{
	"actual_price": 1800,
	"product_id": 4
}
```

```
- list_orders
GET
http://127.0.0.1:5000/orders
```

```
- list_orders and filter_by_product option
GET
http://127.0.0.1:5000/orders?product_id=<value>
```

```
- get_order_by_id
GET
http://127.0.0.1:5000/orders/<value>
get_by_id
```

```
- delete_order_by_id
DELETE 
http://127.0.0.1:5000/orders/<value>
```

```
- update_order
PUT
http://127.0.0.1:5000/orders/<value>
json:
{
	"actual_price": 888,
	"product_id": 3	
}
```

```
- get_metrics
GET
http://127.0.0.1:5000/orders/metrics
```


- A tool such as DB Browser for SQLite can be used to visualise the SQLite database files.
- An API testing tool was used to test responses from the routes and controllers


____

As a new developer at SpeedyBoats, your first task is to help the operational team to manage orders 
and create some metrics.

They have asked you to create an API for them, based on the boilerplate code which they have provided for you.

Selling a boat is hard, it takes a lot of negotiation, this is why every boat has a __list price__ but the sale could happen on a different price. 
Let's call that __actual price__. 

Your tasks:
1. create the endpoints to manage the Orders 
2. create a special endpoint and calculate the discount percentage by product. 
___

__Discount Percentage for a product__

discount percentage = (1 - (total actual price / total list price) ) * 100


__Start Script__

Before you start the development, run the start script to populate the database with some default data.
There are 2 tables: Products and Orders. You don't have to worry about Products, it is populated for your convenience

```
python setup/init_db.py
```

### Your Task ###
1. Create API for Orders to help the sales team manage them.
When listing the Orders there should be an option to filter the response for a particular product


2. Create a special endpoint for the metrics. 
This endpoint doesn't accept any parameter just returns the discount percentage per product based on the orders

