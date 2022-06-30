from app.extensions import db
from app.model import BaseModel

class Supermercado(BaseModel):
    __tablename__ = 'supermercado'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100)) # string limitada
    cnpj = db.Column(db.String(14)) 
    img  = db.Coulumn() # link
    horario_funcionamento = db.Column()