from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color

class Rook(ChessFigure):

    def turns(self, figures=frozenset()):
        turns = self.calc_moves(figures, [up]) + self.calc_moves(figures, [down]) +\
                self.calc_moves(figures, [left]) + self.calc_moves(figures, [right])

        return set(turns)

    def castle(self, kings_to):
        self.position = self.rook_castling_to(kings_to)
        self.touched = True

    def rook_castling_to(self, to):
        castling_map = {
            ('g', 1): ('f', 1),
            ('c', 1): ('d', 1),
            ('g', 8): ('f', 8),
            ('c', 8): ('d', 8),
        }
        return castling_map[to]

    def notation(self):
        return 'R'

    def symbol(self):
        return '\u2656' if self.color == Color.WHITE else '\u265C'
            