#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hellohbnb():
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def CisTxt(text):
	return "C {:s}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pythontxt(text):
	return "Python {:s}".format(text.replace('_', ' '))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
