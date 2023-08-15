# BASIC.PY
# Create Entries into the Table!
from models import db, Puppy, Owner, Toy

# CREATING 2 PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus, fido])
db.session.commit()

# CHECK!
print(Puppy.query.all())

# FILTERS!
# If we have multiple name as rufus then we will get a list of rufus
# Hence we used first() method 
# Other methods are all() , we can also use indexing
# E.g., all()[0] or all()[2]
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# CREATE OWNER OBJECT!
jose = Owner('Jose', rufus.id)

# Give Rufus some Toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS!
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Calling report_toys() method using rufus object
# rufus is a Puppy object
rufus.report_toys()