from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(255), nullable=False)


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)


class ProductMovement(db.Model):
    __tablename__ = 'productmovement'
    movement_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    from_location = db.Column(db.Integer, db.ForeignKey('location.id'))
    to_location = db.Column(db.Integer, db.ForeignKey('location.id'))
    quantity = db.Column(db.Integer, nullable=False)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

