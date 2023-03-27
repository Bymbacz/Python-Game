import math
from enum import Enum
import pygame


class Menu:
    def __init__(self):
        pygame.init()

        self.action: Action = Action.NOTHING
        self.positions_were_set = False
        self.x_board_size: int  # needs setter
        self.y_board_size: int  # needs setter
        self.i=0
        self.keys=None

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
        speed_down_font = pygame.font.Font(None, font_size)
        speed_up_font = pygame.font.Font(None, font_size)

        menu_surface = pygame.Surface((width, height))
        menu_surface.fill("White")
        self.menu_surface = menu_surface

        start_surface = start_font.render("Start <- Press space", False, "Green")
        exit_surface = exit_font.render("Exit This App <- Press esc", False, "Green")
        slow_surface = speed_down_font.render("Make Game Slower <- Press pgup", False, "Green")
        fast_surface = speed_up_font.render("Make Game Faster <- Press pgdn", False, "Green")

        menu_surface.blit(start_surface, (0, 0))
        menu_surface.blit(exit_surface, (0, self.resize_y(0.1)))
        menu_surface.blit(slow_surface, (0, self.resize_y(0.2)))
        menu_surface.blit(fast_surface, (0, self.resize_y(0.3)))
        screen.blit(menu_surface, (self.resize_x(0.3), self.resize_y(0.3)))  # needs arg: screen

    def run(self):
        if self.positions_were_set:
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_SPACE]:
                self.action = Action.START  # ew pozniej dodac jak to dziala
                # self.i+=1
            elif self.keys[pygame.K_ESCAPE]:
                # self.i+=1
                self.action = Action.EXIT
            elif self.keys[pygame.K_PAGEUP]:
                # self.i+=1
                self.action = Action.SPEED_FAST  # ew pozniej dodac jak to dziala
            elif self.keys[pygame.K_PAGEDOWN]:
                # self.i+=1
                self.action = Action.SPEED_SLOW  # ew pozniej dodac jak to dziala
            else:
                pass
                # print(self.i)
            # ew pozniej dodac inne

            match self.action:
                case Action.START:
                    action = Action.NOTHING
                    # todo
                    pass
                case Action.EXIT:
                    print("Hello")
                    action = Action.NOTHING
                    pygame.quit()
                    exit(0)
                case Action.SPEED_FAST:
                    action = Action.NOTHING
                    # todo
                    pass
                case Action.SPEED_SLOW:
                    action = Action.NOTHING
                    # todo
                    pass


class Action(Enum):
    NOTHING = -1
    START = 0
    EXIT = 1
    SPEED_SLOW = 2
    SPEED_FAST = 3
