import pygame
from settings import *

class UI:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(None,UI_FONT_SIZE)

		self.health_bar = pygame.Rect(10,10,BAR_WIDTH,BAR_HEIGHT)


	def update_bar(self,curr,max_val,bg_rect,color):
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		width = curr/max_val * bg_rect.width
		curr_rect = bg_rect.copy()
		curr_rect.width = width
		pygame.draw.rect(self.display_surface,color,curr_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,2)
	def display(self,player):
		self.update_bar(player.health,player.max_health,self.health_bar,HEALTH_BAR_COLOR)
