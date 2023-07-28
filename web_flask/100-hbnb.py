#!/usr/bin/python3
"""Will start a Flask Web Application listening 0.0.0.0 port 5000
Routes:
    /hbnb: Will display the HBNB Homepage
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Will display the HBNB Filters Homepage HTML"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', states=states,
                           places=places)


@app.teardown_appcontext
def teardown(exception):
    """Will remover the SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
