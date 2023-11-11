from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.color import Color
import itertools


class Rook(ChessFigure):
    
    def turns(self, figures=frozenset()):
        literal, numeral = self.position
        turns = [(chr(ord(literal) - i), numeral) for i in range(1, 8)] +\
                [(chr(ord(literal) + i), numeral) for i in range(1, 8)] +\
                [(chr(ord(literal)), numeral + i) for i in range(1, 8)] +\
                [(chr(ord(literal)), numeral - i) for i in range(1, 8)]

        return set(filter(lambda t: not self.is_out_of_board(*t), turns)) - {self.position}

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
            