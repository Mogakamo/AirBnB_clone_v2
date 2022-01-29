#!/usr/bin/python3
from flask imort Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hellohbnb():
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
	return "C {:s}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': ' is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_false=False)
def Pythoniscool(text):
	return 'Python {:s}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
	return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
	return render_template("5-index.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddoreven(n):
	return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
