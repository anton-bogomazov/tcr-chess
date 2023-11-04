from dataclasses import dataclass
from enum import Enum


class ChessGame:

    def __init__(self):
        self.board = ChessBoard()

    def turn(self, fr=None, to=None, figure=None):
        if fr is None:
            raise TypeError('"from" should be a string')
        if to is None:
            raise TypeError('"to" should be a string')
        if figure is None:
            raise TypeError('"figure" should be a string')
        return True

    def get_board(self):
        return self.board


class ChessBoard:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.populate_board(chess_figure_set())

    def populate_board(self, figure_set):
        for figure in figure_set:
            self.set_cell(*figure.position, figure)

    def move(self, fr, to):
        from_literal, from_numeral = fr
        to_literal, to_numeral = to
        if self.cell(from_literal, from_numeral) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(from_literal, from_numeral)
        self.set_cell(to_literal, to_numeral, figure_to_move)
        self.set_cell(from_literal, from_numeral, None)

    # def kings(self):
    #     return [King(Color.WHITE), King(Color.BLACK)]
    # 
    # def queens(self):
    #     return [Queen(Color.WHITE), Queen(Color.BLACK)]
    # 
    # def rooks(self):
    #     return [Rook(Color.WHITE), Rook(Color.WHITE),
    #             Rook(Color.BLACK), Rook(Color.BLACK)]
    # 
    # def bishops(self):
    #     return [Bishop(Color.WHITE), Bishop(Color.WHITE),
    #             Bishop(Color.BLACK), Bishop(Color.BLACK)]
    # 
    # def knights(self):
    #     return [Knight(Color.WHITE), Knight(Color.WHITE),
    #             Knight(Color.BLACK), Knight(Color.BLACK)]
    # 
    # def pawns(self):
    #     return [Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
    #             Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
    #             Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK),
    #             Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK)]

    def literal_to_idx(self, literal):
        return {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }[literal]

    def numeral_to_idx(self, numeral):
        return numeral-1

    def cell(self, literal, numeral):
        return self.board[self.numeral_to_idx(numeral)][self.literal_to_idx(literal)]

    def set_cell(self, literal, numeral, figure):
        self.board[self.numeral_to_idx(numeral)][self.literal_to_idx(literal)] = figure


@dataclass()
class ChessFigure:
    def __init__(self, position, color):
        self.color = color
        self.position = position

    def is_out_of_board(self, literal, numeral):
        return literal not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') or numeral > 8 or numeral < 0


class King(ChessFigure):
    ...


class Queen(ChessFigure):
    ...


class Rook(ChessFigure):
    ...


class Bishop(ChessFigure):
    ...


class Knight(ChessFigure):
    ...


class Pawn(ChessFigure):
    def __init__(self, position, color):
        super(Pawn, self).__init__(position, color)
        self.touched = False
        
    def turns(self):
        literal, numeral = self.position
        short_turn = (literal, numeral + 1)
        long_turn = (literal, numeral + 2)
        return short_turn if self.touched else short_turn, long_turn
        
    def move(self, to):
        if to in self.turns():
            self.position = to
            self.touched = True
        

class Color(Enum):
    WHITE = 1,
    BLACK = 2


def chess_figure_set():
    whites = (
        Rook(('a', 1), Color.WHITE),
        Knight(('b', 1), Color.WHITE),
        Bishop(('c', 1), Color.WHITE),
        Queen(('d', 1), Color.WHITE),
        King(('e', 1), Color.WHITE),
        Bishop(('f', 1), Color.WHITE),
        Knight(('g', 1), Color.WHITE),
        Rook(('h', 1), Color.WHITE),

        Pawn(('a', 2), Color.WHITE),
        Pawn(('b', 2), Color.WHITE),
        Pawn(('c', 2), Color.WHITE),
        Pawn(('d', 2), Color.WHITE),
        Pawn(('e', 2), Color.WHITE),
        Pawn(('f', 2), Color.WHITE),
        Pawn(('g', 2), Color.WHITE),
        Pawn(('h', 2), Color.WHITE),
    )
    blacks = (
        Rook(('a', 8), Color.BLACK),
        Knight(('b', 8), Color.BLACK),
        Bishop(('c', 8), Color.BLACK),
        Queen(('d', 8), Color.BLACK),
        King(('e', 8), Color.BLACK),
        Bishop(('f', 8), Color.BLACK),
        Knight(('g', 8), Color.BLACK),
        Rook(('h', 8), Color.BLACK),

        Pawn(('a', 7), Color.BLACK),
        Pawn(('b', 7), Color.BLACK),
        Pawn(('c', 7), Color.BLACK),
        Pawn(('d', 7), Color.BLACK),
        Pawn(('e', 7), Color.BLACK),
        Pawn(('f', 7), Color.BLACK),
        Pawn(('g', 7), Color.BLACK),
        Pawn(('h', 7), Color.BLACK),
    )
    
    return blacks + whites
