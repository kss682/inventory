from flask_marshmallow import Marshmallow

ma = Marshmallow()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class WarehouseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'location')


class ProductMovementSchema(ma.Schema):
    class Meta:
        fields = (
            'movement_id', 
            'prod_name',
            'from_location',
            'to_location',
            'quantity'
        )


class InventorySchema(ma.Schema):
    class Meta:
        fields = (
            'prod_name',
            'location',
            'quantity',
        )
