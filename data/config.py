import pygame

CELL_SIZE = 30
WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE * 1.5
SIZE = (WIDTH, HEIGHT)
SPEED = 6
HUB_SPEED = 4
JUMPSPEED = 14
GRAVI = 0.8
COLOR = 'red'
POS = (250, 200)

DIFFICULTY = 0

all_sprites = pygame.sprite.Group()

WINDOW_SIZE = 1500, 900
DOOR_SIZE = CELL_SIZE * 3

ROOM_SIZE = 3000, 1200
def change_room_size(new_size):
    global ROOM_SIZE
    ROOM_SIZE = new_size