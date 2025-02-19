#!/usr/bin/python3
"""
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ display text """
    return render_template("7-states_list.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
