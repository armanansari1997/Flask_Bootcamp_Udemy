import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# PUSH THE APP INTO THE APP_CONTEXT (Mandatory)
app.app_context().push()

db = SQLAlchemy(app)

Migrate(app, db)
# #######################################################

class Puppy(db.Model):
    # OVERRIDE the DEFAULT table name
    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'
    
    # SET THE COLUMNS
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.String(70))
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"

