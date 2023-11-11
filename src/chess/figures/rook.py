from src.chess.board_utils import inc_num_pos as up, dec_num_pos as down, dec_lit_pos as left, inc_lit_pos as right, cell, position
from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color
from src.chess.error import OutOfBoardError


class Rook(ChessFigure):
    
    def __calc_moves(self, figures, m):
        result = []
        try:
            cur_position = m(self.position)
            while cell(figures, *cur_position) is None or \
                  cell(figures, *cur_position).color != self.color:
                result.append(cur_position)
                cur_position = m(cur_position)
        except OutOfBoardError:
            pass
        return result

    def turns(self, figures=frozenset()):
        turns = self.__calc_moves(figures, up) + self.__calc_moves(figures, down) +\
                self.__calc_moves(figures, left) + self.__calc_moves(figures, right)

        return set(turns)

    def castle(self, kings_to):
        self.position = self.rook_castling_to(kings_to)
        self.touched = True

    def rook_castling_to(self, to):
        if to == ('g', 1):
            return ('f', 1)
        if to == ('c', 1):
            return ('d', 1)
        if to == ('g', 8):
            return ('f', 8)
        if to == ('c', 8):
            return ('d', 8)

    def notation(self):
        return 'R'

    def symbol(self):
        return '\u2656' if self.color == Color.WHITE else '\u265C'
            