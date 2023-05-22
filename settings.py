from csv import reader
from os import walk
import pygame

#ustawienia Wyswietlania:
WIDTH = 1280
HEIGHT = 720
MODE_TYPES = [pygame.FULLSCREEN, pygame.NOFRAME, pygame.SHOWN] #sposob wyswietlania

TILESIZE = 16
SCALE = 3

FPS = 60

#menu
MENU_FONT_SIZE= "Green"
MENU_BACKGROUND = "Black"

#UI
BAR_HEIGHT = 20
BAR_WIDTH = 200
ITEM_SIZE = 80
UI_FONT_SIZE = 18
UI_FONT = 'Comic Sans MS'

END_BACKGROUND = (0, 0, 255)
UI_BG_COLOR = (0, 0, 0)
UI_BORDER_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)

HEALTH_BAR_COLOR = (255, 0, 0)
ENERGY_COLOR = (0, 255, 0)
UI_BORDER_COLOR_ACTIVE = 'gold'

magic_data = {
	'fireball': {'strength': 10, 'speed': 10, 'cost': 10, 'cooldown': 500,'graphic': '../Grafika/fireball.png'},
	'lightning': {'strength': 20, 'speed': 20, 'cost': 20, 'cooldown': 1000, 'graphic': 'yellow'}
}

monster_data = {
	'slime' : {'health': 30, 'speed': 7, 'strength': 10, 'graphic': '../Grafika/Enemies/2.png', 'notice_radius': 400},
}

def import_csv_layout(path):
	terrain_map = []
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ',')
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(),SCALE)
			surface_list.append(image_surf)

	return surface_list