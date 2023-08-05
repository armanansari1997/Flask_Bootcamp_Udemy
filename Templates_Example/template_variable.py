from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "Arman"
    letters = list(name)
    pup_dictionary = {'pup_name': 'Sammy'}
    return render_template('template_eg.html', name=name, letters=letters,
                           pup_dictionary=pup_dictionary)

if __name__ == '__main__':
    app.run()