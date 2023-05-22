import pygame
from settings import *
class Enemies(pygame.sprite.Sprite):
	def __init__(self,name,pos,groups,obstacle_sprites,damage_player):
		super().__init__(groups)
		self.image = pygame.transform.scale_by(pygame.image.load('Grafika/Enemies/2.png').convert_alpha(),SCALE)
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2()

		self.sprite_type = 'enemy'
		self.obstacle_sprites = obstacle_sprites

		self.name = name
		monster_info = monster_data[self.name]
		self.health = monster_info['health']
		self.speed = monster_info['speed']
		self.damage = monster_info['strength']
		self.notice_radius = monster_info['notice_radius']
		self.attack_radius = 10
		self.status = 'idle'

		self.can_attack = True
		self.attack_time = None
		self.attack_cooldown = 1000
		self.damage_player = damage_player

		self.can_be_damaged = True
		self.hit_time = None
		self.invincibility_time = 500

	def actions(self, player):
		if self.status == 'attack':
			self.attack_time = pygame.time.get_ticks()
			self.damage_player(self.damage)
		elif self.status == 'move':
			self.direction = self.get_player_distance_direction(player)[1]
		else:
			self.direction = pygame.math.Vector2()

	def cooldown(self):
		current_time = pygame.time.get_ticks()
		if not self.can_attack:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.can_attack = True
		if not self.can_be_damaged:
			if current_time - self.hit_time >= self.invincibility_time:
				self.can_be_damaged = True

	def get_status(self, player):
		distance = self.get_player_distance_direction(player)[0]
		if distance <= self.attack_radius and self.can_attack:
			if self.status != 'attack':
				self.frame_index = 0
			self.status = 'attack'
		elif distance <= self.notice_radius:
			self.status = 'move'
		else:
			self.status = 'idle'

	def get_player_distance_direction(self,player):
		enemy_vec = pygame.math.Vector2(self.rect.center)
		player_vec = pygame.math.Vector2(player.rect.center)
		distance = (player_vec - enemy_vec).magnitude()

		if distance > 0:
			direction = (player_vec - enemy_vec).normalize()
		else:
			direction = pygame.math.Vector2()

		return (distance,direction)
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
	def update(self):
		self.move(self.speed)
		self.cooldown()

	def enemy_update(self,player):
		self.get_status(player)
		self.actions(player)