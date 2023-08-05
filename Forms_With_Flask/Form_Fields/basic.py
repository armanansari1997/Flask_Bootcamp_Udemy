from flask import (Flask, render_template, session, 
                   redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, RadioField, 
                     SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

# Custom Secret Key
app.config['SECRET_KEY'] = 'my_secret_key'


class InfoForm(FlaskForm):
    # default validators is 'None'
    # Creating DataRequired Object in the validators list
    breed = StringField('what breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been a neutered?')
    mood = RadioField('Please choose your mood:', 
                      choices=[('mood_one', 'Happy'), 
                               ('mood_two', 'Excited')])
    # For unicode strings I have added 'u' before string
    # To prevent the unicode error
    food_choice = SelectField(u'Pick your favourite food:', 
                              choices=[('chi', 'Chicken'), ('mut', 'Mutton'),
                                        ('fish', 'Fish')])
    
    feedback = TextAreaField()
    submit = SubmitField('Submit')
    

@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thankyou'))
    
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
