from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    r'''
    Requirements:
        1. Any one lower letter and upper letter should be present is username
        2. username ends with a number
    '''
    lower_letter = False
    upper_letter = False
    num_end = False
    
    username = request.args.get('username')
    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()
    
    # all method takes one argument only
    report = all([lower_letter, upper_letter, num_end])
    return render_template('report.html', report=report, 
                           lower=lower_letter, upper=upper_letter,
                           num_end=num_end)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)