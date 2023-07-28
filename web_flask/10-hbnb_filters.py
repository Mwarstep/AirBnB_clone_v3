#!/usr/bin/python3
"""Will start a Flask Web App listening on 0.0.0.0 port 5000
Routes:
    /hbnb_filters: Displays a HTML Page like 6-index.html
    (Filters)

"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Will display a HTML Page with the HBNB Filters page.
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Will remove the SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
