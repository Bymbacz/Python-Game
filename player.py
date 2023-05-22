#rysuje gracza, odpowiada za jego ruch, interakcje, itd...
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites,create_magic,usable_objects):
		super().__init__(groups)
		self.image = pygame.transform.scale_by(pygame.image.load('Grafika/Player/0.png').convert_alpha(),SCALE)
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2()
		self.last_dir = pygame.math.Vector2(1,0)

		self.speed = 8
		self.health = 100
		self.max_health = 100

		self.obstacle_sprites = obstacle_sprites

		self.create_magic = create_magic
		self.usable_objects = usable_objects
		self.attacking = False
		self.magic_index = 0
		self.magic = list(magic_data.keys())[self.magic_index]

		self.can_be_damaged = True
		self.hit_time = None
		self.invincibility_time = 1000

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			if keys[pygame.K_UP]:
				self.direction.y = -1
			elif keys[pygame.K_DOWN]:
				self.direction.y = 1
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT]:
				self.direction.x = 1
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
			else:
				self.direction.x = 0

			if self.direction.x != 0 or self.direction.y != 0:
				self.last_dir = self.direction

			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_timer = pygame.time.get_ticks()
				style = list(magic_data.keys())[self.magic_index]
				strength = list(magic_data.values())[self.magic_index]['strength']
				speed = list(magic_data.values())[self.magic_index]['speed']
				self.create_magic(style, strength, speed)

			if keys[pygame.K_e]:
				print('Wciśnięto e')
				self.usable_objects()

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed
		self.collision('horizontal')
		self.rect.y += self.direction.y * speed
		self.collision('vertical')

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0:  # moving right
						self.rect.right = sprite.rect.left
					if self.direction.x < 0:  # moving left
						self.rect.left = sprite.rect.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0:  # moving down
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0:  # moving up
						self.rect.top = sprite.rect.bottom

	def cooldown(self):
		curr_time = pygame.time.get_ticks()
		if curr_time - self.attack_timer > list(magic_data.values())[self.magic_index]['cooldown']:
			self.attacking = False
			#self.destroy_magic()
		if not self.can_be_damaged:
			if curr_time - self.hit_time >= self.invincibility_time:
				self.can_be_damaged = True

	def update(self):
		self.input()
		self.cooldown()
		self.move(self.speed)