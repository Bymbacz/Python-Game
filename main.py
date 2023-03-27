import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720)) # rozdzielczosc do zmiany, pozniej wypelniana z ustawien (settings.py)
        pygame.display.set_caption('Projekt Rogal') #nazwa do zmiany
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60) #to sa FPS, do ustawienia pozniej z (settings.py)
if __name__ == '__main__':
    game = Game()
    game.run()