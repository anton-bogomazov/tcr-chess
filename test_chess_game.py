import unittest
import chess_game
from chess_board import ChessBoard
from chess_figures import Pawn, Rook, King, Queen, Knight, Bishop
from Color import Color


class ChessGameTest(unittest.TestCase):
    def test_from_to_positions_and_figure_type_is_enough_to_make_turn(self):
        result = chess_game.ChessGame().turn('b1', 'c3', 'knight')
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

    def test_figure_can_be_moved_to_empty_cell(self):
        board = chess_game.ChessGame().get_board()
        self.assertEqual(board.cell('b', 1), chess_game.Knight(('b', 1), chess_game.Color.WHITE))
        board.move(('b', 1), ('c', 3))
        self.assertEqual(board.cell('c', 3), chess_game.Knight(('c', 3), chess_game.Color.WHITE))
        self.assertEqual(board.cell('b', 1), None)

    def test_figure_can_take_opponents_figure(self):
        board = chess_game.ChessGame().get_board()
        board.move(('b', 1), ('c', 3))
        board.move(('c', 3), ('d', 5))

        self.assertIsInstance(board.cell('c', 7), Pawn)
        self.assertEqual(board.cell('c', 7).color, chess_game.Color.BLACK)
        board.move(('d', 5), ('c', 7))
        self.assertIsInstance(board.cell('c', 7), Knight)
        self.assertEqual(len(board.search_board(Pawn)), 15)

    def test_whites_starts(self):
        self.assertEquals(
            chess_game.ChessGame().players_move,
            Color.WHITE
        )
        
    def test_pass_turn(self):
        game = chess_game.ChessGame()
        game.turn('b1', 'c3', 'knight')
        self.assertEquals(
            game.players_move,
            Color.BLACK
        )

    def test_cant_move_white_piece_in_the_blacks_turn(self):
        game = chess_game.ChessGame()
        game.turn('b1', 'c3', 'knight')
        with self.assertRaises(ValueError):
            game.turn('g1', 'f3', 'knight')

    def test_check_condition(self):
        game = chess_game.ChessGame()
        game.turn('b1', 'c3', 'knight')
        game.turn('a7', 'a6', 'pawn')
        game.turn('c3', 'b5', 'knight')
        game.turn('a6', 'a5', 'pawn')
        game.turn('b5', 'c7', 'knight')
        self.assertEqual(Color.BLACK, game.check_to)

    def test_checkmate_condition(self):
        game = chess_game.ChessGame()
        game.turn('b1', 'c3', 'knight')
        game.turn('a7', 'a6', 'pawn')
        game.turn('c3', 'b5', 'knight')
        game.turn('a6', 'a5', 'pawn')
        game.turn('b5', 'c7', 'knight')
        game.turn('a5', 'a4', 'pawn')
        self.assertEqual(True, game.checkmate)

if __name__ == '__main__':
    unittest.main()
