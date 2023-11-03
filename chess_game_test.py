import unittest
import chess_game


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
        self.assertEqual(len(result.board), 8)
        self.assertEqual(len(result.board[0]), 8)

    def test_initially_board_has_standard_figure_set(self):
        board = chess_game.ChessGame().get_board()

        def count_figs(figure_set, color):
            return sum(f.color == color for f in figure_set)

        def whites_eq_blacks(figure_set, n):
            self.assertEqual(count_figs(figure_set, chess_game.Color.WHITE), n)
            self.assertEqual(count_figs(figure_set, chess_game.Color.BLACK), n)

        whites_eq_blacks(board.kings(), 1)
        whites_eq_blacks(board.queens(), 1)
        whites_eq_blacks(board.knights(), 2)
        whites_eq_blacks(board.bishops(), 2)
        whites_eq_blacks(board.rooks(), 2)
        whites_eq_blacks(board.pawns(), 8)


if __name__ == '__main__':
    unittest.main()
