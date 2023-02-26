import random
import pygame
from board import Board
from snake import Snake
from time import sleep

WIDTH = 800
ROWS = 50
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("snake")



def main():
    game_board = Board(ROWS, WIDTH)
    run = True

    while run:
        game_board.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE
                    


    pygame.quit()


main()