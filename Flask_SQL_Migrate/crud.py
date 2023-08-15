from basic import db, Puppy

## CREATE ##
my_puppy = Puppy('Rufus', 5)

db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()  # lists of puppies objects in the TABLE
print(all_puppies)

## SELECT By ID ##
puppy_one = db.session.get(Puppy, 1)
print(puppy_one.name) 

## FILTERS ## 
# PRODUCE SOME SQL CODE!
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())  # ["Frankie is 3 years old"]

## UPDATE ## 
first_puppy = db.session.get(Puppy, 1)
first_puppy.age = 14
db.session.add(first_puppy)
db.session.commit()
print(first_puppy.age)

## DELETE ##
second_puppy = db.session.get(Puppy, 2)
db.session.delete(second_puppy)
db.session.commit()
    
## CHECK THE CHANGES ## 
all_puppies = Puppy.query.all()
print(all_puppies)


r'''Note:
    1. User.query.get(1) is deprecated
    2. Use : db.session.get(User, 1)

'''
