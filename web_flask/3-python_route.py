#!/usr/bin/python3
"""Will start a Flast Web App listening on 0.0.0.0 port 5000
Routes:
    /: will display “Hello HBNB!”
    /hbnb: will display “HBNB”
    /c/<text>: will display “C ”, followed by <text>
    /python/(<text>): display “Python ”, followed by <text>
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Will display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Will display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Will display 'C' followed by <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Will display 'Python' followed by <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
