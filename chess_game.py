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
        self.board = [[None] * 8] * 8
        self.board[7][0] = Rook(Color.WHITE)

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
        map = {
            'a': 0
        }
        return self.board[map[literal]][numeral-1]


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
