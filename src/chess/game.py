from src.chess.figures.color import Color
from src.chess.figures.king import King
from src.chess.board import ChessBoard
from src.chess.figures.sets import standard_chess_figure_set
from src.chess.error import CheckmateError, OpponentsTurnError


class ChessGame:

    def __init__(self, figure_set):
        self.board = ChessBoard(figure_set)
        self.current_player = Color.WHITE
        self.checked_player = None
        self.checkmate = False

    def turn(self, fr=None, to=None):
        if fr is None:
            raise TypeError('"from" should be a string')
        if to is None:
            raise TypeError('"to" should be a string')
        if self.checkmate:
            print(f'Checkmate! The game is over!')
            raise CheckmateError()

        def parse_position(p: str):
            return tuple(p)[0], int(tuple(p)[1])

        self.validate_parameters(parse_position(fr))
        print(f'Moving figure from {fr} to {to}')
        self.move_figure(parse_position(fr), parse_position(to))
        self.update_check_condition()
        print(f'{self.checked_player} player is checked')
        if self.checkmate:
            raise CheckmateError()
        print(f'{self.current_player} is passing turn')
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

    def validate_parameters(self, fr):
        selected_figure = self.board.cell(*fr)
        if selected_figure.color != self.current_player:
            raise OpponentsTurnError()

    def opponent_color(self):
        return Color.BLACK if self.current_player == Color.WHITE else Color.WHITE

    def checked_king(self):
        return [king for king in self.board.search_board(King) if king.checked(self.board.figures)][0]

    def get_board(self):
        return self.board


def standard_chess_game():
    return ChessGame(figure_set=standard_chess_figure_set())
