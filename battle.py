import flask
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


@app.route("/invite", methods=["POST"])
def invite():
    if 'reject' in flask.request.args:
        return ('{"error": "I don\'t want to play"}', 400,
                {'Content-Type': 'application/json'})

    if flask.request.json is None:
        raise ValueError("No JSON invite data found")

    game = flask.request.json['game']
    if game != 'fourup':
        msg = '{{"error": "I don\'t know how to play {game}"}}'.format(
            game=game)
        return msg, 400, {'Content-Type': 'application/json'}
    return "OK, let's play"


if __name__ == "__main__":
    app.run(debug=True)
