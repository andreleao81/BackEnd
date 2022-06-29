from app.extensions import db
from app.model import BaseModel

class Supermercado(BaseModel):

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column() # string limitada
    cnpj = db.Column(db.String(14)) 
    img  = db.Coulumn() # link
    horario = db.Column()