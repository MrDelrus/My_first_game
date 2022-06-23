import pygame, sys
from game import *

class Button:
    def __init__(self, screen, x1, y1, width, height, color):
        x2 = x1 + width
        y2 = y1 + height
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y1), (x2, y2), (x1, y2)))
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def check_click(self, x, y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return True
        else:
            return False

class Menu:

    def __init__(self, screen):
        self.hero = 'amogus red'
        self.screen = screen
        self.font = pygame.font.SysFont('', 37)
        self.run('main_menu')


    def run(self, menu):
        while True:
            if menu == 'before_game_menu':
                menu = self.before_game_menu()
            if menu == 'main_menu':
                menu = self.main_menu()
            if menu == 'custom_hero':
                menu = self.custom_hero()
            if hasattr(menu, '__iter__') and menu[0] == 'after_game_menu':
                if menu[1] == True:
                    menu = self.main_menu()
                else:
                    menu = self.after_game_menu(menu[1])
            if hasattr(menu, '__iter__') and menu[0] == 'start_game':
                menu = self.start_game(menu[1])

    def main_menu(self):
        self.screen.fill(bg_color)
        big_font = pygame.font.SysFont('', 70)
        lbl = big_font.render('DARK LABYRINTHS', True, (0, 0, 0))
        lbl0 = self.font.render('move with W-A-S-D', True, (120, 120, 120))
        btn1 = Button(self.screen, 300, 270, 200, 50, 'green')
        lbl1 = self.font.render('START GAME', True, (0, 0, 0))
        btn2 = Button(self.screen, 300, 470, 200, 50, 'light blue')
        lbl2 = self.font.render('CUSTOM HERO', True, (0, 0, 0))
        self.screen.blit(lbl, (185, 130))
        self.screen.blit(lbl0, (290, 700))
        self.screen.blit(lbl1, (320, 282))
        self.screen.blit(lbl2, (305, 482))
        picture = pygame.image.load('./images/heroes/{0}.png'.format(self.hero))
        picture_rect = picture.get_rect(x=700, y=700)
        self.screen.blit(picture, picture_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn1.check_click(*pygame.mouse.get_pos()):
                        return 'before_game_menu'
                    elif btn2.check_click(*pygame.mouse.get_pos()):
                        return 'custom_hero'

    def custom_hero(self):
        self.screen.fill(bg_color)
        lbl = self.font.render('press esc to exit', True, (120, 120, 120))
        self.screen.blit(lbl, (290, 700))
        # grey purple blue red yellow mixed
        names = ['amogus grey', 'amogus purple', 'amogus blue', 'amogus red', 'amogus yellow', 'amogus mixed',
                 'death grey', 'death purple', 'death blue', 'death red', 'death yellow', 'death mixed',
                 'golem grey', 'golem purple', 'golem blue', 'golem red', 'golem yellow', 'golem mixed']
        buttons = [Button for x in range(len(names))]
        count = 0
        for y in range(4):
            for x in range(6):
                if count == len(names):
                    break
                buttons[count] = Button(self.screen, 100 + x * 50, 200 + y * 50, 32, 32, (100, 150, 200))
                picture = pygame.image.load('./images/heroes/{0}.png'.format(names[count]))
                picture_rect = picture.get_rect(x=100 + x * 50, y=200 + y * 50)
                self.screen.blit(picture, picture_rect)
                count += 1

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'main_menu'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(count):
                        if buttons[i].check_click(*pygame.mouse.get_pos()):
                            self.hero = names[i]
                            return 'main_menu'


    def start_game(self, size):
        game = Game(self.screen, self.hero, size)
        time = game.run()
        return ('after_game_menu', time)

    def before_game_menu(self):
        self.screen.fill('black')
        font = pygame.font.SysFont('', 37)
        btn1 = Button(self.screen, 300, 170, 200, 50, 'yellow')
        lbl1 = font.render('EASY', True, (0, 0, 0))
        btn2 = Button(self.screen, 300, 370, 200, 50, 'orange')
        lbl2 = font.render('NORMAL', True, (0, 0, 0))
        btn3 = Button(self.screen, 300, 570, 200, 50, 'red')
        lbl3 = font.render('HARD', True, (0, 0, 0))
        self.screen.blit(lbl1, (370, 182))
        self.screen.blit(lbl2, (350, 382))
        self.screen.blit(lbl3, (370, 582))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'main_menu'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn1.check_click(*pygame.mouse.get_pos()):
                        return ('start_game', 9)
                    if btn2.check_click(*pygame.mouse.get_pos()):
                        return ('start_game', 15)
                    if btn3.check_click(*pygame.mouse.get_pos()):
                        return ('start_game', 25)

    def after_game_menu(self, time):
        self.screen.fill('black')
        lbl = self.font.render('press esc to exit', True, (120, 120, 120))
        self.screen.blit(lbl, (290, 700))
        lbl = self.font.render(str(time), True, (255, 255, 255))
        self.screen.blit(lbl, (320, 300))
        lbl_text = self.font.render('Your time:', True, (255, 255, 255))
        self.screen.blit(lbl_text, (350, 250))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'main_menu'
