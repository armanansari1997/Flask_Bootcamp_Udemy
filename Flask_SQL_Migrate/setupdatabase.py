from basic import db, Puppy

# CREATES ALL THE TABLES Model --> DB Table

db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

print(sam.id)   # None
print(frank.id) # None

# ADD ALL SESSION AT ONCE
# with app.app_context():
db.session.add_all([sam, frank])
db.session.commit()

# SAME AS ABOVE! (line - 12)
# db.session.add(sam)
# db.session.add(frank)

# COMMIT THE CHANGES TO THE DATABASE

db.session.commit()

print(sam.id) # None
print(frank.id) # None