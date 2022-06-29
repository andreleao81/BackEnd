from app.extensions import db
from app.model import BaseModel

class Suporte(BaseModel):

    id = db.Column(db.Integer, primary_key = True)
    # nome = db.Column() # string limitada
    # cpf = db.Column(db.String(11)) 
    # 4o atributo
