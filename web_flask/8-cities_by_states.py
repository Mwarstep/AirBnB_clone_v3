#!/usr/bin/python3
"""Will start a Flask Web App listening on 0.0.0.0 port 5000
Routes:
    /cities_by_states: Displays a HTML Page listing
    all States and Cities
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Will display a HTML Page with a list of all States and Cities
    sorted by name.
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Will remove the SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
