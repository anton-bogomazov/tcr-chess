import src.chess.figures as figures
from src.chess.error import InvalidMoveError, CastlingNotPossibleError


# is figure a good place to localize block checking logic? (probably yes)


class ChessBoard:
    def __init__(self, figure_set):
        self.figures = figure_set

    def move(self, fr, to):
        if self.cell(*fr) is None:
            raise ValueError('fr references empty cell')
        figure_to_move = self.cell(*fr)
        dest_cell_cont = self.cell(*to)
        
        if self.is_castling_move(fr, to):
            self.check_if_castling_possible(figure_to_move, fr, to)
            figure_to_move.castle(to)
            self.get_castling_rook(to).castle(to)
        elif dest_cell_cont is None:
            # cant move if blocked by other figure except Knight
            if to not in figure_to_move.turns():
                raise InvalidMoveError()
            figure_to_move.move(to)
        elif isinstance(dest_cell_cont, figures.ChessFigure):
            if dest_cell_cont.color != figure_to_move.color:
                self.figures.remove(dest_cell_cont)
                # cant take if blocked by other figure except Knight
                # pawns take figures diagonally
                if to not in figure_to_move.turns():
                    raise InvalidMoveError()
                figure_to_move.move(to)
            else:
                raise ValueError('you are trying to take your own figure')
        else:
            raise RuntimeError('unexpected error: something else except None or Figure in the cell')

    def check_if_castling_possible(self, figure_to_move, fr, to):
        if figure_to_move.touched:
            raise CastlingNotPossibleError('king is touched')
        if self.get_castling_rook(to) is None or self.get_castling_rook(to).touched:
            raise CastlingNotPossibleError('rook is touched or moved')
        if self.is_castling_blocked(fr, to):
            raise CastlingNotPossibleError('castling blocked by figures')

    def get_castling_rook(self, to):
        if to == ('g', 1):
            return self.cell(*('h', 1))
        if to == ('c', 1):
            return self.cell(*('a', 1))
        if to == ('g', 8):
            return self.cell(*('h', 8))
        if to == ('c', 8):
            return self.cell(*('a', 8))
        
    def is_castling_blocked(self, fr, to):
        from_literal, from_numeral = fr
        to_literal, to_numeral = to

        assert from_numeral == to_numeral

        if ord(from_literal) < ord(to_literal):
            n = 0
            while ord(from_literal) < ord(to_literal)-n:
                if self.cell(to_literal, to_numeral) is not None:
                    return True
                n += 1
        if ord(from_literal) > ord(to_literal):
            n = 0
            while ord(from_literal) > ord(to_literal)+n:
                if self.cell(to_literal, to_numeral) is not None:
                    return True
                n += 1

        return False
    
    def is_castling_move(self, fr, to):
        if fr == ('e', 1) and to in {('c', 1), ('g', 1)}:
            return True
        if fr == ('e', 8) and to in {('c', 8), ('g', 8)}:
            return True
        return False
    
    def checked(self, color):
        players_king = [king for king in self.search_board(figures.King) if king.color == color][0]
        opponents_figures = [f for f in self.figures if f.color != color]
        for fig in opponents_figures:
            if players_king.position in fig.turns():
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
                raise RuntimeError('two figures in the same cell')

    def to_string(self):
        literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        def resolve(cell_content):
            if cell_content is None:
                return ' '
            return cell_content.symbol()

        return [[resolve(self.cell(literal, numeral)) for literal in literals]
                                    for numeral in reversed(range(1, 9))]
