#importar sql alchemy
from flask_sqlalchemy import SQLAlchemy
#creamos un objeto que va a manejar la conexion y el acceso a la base de datos
db=SQLAlchemy()
class Favorite(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    api_id=db.Column(db.Integer,unique=True,)
    name=db.Column(db.String(100))
    image=db.Column(db.String(255))
    