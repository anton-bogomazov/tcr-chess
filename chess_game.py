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
        self.populate_board()

    def populate_board(self):
        def populate_col(col_idx, fig_cons):
            self.board[0][col_idx] = fig_cons(Color.BLACK)
            self.board[1][col_idx] = Pawn(Color.BLACK)
            self.board[6][col_idx] = Pawn(Color.WHITE)
            self.board[7][col_idx] = fig_cons(Color.WHITE)

        populate_col(0, lambda color: Rook(color))
        populate_col(1, lambda color: Knight(color))
        populate_col(2, lambda color: Bishop(color))
        populate_col(3, lambda color: Queen(color))
        populate_col(4, lambda color: King(color))
        populate_col(5, lambda color: Bishop(color))
        populate_col(6, lambda color: Knight(color))
        populate_col(7, lambda color: Rook(color))

    def move(self, fr, to):
        from_literal, from_numeral = fr
        to_literal, to_numeral = to
        if self.cell(from_literal, from_numeral) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(from_literal, from_numeral)
        self.set_cell(to_literal, to_numeral, figure_to_move)
        self.set_cell(from_literal, from_numeral, None)

    def kings(self):
        return [King(Color.WHITE), King(Color.BLACK)]

    def queens(self):
        return [Queen(Color.WHITE), Queen(Color.BLACK)]

    def rooks(self):
        return [Rook(Color.WHITE), Rook(Color.WHITE),
                Rook(Color.BLACK), Rook(Color.BLACK)]

    def bishops(self):
        return [Bishop(Color.WHITE), Bishop(Color.WHITE),
                Bishop(Color.BLACK), Bishop(Color.BLACK)]

    def knights(self):
        return [Knight(Color.WHITE), Knight(Color.WHITE),
                Knight(Color.BLACK), Knight(Color.BLACK)]

    def pawns(self):
        return [Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
                Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
                Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK),
                Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK)]

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
    def __init__(self, color):
        self.color = color


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
    def __init__(self, color):
        super(Pawn, self).__init__(color)
        self.position = ('a', 2)
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
