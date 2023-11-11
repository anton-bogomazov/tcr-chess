from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color


class Queen(ChessFigure):
    def turns(self, figures):
        turns = self.calc_moves(figures, [up, left]) + self.calc_moves(figures, [down, left]) +\
                self.calc_moves(figures, [up, right]) + self.calc_moves(figures, [down, right]) +\
                self.calc_moves(figures, [up]) + self.calc_moves(figures, [down]) +\
                self.calc_moves(figures, [left]) + self.calc_moves(figures, [right])

        return set(turns)

    def notation(self):
        return 'Q'

    def symbol(self):
        return '\u2655' if self.color == Color.WHITE else '\u265B'
