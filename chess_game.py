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

    def cell(self, literal, numeral):
        literal_to_idx = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }
        return self.board[numeral-1][literal_to_idx[literal]]


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
    ...


class Color(Enum):
    WHITE = 1,
    BLACK = 2
