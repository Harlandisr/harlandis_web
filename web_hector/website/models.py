from ..instance import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Usario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    dni= db.Column(db.String(9))
    telefono= db.Column(db.Integer(9))
    email= db.Column(db.String(150))
    caballo = db.relationship('Caballo') #Creacion de la relacion entre la tabla caballo y usuario

class Caballo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    meters = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('Usuario.id')) #Creacion de la foreign key




