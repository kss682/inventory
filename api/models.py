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


# class ProductMovement(db.Model):
#     pass


# class Inventory(db.Model):
#     pass
