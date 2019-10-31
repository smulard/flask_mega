from app import db #db defined in init file
'''
The user class inherets from db.Model, a base class for all models from Flask-SQLAlchemy.
The db fields are created as instances of the db.Column class, which takes the field
type as an argument, plus other arguments that allow for indexed columns and addig primary keys.

The __repr__ method tells Python how to print objects of this class, which is useful for debugging.
'''
class User(db.Model): #Model is part of SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)