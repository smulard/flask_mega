from app import db #db defined in init file
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
'''
The user class inherets from db.Model, a base class for all models from Flask-SQLAlchemy.
The db fields are created as instances of the db.Column class, which takes the field
type as an argument, plus other arguments that allow for indexed columns and addig primary keys.

The __repr__ method tells Python how to print objects of this class, which is useful for debugging.

The Post class represents the blog post written by users. The timestamp field is going to be indexed,
which is useful if you want to retrieve posts in chronological order
'''
class User(db.Model): #Model is part of SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)