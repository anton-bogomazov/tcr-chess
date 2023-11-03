import unittest
import chess_game


class ChessGameTest(unittest.TestCase):
    def from_to_positions_and_figure_type_is_enough_to_make_turn(self):
        result = chess_game.ChessGame().turn('f3', 'e5', 'knight')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
