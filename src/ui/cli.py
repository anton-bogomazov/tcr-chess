import os


class Cli:
    def __init__(self, chess_game):
        self.game = chess_game
    
    def start(self):
        while True:
            self.print_board()
            turn = input('> ')
            self.game.turn(*turn.split())
            os.system('clear')
        
    def print_board(self):
        print("      a     b     c     d     e     f     g     h")
        print("   " + "+-----" * 8 + "+")
        for i, row in enumerate(self.game.get_board().to_string()):
            print(8 - i, end="  ")
            print("|", end="  ")
            for cell in row:
                if cell == ' ':
                    print(' ', end='')
                print(cell, end=" |  ")
            print(8 - i, end="")
            print("\n   " + "+-----" * 8 + "+")
        print("      a     b     c     d     e     f     g     h")