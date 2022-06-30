from app.extensions import db
from app.model import BaseModel

class Supermercado(BaseModel):
    __tablename__ = 'supermercado'

    nome = db.Column(db.String(100)) # string limitada
    cnpj = db.Column(db.String(14)) 
    produtos = db.Column(db.String())