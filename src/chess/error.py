class ChessError(Exception):
    ...


class CheckmateError(Exception):
    def __init__(self):
        super().__init__(self, 'Checkmate! The game is over!')
        
        
class OpponentsTurnError(Exception):
    def __init__(self):
        super().__init__(self, 'it is not your turn')


class InvalidMoveError(Exception):
    def __init__(self, reason=''):
        super().__init__(self, f'this move is not allowed {reason}')


class CastlingNotPossibleError(Exception):
    def __init__(self, reason):
        super().__init__(self, f'Castling is not allowed: ${reason}')


class InconsistentStateError(Exception):
    def __init__(self, reason):
        super().__init__(self, f'State is broken: ${reason}')
        

class OutOfBoardError(Exception):
    def __init__(self):
        super().__init__(self, 'Position is out of the board')


class UnsafeTurnError(Exception):
    def __init__(self):
        super().__init__(self, 'That turn is putting your king under attack')
