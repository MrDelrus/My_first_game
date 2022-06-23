import pygame
from size import *

class Person():
    def __init__(self, screen, position, name, size):
        self.screen = screen
        self.size = size
        self.position = position
        self.image = pygame.image.load('./images/heroes/{0}.png'.format(name))
        self.rectangle = self.image.get_rect()
        self.rectangle.left = field_sz * self.position[1]
        self.rectangle.top = field_sz * self.position[0]
        self.speed = 1
        self.moves = [False, False, False, False]

    def get_pos(self):
        return ((self.rectangle.top + 3) // field_sz, (self.rectangle.left + 3) / field_sz)

    def move(self, rotation):
        self.moves[rotation] = True

    def stop(self, rotation):
        self.moves[rotation] = False

    def draw(self):
        self.screen.blit(self.image, self.rectangle)

    def update(self, board):
        if self.moves[0]:
            x = self.rectangle.right - 3
            y1 = self.rectangle.top + 3
            y2 = self.rectangle.bottom - 3
            if x + 1 < field_sz * self.size and (x % field_sz != field_sz - 1 or (board[y1 // field_sz][(x + 1) // field_sz] == '+' and board[y2 // field_sz][(x + 1) // field_sz] == '+')):
                self.rectangle.right += self.speed
        if self.moves[1]:
            x1 = self.rectangle.left + 3
            x2 = self.rectangle.right - 3
            y = self.rectangle.top + 3
            if y > 0 and (y % field_sz != 0 or (board[(y - 1) // field_sz][x1 // field_sz] == '+' and board[(y - 1) // field_sz][x2 // field_sz] == '+')):
                self.rectangle.top -= self.speed
        if self.moves[2]:
            x = self.rectangle.left + 3
            y1 = self.rectangle.top + 3
            y2 = self.rectangle.bottom - 3
            if x > 0 and (x % field_sz != 0 or (board[y1 // field_sz][(x - 1) // field_sz] == '+' and board[y2 // field_sz][(x - 1) // field_sz] == '+')):
                self.rectangle.left -= self.speed
        if self.moves[3]:
            y = self.rectangle.bottom - 3
            x1 = self.rectangle.left + 3
            x2 = self.rectangle.right - 3
            if y + 1 < field_sz * self.size and (y % field_sz != field_sz - 1 or (board[(y + 1) // field_sz][x1 // field_sz] == '+' and board[(y + 1) // field_sz][x2 // field_sz] == '+')):
                self.rectangle.bottom += self.speed
        return (self.rectangle.top // field_sz, self.rectangle.left // field_sz)
