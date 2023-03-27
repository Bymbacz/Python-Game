import pygame, sys

from Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (1280, 720))  # rozdzielczosc do zmiany, pozniej wypelniana z ustawien (settings.py)
        pygame.display.set_caption('Projekt Rogal')  # nazwa do zmiany
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.menu.give_board_size(1280, 720)  # screen params
        self.menu.set_positions(self.screen)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.menu.run()

            pygame.display.update()
            self.clock.tick(60)  # to sa FPS, do ustawienia pozniej z (settings.py)


if __name__ == '__main__':
    game = Game()
    game.run()
