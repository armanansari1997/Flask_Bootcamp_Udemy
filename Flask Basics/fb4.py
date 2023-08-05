from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/information')
def info():
    return '<h1>The world is great</h1>'

@app.route('/name_info/<name>')
def name_info(name):
    # Converting the name into Upper case letters
    return f"<h1>Upper Case : {name.upper()}</h1>"


if __name__ == '__main__':
    app.run()