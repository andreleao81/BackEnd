from app.extensions import db
from app.model import BaseModel

class Produto(BaseModel):
    __tablename__ = 'produto'

   
    marca = db.Column(db.String(100)) # string limitada
    preco = db.Column(db.Integer())
    categoria = db.Column()
    image = db.Column()
