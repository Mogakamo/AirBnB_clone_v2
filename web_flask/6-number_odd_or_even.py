#!/usr/bin/python3
"""import flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbnb():
    """returns hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
    """returns C <some_text>"""
    return "C {:s}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': ' is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pythoniscool(text):
    """returns Python <some_text>"""
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ returns <n> is a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """renders a template file"""
    return render_template("5-index.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
    """checks if a number is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
