from menu import *

def menu():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((field_sz * board_sz, field_sz * board_sz))
    pygame.display.set_caption("Лабиринты")
    bg_color = (255, 255, 255)
    screen.fill(bg_color)
    pygame.display.flip()
    Menu(screen)

menu()