from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop
from chess_board import ChessBoard
from Color import Color

# How to reset checkmate condition?
# If checkmate is still True, set Checkmate
# Checkmate condition

class ChessGame:

    def __init__(self):
        self.board = ChessBoard(standard_chess_figure_set())
        self.players_move = Color.WHITE
        self.check_to = None
        self.checkmate = False

    def turn(self, fr=None, to=None, figure=None):
        if self.checkmate == True:
            raise RuntimeError('Checkmate! The game is over!')

        if fr is None:
            raise TypeError('"from" should be a string')
        if to is None:
            raise TypeError('"to" should be a string')
        if figure is None:
            raise TypeError('"figure" should be a string')
        
        fr_parsed = (tuple(fr)[0], int(tuple(fr)[1]))
        to_parsed = (tuple(to)[0], int(tuple(to)[1]))

        selected_figure = self.board.cell(*fr_parsed)
        if selected_figure.__class__.__name__.lower() != figure:
            raise ValueError('invalid figure')
        if selected_figure.color != self.players_move:
            raise ValueError('it is not your turn')

        self.board.move(fr_parsed, to_parsed)
    
        if self.players_move == self.check_to:
            if self.board.checked(self.players_move):
                self.checkmate = True
                return 'Checkmate! The game is over!'
            else:
                self.check_to = None
     
        if self.board.checked(self.opponent_color()):
            self.check_to = self.opponent_color()
        
        self.players_move = self.opponent_color()
        return True

    def opponent_color(self):
        return Color.BLACK if self.players_move == Color.WHITE else Color.WHITE

    def get_board(self):
        return self.board


def standard_chess_figure_set():
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

