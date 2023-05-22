import pygame, sys
from settings import *
from menu import Menu
from level import Level
from end_screen import End


class Game:
    def __init__(self):
        self.menu_is_present = True
        pygame.init()
        self.resolution = (WIDTH, HEIGHT)  # rozdzielczosc do zmiany, pozniej wypelniana z ustawien (settings.py)
        self.screen = pygame.display.set_mode(self.resolution, MODE_TYPES[2])
        pygame.display.set_caption('Projekt Rogal')  # nazwa do zmiany
        self.clock = pygame.time.Clock()
        self.end=End(self)
        self.menu = Menu()
        self.menu.give_board_size(*self.resolution)  # screen params
        self.menu.set_positions(self.screen)
        self.level=Level(self)

    def hide_menu(self):
        self.menu_is_present = False

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.menu_is_present:
                self.menu.run(self)
            elif self.level.is_running:
                self.screen.fill('black')
                self.level.run()
            else:
                font_size = 40
                start_font = pygame.font.Font(None, font_size)

                if self.level.win:
                    start_surface = start_font.render("The End!!!", False, MENU_FONT_SIZE)
                    self.screen.fill((94, 129, 162))
                else:
                    start_surface = start_font.render("YOU'R DEAD", False, MENU_FONT_SIZE)
                    self.screen.fill('black')

                score_message_rect = start_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                self.screen.blit(start_surface, score_message_rect)
                keys = pygame.key.get_pressed()
                if keys [pygame.K_SPACE]:
                    exit()
            pygame.display.update()
            self.clock.tick(FPS)  # to sa FPS, do ustawienia pozniej z (settings.py)


if __name__ == '__main__':
    game = Game()
    game.run()
