from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def serialize(self):
        return {"id": self.id, "product": self.product}


class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False, unique=True)

    def serialize(self):
        return {"id": self.id, "location": self.location}


class ProductMovement(db.Model):
    __tablename__ = 'productmovement'
    movement_id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(255), db.ForeignKey('product.name'))
    from_location = db.Column(db.String(255), db.ForeignKey('warehouse.location'))
    to_location = db.Column(db.String(255), db.ForeignKey('warehouse.location'))
    quantity = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "movement_id": self.movement_id,
            "product_id": self.product_id,
            "from_location": self.from_location,
            "to_location": self.to_location,
            "quantity": self.quantity
        }


class Inventory(db.Model):
    __tablename__ = 'inventory'
    prod_name = db.Column(db.String(255), db.ForeignKey('product.name'), primary_key=True)
    location = db.Column(db.String(255), db.ForeignKey('warehouse.location'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "prod_name": self.prod_name,
            "location": self.location,
            "quantity": self.quantity
        }
    
