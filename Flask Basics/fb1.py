from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_india():
    return "<h1>Hello India<h1>"


if __name__ == '__main__':
    app.run()