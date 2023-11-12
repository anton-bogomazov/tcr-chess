from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.king import King
from src.chess.error import InvalidMoveError, UnsafeTurnError, InconsistentStateError
from src.chess.board_utils import cell


class ChessBoard:
    def __init__(self, figure_set):
        self.figures = figure_set

    def move(self, fr, to):
        if self.cell(*fr) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(*fr)
        dest_cell_content = self.cell(*to)
        
        if self.is_castling_move(fr, to):
            figure_to_move.castle(self.figures, to)
        elif dest_cell_content is None:
            self.moving(to, figure_to_move)
        elif isinstance(dest_cell_content, ChessFigure):
            self.take(to, figure_to_move)
        else:
            raise InconsistentStateError('something else except None or Figure in the cell')
        
    def moving(self, to, figure_to_move):
        if to not in figure_to_move.turns(self.figures):
            raise InvalidMoveError()
        if not self.is_safe_move(figure_to_move, to):
            raise UnsafeTurnError()
        figure_to_move.move(to)
        if figure_to_move.is_transformable_pawn():
            self.transform_pawn(figure_to_move)
        
    def take(self, to, figure_to_move):
        dest_figure = self.cell(*to)
        if dest_figure.color != figure_to_move.color:
            if to not in figure_to_move.turns(self.figures):
                raise InvalidMoveError()
            self.figures.remove(dest_figure)
            figure_to_move.move(to)
            if figure_to_move.is_transformable_pawn():
                self.transform_pawn(figure_to_move)
        else:
            raise InvalidMoveError('you are trying to take your own figure')

    def transform_pawn(self, pawn):
        self.figures.append(pawn.transform_to())
        self.figures.remove(pawn)
        
    def is_safe_move(self, figure, to):
        # king is not going to stand under attack
        if isinstance(figure, King):
            king = figure
            init_position = king.position
            king.move(to)
            if king.checked(self.figures):
                king.move(init_position)
                return False
            king.move(init_position)
        # figure is not opening king for attack
        else:
            init_position = figure.position
            ally_king = self.king(figure.color)
            figure.move(to)
            if ally_king.checked(self.figures):
                figure.move(init_position)
                return False
            figure.move(init_position)

        return True

    def is_castling_move(self, fr, to):
        if fr == ('e', 1) and to in {('c', 1), ('g', 1)}:
            return True
        if fr == ('e', 8) and to in {('c', 8), ('g', 8)}:
            return True
        return False
    
    def checked(self, color):
        return self.king(color).checked(self.figures)

    def king(self, color):
        kings = [king for king in self.search_board(King) if king.color == color]
        if len(kings) == 1:
            return kings[0]
        else:
            raise InconsistentStateError('No or more than one kings on the same color on the board')
        
    def search_board(self, figure_type):
        return [fig for fig in self.figures if isinstance(fig, figure_type)]

    def cell(self, literal, numeral):
        return cell(self.figures, literal, numeral)
