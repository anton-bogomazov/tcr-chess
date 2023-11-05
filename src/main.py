from chess.game import standard_chess_game
import os


def main():
    game = standard_chess_game()
    while True:
        print_board(game.get_board().to_string())
        turn = input('> ')
        game.turn(*turn.split())
        os.system('clear')
    

def print_board(board):
    print("      a     b     c     d     e     f     g     h")
    print("   " + "+-----" * 8 + "+")
    for i, row in enumerate(board):
        print(8 - i, end="  ")
        print("|", end="  ")
        for cell in row:
            if cell == ' ':
                print(' ', end='')
            print(cell, end=" |  ")
        print(8 - i, end="")
        print("\n   " + "+-----" * 8 + "+")
    print("      a     b     c     d     e     f     g     h")
    

if __name__ == '__main__':
    main()
    