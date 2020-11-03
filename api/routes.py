from flask import Flask, jsonify, current_app as app
from flask_restful import Api, Resource, reqparse
from api.serializers import ProductSchema, WarehouseSchema, ProductMovementSchema, InventorySchema
from api.models import db, Product, Warehouse, ProductMovement, Inventory

api = Api(app)

class ProductApi(Resource):

    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('name', type=str, required=True)

    def get(self):
        products = Product.query.all()
        product_schemas = ProductSchema(many=True)
        return jsonify(product_schemas.dump(products))

    def post(self):
        product_data = self.reqparser.parse_args()        
        product = Product(
            name=product_data['name']
        )
        db.session.add(product)
        db.session.commit()


class WarehouseApi(Resource):

    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('location', type=str, required=True)
    
    def get(self):
        locations = Warehouse.query.all()      
        warehouse_schema = WarehouseSchema(many=True)
        return jsonify(warehouse_schema.dump(locations))

    def post(self):
        warehouse_data = self.reqparser.parse_args()
        warehouse = Warehouse(
            location=warehouse_data['location']
        )
        db.session.add(warehouse)
        db.session.commit() 


class ProductMovementApi(Resource):
    def get(self):
        movements = ProductMovement.query.all()
        movements_schema = ProductMovementSchema(many=True)
        return jsonify(movements_schema.dump(movements))


class InventoryApi(Resource):
    def get(self):
        inventory = Inventory.query.all()
        inventory_schema = InventorySchema(many=True)
        return jsonify(inventory_schema.dump(inventory))


api.add_resource(ProductApi, '/products', endpoint='products')
api.add_resource(WarehouseApi, '/warehouses', endpoint='warehouses')
api.add_resource(ProductMovementApi, '/productmovement', endpoint='productmovements')
api.add_resource(InventoryApi, '/inventory', endpoint='inventory')