from flask import Flask, jsonify, current_app as app
from api.serializers import ProductSchema, WarehouseSchema, ProductMovementSchema, InventorySchema
from api.models import db, Product, Warehouse, ProductMovement, Inventory


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_schemas = ProductSchema(many=True)
    return jsonify(product_schemas.dump(products))


@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Warehouse.query.all()
    warehouse_schema = WarehouseSchema(many=True)
    return jsonify(warehouse_schema.dump(locations))


@app.route('/movements', methods=['GET'])
def get_movements():
    movements = ProductMovement.query.all()
    movements_schema = ProductMovementSchema(many=True)
    return jsonify(movements_schema.dump(movements))


@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = serialization(Inventory.query.all())
    inventory_schema = InventorySchema(many=True)
    return jsonify(inventory_schema.dump(inventory))
