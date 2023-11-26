import unittest
from src.chess.game import standard_chess_game
from src.chess.figures.color import Color

import pandas as pd
import chess.pgn
import chess as pgn_chess
import io


class ChessGameProvider:
    def __init__(self, ds_path='games.csv'):
        self.df = pd.read_csv(ds_path)

    def get_next(self):
        games_moves = self._mate_games()[['moves', 'winner']].sample(1)
        moves = games_moves['moves'].iloc[0].split()
        enumerated_moves = [f'{i + 1}. {turn}' for i, turn in enumerate(moves)]
        parsed_game = pgn_chess.pgn.read_game(io.StringIO(' '.join(enumerated_moves)))
        uci_moves = list(map(lambda m: m.uci(), parsed_game.mainline_moves()))
        tupled_moves = list(map(lambda m: (m[:2], m[2:]), uci_moves))

        return tupled_moves, games_moves.iloc[0]['winner']

    def get_n(self, n):
        return [self.get_next() for _ in range(n)]

    def _mate_games(self):
        return self.df[self.df['victory_status'] == 'mate']


class ApprovalTest(unittest.TestCase):

    # it fails sometimes because of lacking en passant capturing implementation
    def test_play_game(self):
        game_provider = ChessGameProvider()

        for (game_moves, winner) in game_provider.get_n(10):
            game = standard_chess_game()
            print(game_moves)
            for move in game_moves:
                game.turn(*move)

            opponent_color = Color.BLACK if Color[winner.upper()] == Color.WHITE else Color.WHITE
            self.assertEqual(opponent_color, game.checked_player())
