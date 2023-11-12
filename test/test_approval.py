import unittest
from src.chess.game import standard_chess_game
from src.chess.figures.color import Color
from src.chess.error import *


class ApprovalTest(unittest.TestCase):

    def test_play_a_short_chess_game(self):
        game = standard_chess_game()
        moves = [
            ("f2", "f3"),
            ("e7", "e5"),
            ("g2", "g4"),
            ("d8", "h4"), # checkmate
        ]
        for move in moves:
            game.turn(*move)

        self.assertEqual(Color.WHITE, game.checked_player)
        
        with self.assertRaises(CheckmateError):
            game.turn("f3", "f4")

        self.assertEqual(True, game.__checkmate)
        