import unittest
from src.chess.figures.bishop import Bishop
from src.chess.figures.color import Color


class BishopTest(unittest.TestCase):
    
    def test_bishop_possible_turns(self):
        bishop = _bishop()
        
        self.assertEqual(bishop.turns([]), {
            ('a', 1), ('b', 2), ('d', 2), ('e', 1), ('f', 6),
            ('a', 5), ('b', 4), ('d', 4), ('e', 5), ('g', 7), ('h', 8),
        })
        

def _bishop(position=('c', 3), color=Color.WHITE):
    return Bishop(position, color)
