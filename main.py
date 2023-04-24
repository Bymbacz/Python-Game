import pygame, sys
from settings import *
from menu import Menu
from map import Map
from level import Level


class Game:
    def __init__(self):
        self.menu_is_present = True
        pygame.init()
        self.resolution = (WIDTH, HEIGHT)  # rozdzielczosc do zmiany, pozniej wypelniana z ustawien (settings.py)
        self.screen = pygame.display.set_mode(self.resolution, MODE_TYPES[2])
        pygame.display.set_caption('Projekt Rogal')  # nazwa do zmiany
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.menu.give_board_size(*self.resolution)  # screen params
        self.menu.set_positions(self.screen)
        self.level=Level()

    def hide_menu(self):
        self.menu_is_present = False

    #def show_map(self):
        #self.map = Map(self.screen, self.resolution[0], self.resolution[1])

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.menu_is_present:
                self.menu.run(self)
            else:
                self.screen.fill('black')
                self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)  # to sa FPS, do ustawienia pozniej z (settings.py)


if __name__ == '__main__':
    game = Game()
    game.run()
