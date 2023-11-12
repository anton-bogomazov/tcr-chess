from src.chess.figures.chess_figure import ChessFigure
from src.chess.figures.king import King
from src.chess.error import InvalidMoveError, CastlingNotPossibleError, InconsistentStateError


# is figure a good place to localize block checking logic? (probably yes)


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
            self.moving(fr, to, figure_to_move)
        elif isinstance(dest_cell_content, ChessFigure):
            self.take(fr, to, figure_to_move, dest_cell_content)
        else:
            raise InconsistentStateError('something else except None or Figure in the cell')
        
    def moving(self, fr, to, figure_to_move):
        if to not in figure_to_move.turns(self.figures):
            raise InvalidMoveError()
        figure_to_move.move(to)
        if figure_to_move.is_transformable_pawn():
            self.transform_pawn(figure_to_move)
        
    def take(self, fr, to, figure_to_move, dest_figure):
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
        
    def is_castling_move(self, fr, to):
        if fr == ('e', 1) and to in {('c', 1), ('g', 1)}:
            return True
        if fr == ('e', 8) and to in {('c', 8), ('g', 8)}:
            return True
        return False
    
    def checked(self, color):
        players_king = [king for king in self.search_board(King) if king.color == color][0]
        opponents_figures = [f for f in self.figures if f.color != color]
        for fig in opponents_figures:
            if players_king.position in fig.turns(self.figures):
                return True
        return False

    def search_board(self, figure_type):
        return [fig for fig in self.figures if isinstance(fig, figure_type)]

    def cell(self, literal, numeral):
        found_figures = [fig for fig in self.figures if fig.position == (literal, numeral)]
        match len(found_figures):
            case 0:
                return None
            case 1:
                return found_figures[0]
            case _:
                raise InconsistentStateError('two figures in the same cell')

    def to_string(self):
        literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        def resolve(cell_content):
            if cell_content is None:
                return ' '
            return cell_content.symbol()

        return [[resolve(self.cell(literal, numeral)) for literal in literals]
                                    for numeral in reversed(range(1, 9))]
