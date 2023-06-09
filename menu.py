import math
from enum import Enum
import pygame
from settings import *

class Menu:
    def __init__(self):
        pygame.init()

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

        width = self.resize_x(0.4)  # change
        height = self.resize_y(0.4)  # change

        font_size = 40
        start_font = pygame.font.Font(None, font_size)
        exit_font = pygame.font.Font(None, font_size)

        menu_surface = pygame.Surface((width, height))
        menu_surface.fill(MENU_BACKGROUND)
        self.menu_surface = menu_surface

        start_surface = start_font.render("Start <- Press space", False, MENU_FONT_SIZE)
        exit_surface = exit_font.render("Exit This App <- Press esc", False, MENU_FONT_SIZE)

        menu_surface.blit(start_surface, (0, 0))
        menu_surface.blit(exit_surface, (0, self.resize_y(0.1)))
        screen.blit(menu_surface, (self.resize_x(0.3), self.resize_y(0.3)))  # needs arg: screen

    def hide(self):
        pass


    def run(self,engine):
        if self.positions_were_set:
            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_SPACE]:
                self.action = Action.START
            elif self.keys[pygame.K_ESCAPE]:
                self.action = Action.EXIT
            else:
                pass

            match self.action:
                case Action.START:
                    self.hide()
                    engine.hide_menu()
                    pass
                case Action.EXIT:
                    pygame.quit()
                    exit(0)
            action = Action.NOTHING


class Action(Enum):
    NOTHING = -1
    START = 0
    EXIT = 1
