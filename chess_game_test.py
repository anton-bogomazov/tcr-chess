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

    def test_pawn_possible_turns(self):
        pawn = chess_game.Pawn(('a', 2), chess_game.Color.WHITE)
        self.assertEqual(len(pawn.turns()), 2)

    def test_pawn_possible_turns_only_short_turn_after_touch(self):
        pawn = chess_game.Pawn(('a', 2), chess_game.Color.WHITE)
        pawn.move(('a', 3))
        self.assertEqual(len(pawn.turns()), 1)

    def test_pawn_move(self):
        pawn = chess_game.Pawn(('a', 2), chess_game.Color.WHITE)
        pawn.move(('a', 3))
        self.assertEqual(pawn.position, ('a', 3))

    def test_pawn_invlid_move(self):
        pawn = chess_game.Pawn(('a', 2), chess_game.Color.WHITE)
        pawn.move(('b', 3))
        self.assertEqual(pawn.position, ('a', 2))

    def test_knight_possible_turns(self):
        knight = chess_game.Knight(('c', 3), chess_game.Color.WHITE)
        self.assertEqual(len(knight.turns()), 8)
        self.assertEqual(knight.turns(), {
            ('b', 1), ('d', 1), ('b', 5), ('d', 5),
            ('a', 2), ('a', 4), ('e', 2), ('e', 4),
        })

    def test_knight_possible_turns_less_moves_on_the_boards_edge(self):
        knight = chess_game.Knight(('a', 3), chess_game.Color.WHITE)
        self.assertEqual(len(knight.turns()), 4)

    def test_knight_possible_turns_least_possible_turns_in_the_corner(self):
        knight = chess_game.Knight(('a', 8), chess_game.Color.WHITE)
        self.assertEqual(len(knight.turns()), 2)

    def test_bishop_possible_turns(self):
        bishop = chess_game.Bishop(('c', 3), chess_game.Color.WHITE)
        self.assertEqual(len(bishop.turns()), 11)
        self.assertEqual(bishop.turns(), {
            ('a', 1), ('b', 2), ('d', 2), ('e', 1), ('f', 6),
            ('a', 5), ('b', 4), ('d', 4), ('e', 5), ('g', 7), ('h', 8),
        })

    def test_rook_possible_turns(self):
        rook = chess_game.Rook(('c', 3), chess_game.Color.WHITE)
        self.assertEqual(len(rook.turns()), 14)

if __name__ == '__main__':
    unittest.main()
