class ChessError(Exception):
    ...


class CheckmateError(Exception):
    def __init__(self):
        super().__init__(self, 'Checkmate! The game is over!')
        
        
class OpponentsTurnError(Exception):
    def __init__(self):
        super().__init__(self, 'it is not your turn')
