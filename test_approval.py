import unittest
from chess_game import ChessGame
from Color import Color

class ApprovalTest(unittest.TestCase):

    def test_play_a_short_chess_game(self):
        game = ChessGame()
        moves = [
            ("f2", "f3", "pawn"),
            ("e7", "e5", "pawn"),
            ("g2", "g4", "pawn"),
            ("d8", "h4", "queen"), # checkmate
            ("f3", "f4", "pawn"),
        ]
        for move in moves:
            game.turn(*move)

        self.assertEqual(True, game.checkmate)
        self.assertEqual(Color.WHITE, game.checked_player)
        