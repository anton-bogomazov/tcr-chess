from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.king import King
from src.chess.error import InvalidMoveError, UnsafeTurnError, InconsistentStateError
from src.chess.board_utils import cell


class ChessBoard:
    def __init__(self, figure_set):
        self.figures = figure_set

    def move_figure(self, fr, to):
        figure_to_move = self.cell(*fr)
        dest_cell_content = self.cell(*to)
        
        if is_castling_move(fr, to):
            figure_to_move.castle(self.figures, to)
        elif dest_cell_content is None:
            self.__moving(to, figure_to_move)
        elif isinstance(dest_cell_content, ChessFigure):
            self.__take(to, figure_to_move)
        else:
            raise InconsistentStateError('something else except None or Figure in the cell')
        
    def is_checked(self, color):
        return self.get_king(color).checked(self.figures)

    def get_king(self, color):
        def search_board(figure_type):
            return [fig for fig in self.figures if isinstance(fig, figure_type)]
        kings = [king for king in search_board(King) if king.color == color]
        if len(kings) == 1:
            return kings[0]
        else:
            raise InconsistentStateError('No or more than one kings on the same color on the board')

    def cell(self, literal, numeral):
        return cell(self.figures, literal, numeral)

    def __moving(self, to, figure_to_move):
        if to not in figure_to_move.turns(self.figures):
            raise InvalidMoveError()
        if not self.__is_safe_for_king(figure_to_move, to):
            raise UnsafeTurnError()
        figure_to_move.move(to)
        if figure_to_move.is_transformable_pawn():
            self.__transform_pawn(figure_to_move)
        
    def __take(self, to, figure_to_move):
        dest_figure = self.cell(*to)
        if dest_figure.color != figure_to_move.color:
            if to not in figure_to_move.turns(self.figures):
                raise InvalidMoveError()
            self.figures.remove(dest_figure)
            figure_to_move.move(to)
            if figure_to_move.is_transformable_pawn():
                self.__transform_pawn(figure_to_move)
        else:
            raise InvalidMoveError('you are trying to take your own figure')

    def __transform_pawn(self, pawn):
        self.figures.append(pawn.transform_to())
        self.figures.remove(pawn)
        
    def __is_safe_for_king(self, figure, to):
        init_position = figure.position
        ally_king = self.get_king(figure.color)
        figure.move(to)
        if ally_king.checked(self.figures):
            figure.move(init_position)
            return False
        figure.move(init_position)

        return True


def is_castling_move(fr, to):
    if fr == ('e', 1) and to in {('c', 1), ('g', 1)}:
        return True
    if fr == ('e', 8) and to in {('c', 8), ('g', 8)}:
        return True
    return False