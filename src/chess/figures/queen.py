from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color
from functools import reduce


class Queen(ChessFigure):
    def turns(self, figures):
        turns = [up, left], [down, left], [up, right], [down, right], [up], [down], [right], [left]
        return set(reduce(lambda acc, m: acc + self.calc_moves(figures, m), turns, []))

    def notation(self):
        return 'Q'

    def symbol(self):
        return '\u2655' if self.color == Color.WHITE else '\u265B'
