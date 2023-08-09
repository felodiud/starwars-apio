from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }


db = SQLAlchemy()


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    jedi = db.Column(db.Boolean, nullable=False)
    origin = db.Column(db.String(200), ForeignKey('planet.name'))
    planet = db.relationship(db.Planet)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "origin": self.origin,
            "jedi": self.origin,
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def to_dic(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
        }
