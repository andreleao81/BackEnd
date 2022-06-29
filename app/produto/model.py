from app.extensions import db
from app.model import BaseModel

class Produto():

    id = db.Column(db.Integer, primary_key = True)
    marca = db.Column() # string limitada
    preco = db.Column()
    categoria = db.Column()
    servico = db.Column()
    img = db.Column()
