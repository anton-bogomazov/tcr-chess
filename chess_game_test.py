import unittest
import chess_game


class ChessGameTest(unittest.TestCase):
    def test_something(self):
        result = chess_game.ChessGame().turn('f3', 'e5', 'knight')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
