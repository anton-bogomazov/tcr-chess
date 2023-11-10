import unittest
from src.chess.board_utils import *
from src.chess.error import InconsistentStateError


class ChessBoardTest(unittest.TestCase):
    
    def test_util_change_position_utils(self):
        self.assertEqual(('b', 1), inc_lit_pos(('a', 1)))
        self.assertEqual(('b', 1), dec_lit_pos(('c', 1)))
        self.assertEqual(('b', 4), inc_num_pos(('b', 3)))
        self.assertEqual(('b', 2), dec_num_pos(('b', 3)))

    def test_util_increment_board_literal(self):
        self.assertEqual(
            'b', increment_literal('a')
        )
        
    def test_error_with_not_board_literal(self):
        with self.assertRaises(InconsistentStateError):
            increment_literal('i')
        with self.assertRaises(InconsistentStateError):
            increment_literal('0')

    def test_util_increment_board_literal_do_nothing_if_out_of_bounds(self):
        with self.assertRaises(OutOfBoardError):
            increment_literal('h')

    def test_util_decrement_board_literal(self):
        self.assertEqual(
            'a', decrement_literal('b')
        )

    def test_util_decrement_board_literal_do_nothing_if_out_of_bounds(self):
        with self.assertRaises(OutOfBoardError):
            decrement_literal('a')

    def test_util_increment_board_numeral(self):
        self.assertEqual(
            2, increment_numeral(1)
        )

    def test_util_increment_board_numeral_do_nothing_if_out_of_bounds(self):
        with self.assertRaises(OutOfBoardError):
            increment_numeral(8)

    def test_util_decrement_board_numeral(self):
        self.assertEqual(
            2, decrement_numeral(3)
        )

    def test_util_decrement_board_numeral_do_nothing_if_out_of_bounds(self):
        with self.assertRaises(OutOfBoardError):
            decrement_numeral(1)

    def test_error_with_not_board_numeral(self):
        with self.assertRaises(InconsistentStateError):
            decrement_numeral(9)
        with self.assertRaises(InconsistentStateError):
            decrement_numeral(0)

