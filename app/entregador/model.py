from app.extensions import db
from app.model import BaseModel

class Entregador(BaseModel):
    __tablename__ = 'entregador'


    nome = db.Column() # string limitada
    cpf = db.Column(db.String(11)) 
    senha = db.Column(db.String(50))
    entregas = db.Column()
    telefone = db.Column()
    
