from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop


class ChessBoard:
    def __init__(self, figure_set):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.populate_board(figure_set)

    def populate_board(self, figure_set):
        for figure in figure_set:
            self.set_cell(*figure.position, figure)

    def move(self, fr, to):
        from_literal, from_numeral = fr
        to_literal, to_numeral = to
        if self.cell(from_literal, from_numeral) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(from_literal, from_numeral)
        self.set_cell(to_literal, to_numeral, figure_to_move)
        self.set_cell(from_literal, from_numeral, None)

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
        return [fig for row in self.board for fig in row if isinstance(fig, figure_type)]

    def literal_to_idx(self, literal):
        return {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
        }[literal]

    def numeral_to_idx(self, numeral):
        return numeral-1

    def cell(self, literal, numeral):
        return self.board[self.numeral_to_idx(numeral)][self.literal_to_idx(literal)]

    def set_cell(self, literal, numeral, figure):
        self.board[self.numeral_to_idx(numeral)][self.literal_to_idx(literal)] = figure