import pygame
import random  

EMPTY = (255, 255, 255)  # white
SNAKE = (0, 0, 0)  # black
FRUIT = (255, 0, 0)  # red

LINE_RECT_WIDTH = 2


class Board:
    def __init__(self, rows, width):
        self.width = width
        self.rows = rows
        self.cells = []
        for i in range(rows):
            self.cells.append([])
            for j in range(rows):
                self.cells[i].append(Cell(i, j, self.width // self.rows))

    def draw(self,screen):
        screen.fill(EMPTY)
        for i in range(self.rows):
            for j in range(self.rows):
                self.cells[i][j].draw(screen)



class Cell:
    def __init__(self, row, col, width):
        self.x = row * width
        self.y = col * width
        self.color = EMPTY
        self.width = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.y, self.x, self.width, self.width))

    def set_color(self, new_color):
        self.color = new_color