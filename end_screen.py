import math
from enum import Enum
import pygame
from settings import *

class End:
    def __init__(self,engine):
        pygame.init()
        self.engine = engine

        self.action: Action = Action.NOTHING
        self.positions_were_set = False
        self.x_board_size: int  # needs setter
        self.y_board_size: int  # needs setter
        self.i = 0
        self.j = 0

        self.keys = None

    def give_board_size(self, x, y):
        self.x_board_size = x
        self.y_board_size = y

    def resize_x(self, scale):
        return math.floor(self.x_board_size * scale)

    def resize_y(self, scale):
        return math.floor(self.y_board_size * scale)

    def set_positions(self, screen):
        self.positions_were_set = True
        screen.fill((94, 129, 162))

        font_size = 40
        start_font = pygame.font.Font(None, font_size)
        exit_font = pygame.font.Font(None, font_size)

        start_surface = start_font.render("GRATULACJE --> Ukonczyles gre!!!", False, MENU_FONT_SIZE)

        #score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = start_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(start_surface, score_message_rect)
    def hide(self):
        pass


    def run(self):
        if self.positions_were_set:
            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_SPACE]:
                self.action = Action.START
            else:
                pass

            match self.action:
                case Action.START:
                    self.hide()
            action = Action.NOTHING


class Action(Enum):
    NOTHING = -1
    START = 0