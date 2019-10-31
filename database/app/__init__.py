'''Application object of an instance of class Flask.
The __name__ variable passed to the flask class is a Python predefined variable, which is set to the name of the module in which it is used.
Flask uses the location of the module passed here as a starting point when it needs to load associated resources, such as template files.

 The app package is defined by the app directory and the __init__.py script. It's references in the 'from app import routes' statement.
The 'app' variable is defined as a instance of class 'Flask' in the '__init__.py' script, which makes it a member of the 'app' package.
The routes are the different URLs that the application implements. In Flask,, handlers for the application routes are written as Python functions,
called 'view functions'. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requents a given URL.

This SQLite database is represented here by an instance. It also has a database migration instance.
The models module from the app defines the structure of the database.
'''
from flask import Flask
from config import Config #import Config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app) #db instance
migrate = Migrate(app, db) #db migration instance

from app import routes, models #py files


