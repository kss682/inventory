from flask import Flask
from api.models import db



def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
    # app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        return app
