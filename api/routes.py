from flask import Flask, jsonify, current_app as app
from api.models import db, Product, Warehouse, ProductMovement, Inventory


def serialization(query_results):
    results = []
    for i in query_results:
        results.append(i.serialize())
    return results


@app.route('/products', methods=['GET'])
def get_products():
    products = serialization(Product.query.all())
    return jsonify(products)


@app.route('/locations', methods=['GET'])
def get_locations():
    locations = serialization(Location.query.all())
    return jsonify(locations)


@app.route('/movements', methods=['GET'])
def get_movements():
    movements = serialization(ProductMovement.query.all())
    return jsonify(movements)


@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = serialization(Inventory.query.all())
    return jsonify(inventory)
