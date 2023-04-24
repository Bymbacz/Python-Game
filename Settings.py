from csv import reader
from os import walk
import pygame

#ustawienia Wyswietlania:
WIDTH = 1280
HEIGHT = 720
MODE_TYPES = [pygame.FULLSCREEN, pygame.NOFRAME, pygame.SHOWN] #sposob wyswietlania

TILESIZE = 64
SCALE = 4

FPS = 60

MENU_FONT_SIZE= "Green"
MENU_BACKGROUND = "Black"

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