import unittest
import chess_game
from chess_board import ChessBoard
from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop


class ChessGameTest(unittest.TestCase):
    def test_from_to_positions_and_figure_type_is_enough_to_make_turn(self):
        result = chess_game.ChessGame().turn('f3', 'e5', 'knight')
        self.assertEqual(result, True)

    def test_fail_to_make_turn_if_every_arg_is_not_provided(self):
        with self.assertRaises(TypeError):
            chess_game.ChessGame().turn('f3', 'knight')
        with self.assertRaises(TypeError):
            chess_game.ChessGame().turn('f3')
        with self.assertRaises(TypeError):
            chess_game.ChessGame().turn()

    def test_game_has_chess_board(self):
        result = chess_game.ChessGame().get_board()
        self.assertIsInstance(result, ChessBoard)

    def test_initially_board_has_standard_figure_set(self):
        board = chess_game.ChessGame().get_board()

        def count_figs(figure_set, color):
            return sum(f.color == color for f in figure_set)

        def whites_eq_blacks(figure_set, n):
            self.assertEqual(count_figs(figure_set, chess_game.Color.WHITE), n)
            self.assertEqual(count_figs(figure_set, chess_game.Color.BLACK), n)

        whites_eq_blacks(board.search_board(King), 1)
        whites_eq_blacks(board.search_board(Queen), 1)
        whites_eq_blacks(board.search_board(Knight), 2)
        whites_eq_blacks(board.search_board(Bishop), 2)
        whites_eq_blacks(board.search_board(Rook), 2)
        whites_eq_blacks(board.search_board(Pawn), 8)

    def test_figures_initially_placed_at_standard_cells(self):
        board = chess_game.ChessGame().get_board()
        def check_if_positioned_well(fig_row, pawn_row, color):
            for literal in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
                self.assertEqual(board.cell(literal, pawn_row), chess_game.Pawn((literal, pawn_row), color))
            self.assertEqual(board.cell('a', fig_row), chess_game.Rook(('a', fig_row), color))
            self.assertEqual(board.cell('b', fig_row), chess_game.Knight(('b', fig_row), color))
            self.assertEqual(board.cell('c', fig_row), chess_game.Bishop(('c', fig_row), color))
            self.assertEqual(board.cell('d', fig_row), chess_game.Queen(('d', fig_row), color))
            self.assertEqual(board.cell('e', fig_row), chess_game.King(('e', fig_row), color))
            self.assertEqual(board.cell('f', fig_row), chess_game.Bishop(('f', fig_row), color))
            self.assertEqual(board.cell('g', fig_row), chess_game.Knight(('g', fig_row), color))
            self.assertEqual(board.cell('h', fig_row), chess_game.Rook(('h', fig_row), color))

        check_if_positioned_well(1, 2, chess_game.Color.WHITE)
        check_if_positioned_well(8, 7, chess_game.Color.BLACK)

    def test_figure_can_be_moved(self):
        board = chess_game.ChessGame().get_board()
        self.assertEqual(board.cell('b', 1), chess_game.Knight(('b', 1), chess_game.Color.WHITE))
        board.move(('b', 1), ('c', 3))
        self.assertEqual(board.cell('c', 3), chess_game.Knight(('c', 3), chess_game.Color.WHITE))
        self.assertEqual(board.cell('b', 1), None)


if __name__ == '__main__':
    unittest.main()
