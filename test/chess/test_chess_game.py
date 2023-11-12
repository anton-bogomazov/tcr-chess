import unittest
from src.chess.figures.pawn import Pawn
from src.chess.figures.rook import Rook
from src.chess.figures.queen import Queen
from src.chess.figures.bishop import Bishop
from src.chess.figures.knight import Knight
from src.chess.figures.king import King
from src.chess.game import standard_chess_game
from src.chess.board import ChessBoard
from src.chess.error import *
from src.chess.figures.color import Color


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
        self.assertTrue(game.get_board().checked(Color.BLACK))

    def test_checkmate_condition(self):
        game = standard_chess_game()
        game.turn('b1', 'c3')
        game.turn('a7', 'a6')
        game.turn('c3', 'b5')
        game.turn('a6', 'a5')
        game.turn('b5', 'c7')
        with self.assertRaises(CheckmateError):
            game.turn('a5', 'a4')

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
        game.turn('d8', 'c7')
        self.assertEqual(game.get_board().checked(Color.BLACK), False)

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

    def test_rook_can_be_blocked_by_opponents_figures(self):
        sut = Rook(('d', 6), Color.WHITE)
        figures = [
            King(('d', 5), Color.WHITE),
            Pawn(('e', 6), Color.BLACK),
            Pawn(('b', 6), Color.WHITE),
            Pawn(('a', 6), Color.BLACK),
            sut
        ]
        self.assertEqual({('d', 8), ('d', 7), ('c', 6), ('e', 6)}, sut.turns(figures))

    def test_rook_can_be_blocked_by_friendly_figures_no_turns(self):
        game = standard_chess_game()
        bottom_right_rook = game.get_board().cell('a', 1)
        self.assertEqual(set(), bottom_right_rook.turns(game.get_board().figures))

    def test_transform_pawn(self):
        pawn = Pawn(('a', 7), Color.WHITE)
        board = ChessBoard([pawn, King(('a', 1), Color.WHITE)])
        
        board.move(('a', 7), ('a', 8))
        
        self.assertFalse(pawn in board.figures)
        self.assertEqual(board.cell(*('a', 8)), Queen(('a', 8), Color.WHITE))

    def test_only_pawn_is_transformable(self):
        queen = Queen(('a', 7), Color.WHITE)
        board = ChessBoard([queen, King(('a', 1), Color.WHITE)])

        board.move(('a', 7), ('a', 8))

        self.assertTrue(queen in board.figures)
        self.assertEqual(board.cell(*('a', 8)), Queen(('a', 8), Color.WHITE))

    def test_cant_move_to_attacked_cell(self):
        king = King(('c', 3), color=Color.BLACK)
        figs = [
            king,
            King(('c', 5), color=Color.WHITE),
            King(('d', 1), color=Color.WHITE),
        ]
        board = ChessBoard(figs)
        
        with self.assertRaises(UnsafeTurnError):
            board.move(('c', 3), ('c', 4))

    def test_it_is_not_allowed_to_open_ally_king_for_attack(self):
        game = standard_chess_game()
        game.turn('e2', 'e4')
        game.turn('e7', 'e5')
        game.turn('f1', 'b5')

        with self.assertRaises(UnsafeTurnError):
            game.turn('d7', 'd6')

    def test_player_doesnt_pass_turn_when_unsafe_or_invalid(self):
        game = standard_chess_game()
        self.assertEqual(Color.WHITE, game.current_player)
        game.turn('e2', 'e4')
        self.assertEqual(Color.BLACK, game.current_player)
        game.turn('e7', 'e5')
        self.assertEqual(Color.WHITE, game.current_player)
        game.turn('f1', 'b5')
        self.assertEqual(Color.BLACK, game.current_player)
        with self.assertRaises(InvalidMoveError):
            game.turn('a8', 'a5')
        self.assertEqual(Color.BLACK, game.current_player)
        with self.assertRaises(UnsafeTurnError):
            game.turn('d7', 'd6')
        self.assertEqual(Color.BLACK, game.current_player)
