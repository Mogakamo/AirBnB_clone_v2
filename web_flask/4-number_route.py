#!/usr/bin/python3
"""import flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbnb():
    """returns hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cistxt(text):
    """returns C <custom_text>"""
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': ' is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pythonistxt(text):
    """returns Python <custom_text>"""
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """returns <n> is a number"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
