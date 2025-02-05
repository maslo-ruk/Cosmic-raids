

CELL_SIZE = 60
WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE * 1.5
SIZE = (WIDTH, HEIGHT)
SPEED = CELL_SIZE // 5
HUB_SPEED = 4
JUMPSPEED = CELL_SIZE * 14 // 30
GRAVI = 1.2
ENEMY_SPEED = 7
COLOR = 'red'
POS = (250, 200)

DIFFICULTY = 0

WINDOW_SIZE = 1500, 900
def set_windowsize(a, b):
    global WINDOW_SIZE
    WINDOW_SIZE = a, b
# set_windowsize()
DOOR_SIZE = CELL_SIZE * 3

ROOM_SIZE = 3000, 1200
def change_room_size(new_size):
    global ROOM_SIZE
    ROOM_SIZE = new_size