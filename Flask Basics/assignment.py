from flask import Flask

app = Flask(__name__)


@app.route('/puppy/<name>')
def puppy_latin(name):
    r"""
    Args:
        name (str)): if name does not ends with 'y' then add y at the end of name
        else remove 'y' from end and add 'iful' at the end of name

    Returns:
        Returning a str
    """
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    
    return f"<h1>Your puppy latin name is : {pupname}</h1>"
    
    
if __name__ == '__main__':
    app.run()