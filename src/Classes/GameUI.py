import pygame
from pygame.draw import rect
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill(color=(255, 255, 255))
pygame.display.set_caption("TicTacToe")

lineThickness = 3
lineColor = pygame.Color(200, 200, 200)
cellsPerLine = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x, y = screen.get_size()

    # draw the lines for the tic tac toe board
    for i in range(1, cellsPerLine):
        xPos, yPos = x * (0.33 * i), y * (0.33 * i)
        rect(screen, lineColor, pygame.Rect(xPos, 0, lineThickness, y))
        rect(screen, lineColor, pygame.Rect(0, yPos, x, lineThickness))

    pygame.display.update()
