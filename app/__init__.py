from flask import Flask
from .config import Config
from .extensions import db, migrate


from app.cliente.model import cliente_api
from app.entrega.model import entrega_api


def create_app():
    
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(entrega_api)


    return app

