from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    is_user_logged_in = False
    return render_template('control_flow.html',     
                           is_user_logged_in=is_user_logged_in)



# @app.route('/')
# def index():
#     puppy_names = ['Tommy', 'Sammy', 'Fluppy']
#     return render_template('control_flow.html', puppy_names=puppy_names)


if __name__ == '__main__':
    app.run()