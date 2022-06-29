from app.extensions import db
from app.model import BaseModel


class Entrega(BaseModel):

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column() # string limitada
    adress = db.Column()
    produto = db.Column()
    quantidade = db.Column()