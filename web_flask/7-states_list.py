#!/usr/bin/python3
"""Will start a Flask Web App listening on 0.0.0.0 port 5000
Routes:
    /states_list: Displays a HTML Page listing
    all State objects in the DBStorage
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Will display a HTML Page with a list of all State objects in DB Storage
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Will remove the SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
