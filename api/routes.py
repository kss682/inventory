from flask import Flask, jsonify, current_app as app
from flask_restful import Api, Resource, reqparse
from api.serializers import (
    ProductSchema, 
    StoreSchema,
    BillSchema,
    WarehouseSchema, 
    ProductMovementSchema, 
    InventorySchema
)
from api.models import (
    db, 
    Product, 
    Store,
    Bill,
    Warehouse, 
    ProductMovement, 
    Inventory
)

api = Api(app)


class ProductApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('name', type=str, required=True)
        self.reqparser.add_argument('cost', type=float, required=True)

    def get(self):
        products = Product.query.all()
        product_schemas = ProductSchema(many=True)
        return jsonify(product_schemas.dump(products))

    def post(self):
        product_data = self.reqparser.parse_args() 
        product = Product(       
            name=product_data['name'],
            cost=product_data['cost']
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"status_code": 201})


class StoreApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('prod_name', type=str, required=True)
        self.reqparser.add_argument('quantity', type=int, required=True)
    
    def get(self):
        store_items = Store.query.all()
        store_schemas = StoreSchema(many=True)
        return jsonify(store_schemas.dump(store_items))

    def post(self):
        pass


class BillApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('items', type=dict, required=True)
        self.reqparser.add_argument('total_cost', type=float)
    
    def get(self):
        bill = Bill.query.all()
        bill_schema = BillSchema(many=True)
        return jsonify(bill_schema.dump(bill))
    
    def post(self):
        bill_data = self.reqparser.parse_args()
        bill = Bill(
            items=bill_data['items'],
            total_cost=bill_data['total_cost']
        )
        db.session.add(bill)
        db.session.commit()
        return jsonify({"status_code": 201})


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
        return jsonify({"status_code": 201})


class ProductMovementApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('product_name', type=str, required=True)
        self.reqparser.add_argument('from_location', type=str, required=True)
        self.reqparser.add_argument('to_location', type=str, required=True)
        self.reqparser.add_argument('quantity', type=int, required=True)

    def get(self):
        movements = ProductMovement.query.all()
        movements_schema = ProductMovementSchema(many=True)
        return jsonify(movements_schema.dump(movements))

    def post(self):    
        productmovement_data = self.reqparser.parse_args()
        productmovement = ProductMovement(
            prod_name=productmovement_data['prod_name'],
            from_location=productmovement_data['from_location'],
            to_location=productmovement_data['to_location'],
            quantity=productmovement_data['quantity']
        )
        db.session.add(productmovement)
        db.session.commit()
        return jsonify({"status_code": 201})


class InventoryApi(Resource):

    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('product_name', type=str, required=True)
        self.reqparser.add_argument('location', type=str, required=True)
        self.reqparser.add_argument('quantity', type=int, required=True)
        
    def get(self):
        inventory = Inventory.query.all()
        inventory_schema = InventorySchema(many=True)
        return jsonify(inventory_schema.dump(inventory))

    def post(self):
        inventory_data = self.reqparser.parse_args()
        inventory = Inventory(
            prod_name=inventory_data['prod_name'],
            location=inventory_data['location'],
            quantity=inventory_data['quantity']
        )
        db.session.add(inventory_data)
        db.session.commit()
        return jsonify({"status_code": 200})


api.add_resource(ProductApi, '/products', endpoint='products')
api.add_resource(StoreApi, '/store', endpoint='store')
api.add_resource(WarehouseApi, '/warehouses', endpoint='warehouses')
api.add_resource(ProductMovementApi, '/productmovement', endpoint='productmovements')
api.add_resource(InventoryApi, '/inventory', endpoint='inventory')