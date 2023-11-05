from src.chess.figures import Color
from src.chess.board import ChessBoard
from src.chess.sets import standard_chess_figure_set


class ChessGame:

    def __init__(self, figure_set=standard_chess_figure_set()):
        self.board = ChessBoard(figure_set)
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
            raise RuntimeError('Create a new game, this one is finished!')

        def parse_position(p: str):
            return tuple(p)[0], int(tuple(p)[1])

        self.validate_parameters(parse_position(fr), figure)
        self.move_figure(parse_position(fr), parse_position(to))
        self.update_check_condition()
        if self.checkmate:
            raise RuntimeError('Checkmate! The game is over!')
        self.pass_turn()

    def move_figure(self, fr, to):
        self.board.move(fr, to)
        
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