import unittest
from src.chess.game import standard_chess_game
from src.chess.figures import Color


class ApprovalTest(unittest.TestCase):

    def test_play_a_short_chess_game(self):
        game = standard_chess_game()
        moves = [
            ("f2", "f3", "pawn"),
            ("e7", "e5", "pawn"),
            ("g2", "g4", "pawn"),
            ("d8", "h4", "queen"), # checkmate
        ]
        for move in moves:
            game.turn(*move)

        self.assertEqual(Color.WHITE, game.checked_player)
        
        with self.assertRaises(RuntimeError):
            game.turn("f3", "f4", "pawn")

        self.assertEqual(True, game.checkmate)
        