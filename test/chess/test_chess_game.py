import unittest
from src.chess.pawn import Pawn
from src.chess.rook import Rook
from src.chess.queen import Queen
from src.chess.bishop import Bishop
from src.chess.knight import Knight
from src.chess.king import King
from src.chess.game import standard_chess_game
from src.chess.board import ChessBoard
from src.chess.error import *
from src.chess.color import Color


class ChessGameTest(unittest.TestCase):
    def test_from_to_positions_and_figure_type_is_enough_to_make_turn(self):
        standard_chess_game().turn('b1', 'c3')

    def test_fail_to_make_turn_if_every_arg_is_not_provided(self):
        with self.assertRaises(TypeError):
            standard_chess_game().turn('f3')
        with self.assertRaises(TypeError):
            standard_chess_game().turn('f3')
        with self.assertRaises(TypeError):
            standard_chess_game().turn()

    def test_game_has_chess_board(self):
        result = standard_chess_game().get_board()
        self.assertIsInstance(result, ChessBoard)

    def test_initially_board_has_standard_figure_set(self):
        board = standard_chess_game().get_board()

        def count_figs(figure_set, color):
            return sum(f.color == color for f in figure_set)

        def whites_eq_blacks(figure_set, n):
            self.assertEqual(count_figs(figure_set, Color.WHITE), n)
            self.assertEqual(count_figs(figure_set, Color.BLACK), n)

        whites_eq_blacks(board.search_board(King), 1)
        whites_eq_blacks(board.search_board(Queen), 1)
        whites_eq_blacks(board.search_board(Knight), 2)
        whites_eq_blacks(board.search_board(Bishop), 2)
        whites_eq_blacks(board.search_board(Rook), 2)
        whites_eq_blacks(board.search_board(Pawn), 8)

    def test_figures_initially_placed_at_standard_cells(self):
        board = standard_chess_game().get_board()
        def check_if_positioned_well(fig_row, pawn_row, color):
            for literal in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
                self.assertEqual(board.cell(literal, pawn_row), Pawn((literal, pawn_row), color))
            self.assertEqual(board.cell('a', fig_row), Rook(('a', fig_row), color))
            self.assertEqual(board.cell('b', fig_row), Knight(('b', fig_row), color))
            self.assertEqual(board.cell('c', fig_row), Bishop(('c', fig_row), color))
            self.assertEqual(board.cell('d', fig_row), Queen(('d', fig_row), color))
            self.assertEqual(board.cell('e', fig_row), King(('e', fig_row), color))
            self.assertEqual(board.cell('f', fig_row), Bishop(('f', fig_row), color))
            self.assertEqual(board.cell('g', fig_row), Knight(('g', fig_row), color))
            self.assertEqual(board.cell('h', fig_row), Rook(('h', fig_row), color))

        check_if_positioned_well(1, 2, Color.WHITE)
        check_if_positioned_well(8, 7, Color.BLACK)

    def test_figure_can_be_moved_to_empty_cell(self):
        board = standard_chess_game().get_board()
        self.assertEqual(board.cell('b', 1), Knight(('b', 1), Color.WHITE))
        board.move(('b', 1), ('c', 3))
        self.assertEqual(board.cell('c', 3), Knight(('c', 3), Color.WHITE))
        self.assertEqual(board.cell('b', 1), None)

    def test_figure_can_take_opponents_figure(self):
        board = standard_chess_game().get_board()
        board.move(('b', 1), ('c', 3))
        board.move(('c', 3), ('d', 5))

        self.assertIsInstance(board.cell('c', 7), Pawn)
        self.assertEqual(board.cell('c', 7).color, Color.BLACK)
        board.move(('d', 5), ('c', 7))
        self.assertIsInstance(board.cell('c', 7), Knight)
        self.assertEqual(len(board.search_board(Pawn)), 15)

    def test_whites_starts(self):
        self.assertEquals(
            standard_chess_game().current_player,
            Color.WHITE
        )
        
    def test_pass_turn(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        self.assertEquals(
            game.current_player,
            Color.BLACK
        )

    def test_cant_move_white_piece_in_the_blacks_turn(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        with self.assertRaises(OpponentsTurnError):
            game.turn('g1', 'f3')

    def test_check_condition(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        game.turn('a7', 'a6')
        game.turn('c3', 'b5')
        game.turn('a6', 'a5')
        game.turn('b5', 'c7')
        self.assertEqual(Color.BLACK, game.checked_player)

    def test_checkmate_condition(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        game.turn('a7', 'a6')
        game.turn('c3', 'b5')
        game.turn('a6', 'a5')
        game.turn('b5', 'c7')
        with self.assertRaises(CheckmateError):
            game.turn('a5', 'a4')
        self.assertEqual(True, game.checkmate)

    def test_king_can_be_checked(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        game.turn('a7', 'a6')
        game.turn('c3', 'b5')
        game.turn('a6', 'a5')
        self.assertEqual(game.get_board().checked(Color.BLACK), False)
        game.turn('b5', 'c7')
        self.assertEqual(game.get_board().checked(Color.BLACK), True)

    def test_taking_attacking_figure_resets_check(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        game.turn('a7', 'a6')
        game.turn('c3', 'b5')
        game.turn('a6', 'a5')
        game.turn('b5', 'c7')
        self.assertEqual(game.get_board().checked(Color.BLACK), True)
        self.assertEqual(game.checked_player, Color.BLACK)
        game.turn('d8', 'c7')
        self.assertEqual(game.get_board().checked(Color.BLACK), False)
        self.assertEqual(game.checked_player, None)

    def test_turn_is_not_possible_when_checkmate(self):
        game = standard_chess_game()
        game.checkmate = True
        
        with self.assertRaises(CheckmateError):
            game.turn('b1', 'c3')

    def test_is_castling_move(self):
        board = standard_chess_game().get_board()
        self.assertEqual(True, board.is_castling_move(('e', 1), ('g', 1)))
        self.assertEqual(True, board.is_castling_move(('e', 8), ('c', 8)))

    def test_castling_move_impossible_when_blocked_by_figures(self):
        board = standard_chess_game().get_board()
        with self.assertRaises(CastlingNotPossibleError):
            board.move(('e', 1), ('g', 1))
        with self.assertRaises(CastlingNotPossibleError):
            board.move(('e', 1), ('c', 1))

    def test_castling_move_impossible_when_king_touched(self):
        king = King(('e', 1), Color.WHITE)
        king.touched = True
        board = ChessBoard((king, Rook(('h', 1), Color.WHITE)))

        with self.assertRaises(CastlingNotPossibleError):
            board.move(('e', 1), ('g', 1))

    def test_castling_move_impossible_when_rook_touched(self):
        rook = Rook(('h', 1), Color.WHITE)
        rook.touched = True
        board = ChessBoard((King(('e', 1), Color.WHITE), rook))

        with self.assertRaises(CastlingNotPossibleError):
            board.move(('e', 1), ('g', 1))

    def test_castling_move_impossible_when_rook_moved(self):
        board = ChessBoard([King(('e', 1), Color.WHITE)])
        with self.assertRaises(CastlingNotPossibleError):
            board.move(('e', 1), ('g', 1))

    def test_perform_castling_move(self):
        game = standard_chess_game()
        game.turn('g1', 'f3')
        game.turn('a7', 'a6')
        game.turn('g2', 'g3')
        game.turn('a6', 'a5')
        game.turn('f1', 'h3')
        game.turn('a5', 'a4')
        game.turn('e1', 'g1')
        self.assertEqual(None, game.get_board().cell('e', 1))
        self.assertEqual(None, game.get_board().cell('h', 1))
        self.assertIsInstance(game.get_board().cell('f', 1), Rook)
        self.assertIsInstance(game.get_board().cell('g', 1), King)

    @unittest.skip
    def test_rook_can_be_blocked_by_opponents_figures(self):
        sut = Rook(('d', 6), Color.WHITE)
        figures = [
            King(('d', 5), Color.WHITE),
            Pawn(('e', 6), Color.BLACK),
            Pawn(('b', 6), Color.WHITE),
            Pawn(('a', 6), Color.BLACK),
            sut
        ]
        self.assertEqual({('d', 8), ('d', 7), ('c', 6), ('e', 6)}, sut.possible_moves(figures))
        self.assertEqual(Pawn(('b', 6), Color.WHITE), sut.closest_left(figures))
        self.assertEqual(Pawn(('e', 6), Color.BLACK), sut.closest_right(figures))
        self.assertEqual(King(('d', 5), Color.WHITE), sut.closest_bottom(figures))
        self.assertEqual(None, sut.closest_top(figures))

    def test_rook_can_be_blocked_by_friendly_figures_no_turns(self):
        game = standard_chess_game()
        bottom_right_rook = game.get_board().cell('a', 1)
        self.assertEqual(set(), bottom_right_rook.possible_moves(game.get_board().figures))


if __name__ == '__main__':
    unittest.main()
