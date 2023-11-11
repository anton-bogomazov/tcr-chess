from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class Knight(ChessFigure):
    def turns(self, figures=frozenset()):
        turns = [
            [left, left, down],
            [left, left, up],
            [right, right, down],
            [right, right, up],

            [left, up, up],
            [left, down, down],
            [right, up, up],
            [right, down, down],
        ]

        return set(self.calc_singly_moves(figures, turns))

    def notation(self):
        return 'N'

    def symbol(self):
        return '\u2658' if self.color == Color.WHITE else '\u265E'
            