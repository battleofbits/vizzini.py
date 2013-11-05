import os
import flask
import json
import random

app = flask.Flask(__name__)


@app.route("/")
def blunder():
    return "Never get involved in a land war in Asia."


@app.route("/fourup", methods=["POST"])
def fourup_move():
    if flask.request.json is None:
        raise ValueError("No JSON match data found")

    toprow = flask.request.json["board"][0]

    # Find the open spaces
    open_spaces = [i for i, x in enumerate(toprow) if x == ""]

    if len(open_spaces) == 0:
        raise ValueError("No open spaces left on the board")

    # Pick an empty space
    return flask.jsonify(column=random.choice(open_spaces))


if __name__ == "__main__":
    app.run(debug=True)
