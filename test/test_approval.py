import unittest
from src.chess.game import standard_chess_game
from src.chess.figures.color import Color
from src.chess.error import *

import pandas as pd
import chess as pgn_chess
import io


class ChessGameProvider:
    def __init__(self, ds_path='games.csv'):
        self.df = pd.read_csv(ds_path)

    def get_next(self):
        games_moves = self.df[['moves']].sample(1)
        moves = games_moves['moves'].iloc[0].split()
        enumerated_moves = [f'{i + 1}. {turn}' for i, turn in enumerate(moves)]
        parsed_game = pgn_chess.pgn.read_game(io.StringIO(' '.join(enumerated_moves)))
        uci_moves = list(map(lambda m: m.uci(), parsed_game.mainline_moves()))
        tupled_moves = list(map(lambda m: (m[:2], m[2:]), uci_moves))

        return tupled_moves


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

        self.assertEqual(Color.WHITE, game.__checked_player)
        
        with self.assertRaises(CheckmateError):
            game.turn("f3", "f4")

        self.assertEqual(True, game.__checkmate)

    def test_play_game(self):
        game_provider = ChessGameProvider()

        while True:
            game = standard_chess_game()
            moves = game_provider.get_next()
            print(moves)
            for move in moves:
                game.turn(*move)
