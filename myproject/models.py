##########################
#### MODELS.PY ##############
##########################

# setup 'db' inside __init__.py file under myproject folder
from myproject import db

class Puppy(db.Model):
    
    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    owner = db.relationship('Owner', backref="puppy", uselist=False)
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        
        return f"Puppy name: {self.name} and no owner assigned yet!"


class Owner(db.Model):
    
    __tablename__ = 'owners'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))
    
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self):
        return f"Owner name: {self.name}"
    