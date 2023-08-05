from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/information')
def info():
    return '<h1>The World is great</h1>'

# Dynamic Routing
@app.route('/name_info/<name>')
def name_info(name):
    return f"<h1>This is a page for {name} <h1>"

if __name__ == '__main__':
    app.run()