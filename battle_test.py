import battle
import unittest
import json

FOURUP_HOOK = """{
  "href": "https://battleofbits.com/games/four-up/matches/1",
  "players": {
    "https://battleofbits.com/players/deepblue": "R",
    "https://battleofbits.com/players/garry": "B"
  },
  "turn": "https://battleofbits.com/players/deepblue",
  "loser": "",
  "winner": "",
  "started": "2013-01-01T23:00:01Z",
  "finished": "",
  "moves": "https://battleofbits.com/games/four-up/matches/1/moves",
  "board": [
    ["R","R","R","R","R","R",""],
    ["","","","","","",""],
    ["","","","","","",""],
    ["","","","","","",""],
    ["","B","","","","",""],
    ["","R","B","","","",""]
  ]
}"""


class BattleTestCase(unittest.TestCase):

    def setUp(self):
        self.app = battle.app.test_client()

    def test_four_selection(self):
        headers = [('Content-Type', 'application/json')]
        response = self.app.post('/fourup', data=FOURUP_HOOK, headers=headers)
        move = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(move['column'], 6)

    def test_invite(self):
        headers = [('Content-Type', 'application/json')]
        response = self.app.post('/invite', data={'game': 'fourup'},
                                 headers=headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
