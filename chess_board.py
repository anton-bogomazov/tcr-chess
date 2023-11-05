from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop, ChessFigure

# Allow to do castling

class ChessBoard:
    def __init__(self, figure_set):
        self.figures = figure_set

    def move(self, fr, to):
        from_literal, from_numeral = fr
        if self.cell(from_literal, from_numeral) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(from_literal, from_numeral)
        dest_cell_cont = self.cell(*to)
        if dest_cell_cont is None:
            figure_to_move.move(to)
        #castling here
        elif isinstance(dest_cell_cont, ChessFigure):
            if dest_cell_cont.color != figure_to_move.color:
                self.figures.remove(dest_cell_cont)
                figure_to_move.move(to)
            else:
                raise ValueError('you are trying to take your own figure')
        else:
            raise RuntimeError('unexpected error: something else except None or Figure in the cell')

    def checked(self, color):
        kings = [king for king in self.search_board(King) if king.color == color][0]
        opponents_figures = [f for f in self.figures if f.color != color]
        for fig in opponents_figures:
            if kings.position in fig.turns():
                return True
        return False

    def search_board(self, figure_type):
        return [fig for fig in self.figures if isinstance(fig, figure_type)]

    def cell(self, literal, numeral):
        found_figures = [fig for fig in self.figures if fig.position == (literal, numeral)]
        if len(found_figures) == 1:
            return found_figures[0]
        elif len(found_figures) == 0:
            return None
        else:
            raise RuntimeError('two figures in the same cell')
