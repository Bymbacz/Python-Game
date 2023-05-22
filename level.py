#Odpowiada za wyswietlanie mapy, gracza i obiektow, przekazuje to wszystko do maina
import pygame
from settings import *
from player import Player
from tile import Tile
from enemies import Enemies
from magic import Magic
from random import choice
from ui import UI

class Level:
    def __init__(self,engine):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.to_attack_sprites = pygame.sprite.Group()
        self.usable_sprites = pygame.sprite.Group()
        self.create_map()
        self.ui = UI()
        self.magic = Magic(self.player)
        self.is_running = True
        self.engine = engine
        self.win = False
    def create_map(self):
        layouts = {
            'STOP': import_csv_layout('Maps/mapa_STOP.csv'),
            'Player': import_csv_layout('Maps/mapa_Player.csv'),
            'Enemies': import_csv_layout('Maps/mapa_Enemies.csv'),
            'Door': import_csv_layout('Maps/mapa_Door.csv'),
            'Chests': import_csv_layout('Maps/mapa_chests.csv'),
        }
        graphics = {
            'Enemies': import_folder('Grafika/Enemies'),
            'Door': import_folder('Grafika/Door'),
            'Chests': import_folder('Grafika/Chests'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE*SCALE
                        y = row_index * TILESIZE*SCALE
                        if style == 'STOP':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'Enemies':
                            Enemies('slime',(x, y), [self.visible_sprites,self.to_attack_sprites], self.obstacle_sprites,self.damage_logic)
                        if style == 'Door':
                            if col == '0':
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'door', graphics['Door'][3])
                            if col == '2':
                                Tile((x, y), [self.visible_sprites, self.usable_sprites], 'door', graphics['Door'][0])
                            else:
                                Tile((x, y), [self.usable_sprites], 'door', graphics['Door'][2])
                        if style == 'Chests':
                            Tile((x, y), [self.visible_sprites, self.usable_sprites], 'chest', graphics['Chests'][1])
                        if style == 'Player':
                            self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites,self.create_magic,self.usable_objects)

    def create_magic(self,style,strength,speed):
        if style == 'fireball':
            self.magic.fireball(self.player, [self.visible_sprites, self.attack_sprites], strength, speed)

    def usable_objects(self):
        collision_sprites = pygame.sprite.spritecollide(self.player, self.usable_sprites, True)
        if collision_sprites:
            for target in collision_sprites:
                if target.sprite_type == 'door':
                    self.is_running = False
                    self.win = True
                if target.sprite_type == 'chest':
                    target.kill()

    def attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.to_attack_sprites, True)
                if collision_sprites:
                    for target in collision_sprites:
                        if target.sprite_type == 'chest':
                            target.kill()
                        else:
                            if target.can_be_damaged:
                                target.health -= attack_sprite.damage
                                target.can_be_damaged = False
                                target.hit_time = pygame.time.get_ticks()
                                if target.health <= 0:
                                    target.kill()

    def damage_logic(self,value):
        if self.player.can_be_damaged:
            self.player.health -= value
            self.player.can_be_damaged = False
            self.player.hit_time = pygame.time.get_ticks()
            if self.player.health <= 0:
                self.is_running = False

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.attack_logic()
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.transform.scale_by(pygame.image.load('Grafika/mapa.png').convert(),SCALE)
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)