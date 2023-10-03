# Simple Tic Tac Toe game made during university practice

from Classes.Game import Game as TicTacToeGame
from config import *


def __main__():
    game = TicTacToeGame()

    while game.active:
        game.rotate_turn()

        win = game.checkForWin()
        draw = game.areAllCellsOccupied()

        if win or draw:
            game.active = False
            print()
            print("="*30)

            if win:
                print("GAME OVER - " + game.turn + " HAS WON!")
            else:
                print("GAME OVER - DRAW!")

            game.display_board()
            print("="*30)


__main__()
