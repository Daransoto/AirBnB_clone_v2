#!/usr/bin/python3
""" Starts a Flask web application. """
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_and_var(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def Python_and_var(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', states=storage.all("State"))


@app.teardown_appcontext
def teardown_app(Error):
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
