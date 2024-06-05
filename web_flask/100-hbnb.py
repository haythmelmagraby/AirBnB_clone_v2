#!/usr/bin/python3
""" 11. HBNB filters """
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display hbnb """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)



@app.teardown_appcontext
def teardown(exc):
    """ remove session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
