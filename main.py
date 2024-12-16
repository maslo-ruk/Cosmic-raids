# Example file showing a circle moving on screen
# Примеры событий
# python -m pygame.examples.eventlist

import pygame

def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Белий кролик")
    running = True
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 1000)


pygame.quit()
