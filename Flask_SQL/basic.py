import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# PUSH THE APP INTO THE APP_CONTEXT (Mandatory)
app.app_context().push()

db = SQLAlchemy(app)

# #######################################################

class Puppy(db.Model):
    # OVERRIDE the DEFAULT table name
    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'
    
    # SET THE COLUMNS
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"

