from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop


class ChessBoard:
    def __init__(self, figure_set):
        self.figures = figure_set

    def move(self, fr, to):
        from_literal, from_numeral = fr
        if self.cell(from_literal, from_numeral) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(from_literal, from_numeral)
        figure_to_move.move(to)

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
        return [fig for fig in self.figures if isinstance(fig, figure_type)]

    def cell(self, literal, numeral):
        found_figures = [fig for fig in self.figures if fig.position == (literal, numeral)]
        if len(found_figures) == 1:
            return found_figures[0]
        elif len(found_figures) == 0:
            return None
        else:
            raise RuntimeError('two figures in the same cell')
