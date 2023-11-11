from src.chess.figures import *
from src.chess.pawn import Pawn
from src.chess.knight import Knight
from src.chess.king import King


def standard_chess_figure_set():
    literals = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def player_set(figures_row, pawns_row, color):
        rooks = [Rook((lit, figures_row), color) for lit in ('a', 'h')]
        knights = [Knight((lit, figures_row), color) for lit in ('b', 'g')]
        bishops = [Bishop((lit, figures_row), color) for lit in ('c', 'f')]
        figures = [
            Queen(('d', figures_row), color),
            King(('e', figures_row), color)
        ] + rooks + knights + bishops
        pawns = [Pawn((lit, pawns_row), color) for lit in literals]

        return figures + pawns

    return player_set(1, 2, Color.WHITE) + \
           player_set(8, 7, Color.BLACK)