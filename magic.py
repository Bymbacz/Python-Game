import time

import pygame
from settings import *

class Magic:
	def __init__(self,an_player):
		self.an_player = an_player

	def fireball(self,player,groups,strength,speed):
		print(strength,speed)
		for i in range(1,6):
			if player.last_dir.x:
				offset_x = player.last_dir.x * i * TILESIZE * SCALE
				x = player.rect.centerx + offset_x
				y = player.rect.centery
				Particle((x,y),100,groups,strength)
			else:
				offset_y = player.last_dir.y * i * TILESIZE * SCALE
				x = player.rect.centerx
				y = player.rect.centery + offset_y
				Particle((x,y),100,groups,strength)

class Particle(pygame.sprite.Sprite):
	def __init__(self,pos,life_time,groups,damage):
		super().__init__(groups)
		self.image = pygame.transform.scale_by(pygame.image.load('Grafika/Spells/fireball.png').convert_alpha(),SCALE/32)
		self.rect = self.image.get_rect(center = pos)
		self.life_time = life_time
		self.start_time = pygame.time.get_ticks()
		self.damage = damage
	def is_alive(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.start_time >= self.life_time:
			self.kill()

	def update(self):
		self.is_alive()
