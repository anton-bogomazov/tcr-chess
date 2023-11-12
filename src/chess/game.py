from src.chess.figures.color import Color
from src.chess.board import ChessBoard
from src.chess.figures.sets import standard_chess_figure_set
from src.chess.error import CheckmateError, OpponentsTurnError, UnsafeTurnError, InconsistentStateError


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
        self.__validate_parameters(parse_position(fr))
        self.__finish_if_checkmate()
        
        print(f'Moving figure from {fr} to {to}')
        self.__make_turn(parse_position(fr), parse_position(to))
        
        self.__update_check_condition()
        print(f'{self.checked_player} player is checked')
        self.__finish_if_checkmate()
        
        print(f'{self.current_player} is passing turn')
        self.__pass_turn()

    def get_board(self):
        return self.board
    
    def __validate_parameters(self, fr):
        selected_figure = self.board.cell(*fr)
        if selected_figure.color != self.current_player:
            raise OpponentsTurnError()
        
    def __finish_if_checkmate(self):
        if self.checkmate:
            print(f'Checkmate! The game is over!')
            raise CheckmateError()
        
    def __make_turn(self, fr, to):
        try:
            self.board.move(fr, to)
        except UnsafeTurnError:
            # if there is no turn (aka checkmate) make any turn to finish the game
            if self.current_player != self.checked_player:
                raise UnsafeTurnError
            
    def __update_check_condition(self):
        # if current_player was checked last turn
        if self.current_player == self.checked_player:
            # and still checked, declare checkmate
            if self.board.checked(self.current_player):
                self.checkmate = True
            else:
                self.checked_player = None
        # current_player checks opponent
        if self.board.checked(self.__opponent_color()):
            self.checked_player = self.__opponent_color()

    def __pass_turn(self):
        self.current_player = self.__opponent_color()

    def __opponent_color(self):
        return Color.BLACK if self.current_player == Color.WHITE else Color.WHITE


def standard_chess_game():
    return ChessGame(figure_set=standard_chess_figure_set())


def parse_position(p: str):
    return tuple(p)[0], int(tuple(p)[1])
