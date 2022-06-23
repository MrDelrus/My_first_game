import pygame, time, sys
from datetime import datetime
import controls
from labyrinth import *
from person import *

class Game:

    def __init__(self, screen, name = start_hero, size = board_sz):
        self.screen = screen
        self.size = size
        self.time = datetime.now()
        self.labyrinth = Labyrinth(self.screen, self.size - 2)
        self.board = self.labyrinth.get_board()
        self.person = Person(self.screen, (1, 0), name, self.size)
        self.fin = False

    def run(self):
        self.draw()
        self.screen.fill('black')
        pygame.display.flip()
        while True:
            controls.events(self.screen, self)
            T = controls.update(self.screen, self)
            if T is not False:
                return T
            time.sleep(0.005)

    def person_move(self, rotation):
        self.person.move(rotation)

    def person_stop(self, rotation):
        self.person.stop(rotation)

    def draw(self):
        self.labyrinth.draw(self.person.get_pos())
        self.person.draw()
        pygame.display.flip()

    def update(self):
        if self.fin:
            return True
        if self.person.update(self.board) == (self.size - 2, self.size - 1):
            T = datetime.now() - self.time
            self.labyrinth.draw([-1, -1])
            font = pygame.font.SysFont('', 37)
            lbl = font.render('press esc to exit', True, (120, 120, 120))
            self.screen.blit(lbl, (290, 700))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return T
        self.draw()
        return False

    def finish(self):
        self.fin = True