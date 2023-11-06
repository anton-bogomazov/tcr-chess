class ChessError(Exception):
    ...


class CheckmateError(Exception):
    def __init__(self):
        super().__init__(self, 'Checkmate! The game is over!')
        
        
class OpponentsTurnError(Exception):
    def __init__(self):
        super().__init__(self, 'it is not your turn')

class InvalidMoveError(Exception):
    def __init__(self):
        super().__init__(self, 'this move is not allowed')


class CastlingNotPossibleError(Exception):
    def __init__(self, reason):
        super().__init__(self, f'Castling is not allowed: ${reason}')
