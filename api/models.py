from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False, unique=True)


class ProductMovement(db.Model):
    __tablename__ = 'productmovement'
    movement_id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(255), db.ForeignKey('product.name'))
    from_location = db.Column(db.String(255), db.ForeignKey('warehouse.location'))
    to_location = db.Column(db.String(255), db.ForeignKey('warehouse.location'))
    quantity = db.Column(db.Integer, nullable=False)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    prod_name = db.Column(db.String(255), db.ForeignKey('product.name'), primary_key=True)
    location = db.Column(db.String(255), db.ForeignKey('warehouse.location'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
