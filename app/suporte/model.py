from app.extensions import db
from app.model import BaseModel

class Suporte(BaseModel):
    __tablename__ = 'suporte'
    
    codigo_suporte = db.Column()
    telefone = db.Column(db.Integer())
    senha = db.Column()
