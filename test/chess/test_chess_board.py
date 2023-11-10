import unittest
from src.chess.board import increment_literal

class ChessBoardTest(unittest.TestCase):
    
    def test_util_increment_board_literal(self):
        self.assertEqual(
            'b', increment_literal('a')
        )
