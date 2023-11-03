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
        self.assertEqual(len(board.kings()), 2)
        self.assertEqual(len(board.queens()), 2)
        self.assertEqual(len(board.rooks()), 4)
        self.assertEqual(len(board.bishops()), 4)
        self.assertEqual(len(board.knights()), 4)
        self.assertEqual(len(board.pawns()), 16)

        def count_figs(figure_set, color):
            return sum(f.color == color for f in figure_set)

        self.assertEqual(count_figs(board.kings(), chess_game.Color.WHITE), 1)
        self.assertEqual(count_figs(board.kings(), chess_game.Color.BLACK), 1)


if __name__ == '__main__':
    unittest.main()
