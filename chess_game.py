from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop
from chess_board import ChessBoard
from Color import Color


class ChessGame:

    def __init__(self):
        self.board = ChessBoard(standard_chess_figure_set())
        self.current_player = Color.WHITE
        self.checked_player = None
        self.checkmate = False

    def turn(self, fr=None, to=None, figure=None):
        if fr is None:
            raise TypeError('"from" should be a string')
        if to is None:
            raise TypeError('"to" should be a string')
        if figure is None:
            raise TypeError('"figure" should be a string')

        if self.checkmate:
            raise RuntimeError('Checkmate! The game is over!')

        def parse_position(p: str):
            return tuple(p)[0], int(tuple(p)[1])

        self.validate_parameters(parse_position(fr), figure)
        self.board.move(parse_position(fr), parse_position(to))
        self.update_check_condition()
        self.pass_turn()

    def update_check_condition(self):
        if self.current_player == self.checked_player:
            if self.board.checked(self.current_player):
                self.checkmate = True
            else:
                self.checked_player = None
        if self.board.checked(self.opponent_color()):
            self.checked_player = self.opponent_color()

    def pass_turn(self):
        self.current_player = self.opponent_color()

    def validate_parameters(self, fr, figure):
        def figure_name(instance):
            return instance.__class__.__name__.lower()

        selected_figure = self.board.cell(*fr)
        if figure_name(selected_figure) != figure:
            raise ValueError('invalid figure')
        if selected_figure.color != self.current_player:
            raise ValueError('it is not your turn')

    def opponent_color(self):
        return Color.BLACK if self.current_player == Color.WHITE else Color.WHITE

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
