#Odpowiada za wyswietlanie mapy, gracza i obiektow, przekazuje to wszystko do maina
import pygame
from Settings import *
from player import Player
from tile import Tile
from random import choice

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

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
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'slime', graphics['Enemies'][1])
                        if style == 'Door':
                            if col == '0':
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'door', graphics['Door'][3])
                            else:
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'door', graphics['Door'][0])
                        if style == 'Chests':
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'chest', graphics['Chests'][1])
                        if style == 'Player':
                            self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

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