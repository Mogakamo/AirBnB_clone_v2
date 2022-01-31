#!/usr/bin/python3
"""import flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbnb():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cistxt(text):
    """ Return C is <custom_text>"""
    return 'C {:s}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
