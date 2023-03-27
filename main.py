import pygame, sys

from Menu import Menu
from Map import Map


class Game:
    def __init__(self):
        self.menu_is_present = True
        pygame.init()
        self.resolution = (1280, 720)  # rozdzielczosc do zmiany, pozniej wypelniana z ustawien (settings.py)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Projekt Rogal')  # nazwa do zmiany
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.menu.give_board_size(self.resolution[0], self.resolution[1])  # screen params
        self.menu.set_positions(self.screen)

    def hide_menu(self):
        self.menu_is_present = False

    def show_map(self):
        self.map = Map(self.screen, self.resolution[0], self.resolution[1])

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.menu_is_present:
                self.menu.run(self)

            pygame.display.update()
            self.clock.tick(60)  # to sa FPS, do ustawienia pozniej z (settings.py)


if __name__ == '__main__':
    game = Game()
    game.run()
