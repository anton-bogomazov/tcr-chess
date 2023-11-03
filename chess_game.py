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

    def kings(self):
        return [King(), King()]

    def queens(self):
        return [Queen(), Queen()]

    def rooks(self):
        return [Rook(), Rook(), Rook(), Rook()]

    def bishops(self):
        return [Bishop(), Bishop(), Bishop(), Bishop()]

    def knights(self):
        return [Knight(), Knight(), Knight(), Knight()]

    def pawns(self):
        return [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()]


class ChessFigure:
    ...


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
