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

    def kings(self):
        return self.search_board(King)

    def queens(self):
        return self.search_board(Queen)

    def rooks(self):
        return self.search_board(Rook)
    
    def bishops(self):
        return self.search_board(Bishop)

    def knights(self):
        return self.search_board(Knight)

    def pawns(self):
        return self.search_board(Pawn)

    def search_board(self, figure_type):
        return [fig for row in self.board for fig in row if isinstance(fig, figure_type)]
    
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

    def turns(self):
        literal, numeral = self.position
        turns = [
            (chr(ord(literal) - 2), numeral - 1),
            (chr(ord(literal) - 2), numeral + 1),
            (chr(ord(literal) + 2), numeral - 1),
            (chr(ord(literal) + 2), numeral + 1),
            (chr(ord(literal) - 1), numeral - 2),
            (chr(ord(literal) - 1), numeral + 2),
            (chr(ord(literal) + 1), numeral - 2),
            (chr(ord(literal) + 1), numeral + 2),
        ]
        return list(filter(lambda t: not self.is_out_of_board(*t), turns))

    def move(self, to):
        if to in self.turns():
            self.position = to
            self.touched = True


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
    literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def player_set(figures_row, pawns_row, color):
        rooks = [Rook((lit, figures_row), color) for lit in ('a', 'h')]
        knights = [Knight((lit, figures_row), color) for lit in ('b', 'g')]
        bishops = [Bishop((lit, figures_row), color) for lit in ('c', 'f')]
        figures = [
            Queen(('d', figures_row), color),
            King(('e', figures_row), color)
        ] + rooks + knights + bishops
        pawns = [Pawn((lit, pawns_row), color) for lit in literals]

        return figures + pawns
    
    return player_set(1, 2, Color.WHITE) + \
        player_set(8, 7, Color.BLACK)
