#!/usr/bin/python3
"""Will start a Flask Web App listening on 0.0.0.0 port 5000
Routes:
    /states: Displays a HTML Page listing all State objects in DBStorage
    /states/<id>: Displays HTML Page with state <id>
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Will display a HTML Page with a list of all State objects
    """
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Will display a HTML Page with a list of all State <id>
    """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """Will remove the SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
