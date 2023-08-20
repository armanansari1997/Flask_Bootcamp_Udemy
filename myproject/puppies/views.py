# myproject/puppies/views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy


puppies_blueprints = Blueprint('puppies', __name__, 
                               template_folder='templates/puppies')


@puppies_blueprints.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    
    if form.validate_on_submit():
        name = form.name.data
        
        # Add new puppy to the database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
     
    return render_template('add.html', form=form)


@puppies_blueprints.route('/list')
def list():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprints.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    
    if form.validate_on_submit():
        id = form.id.data
        pup = db.session.get(Puppy, id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    
    return render_template('delete.html', form=form)