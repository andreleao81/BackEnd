from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)

class Entrega(BaseModel):
    __tablename__ = 'entrega'

    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.String(15)) 
    adress = db.Column(db.Integer, db.ForeignKey("cliente.id")) 
    produto = db.Column() 
    quantidade = db.Column()