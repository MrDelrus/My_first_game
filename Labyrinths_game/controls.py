import time
import pygame, sys

def events(screen, game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.finish()
            if event.key == pygame.K_d:
                game.person_move(0)
            elif event.key == pygame.K_w:
                game.person_move(1)
            elif event.key == pygame.K_a:
                game.person_move(2)
            elif event.key == pygame.K_s:
                game.person_move(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                game.person_stop(0)
            if event.key == pygame.K_w:
                game.person_stop(1)
            if event.key == pygame.K_a:
                game.person_stop(2)
            if event.key == pygame.K_s:
                game.person_stop(3)

def update(screen, game):
    screen.fill('black')
    time = game.update()
    if time is not False:
        return time
    pygame.display.flip()
    return False
