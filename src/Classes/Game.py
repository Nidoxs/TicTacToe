from config import *
import sys
sys.path.append("../src")


class Game:
    winningLines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self) -> None:
        self.active = True
        self.board = DEFAULT_BOARD

    def isActive(self):
        return self.active

    def resetBoard(self):
        self.board = DEFAULT_BOARD

    def areAllCellsOccupied(self):
        for cell in self.board:
            if cell != EMPTY_SLOT_CHAR:
                return False

        return True

    def hasPlayerWon(self, player):
        board = self.board

        for combo in self.winningLines:
            a, b, c = board[combo[0]], board[combo[1]], board[combo[2]]

            if a == player and b == player and c == player:
                return True

    def rotate_turn(self):
        self.turn = PLAYERS[0] if self.turn == PLAYERS[1] else PLAYERS[1]

        validMove = None

        while validMove == None:
            cell = input(INPUT_STRING.format(turn=self.turn))

            if cell != "":
                cell = int(cell) - 1

                withinRange = (cell >= 0 and cell <= 8)
                cellIsFree = self.board[cell] == EMPTY_SLOT_CHAR

                if withinRange and cellIsFree:
                    validMove = cell

        self.board[cell] = self.turn
