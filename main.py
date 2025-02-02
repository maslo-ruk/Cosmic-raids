import pygame
from data.platformer import Platformer
from data.player import Player


def main():
    pygame.init()
    size = width, height = 1500, 900
    player = Player((300, 200))
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    current_scene = Platformer((3000, 1200), screen, clock, player)
    runi = True
    sound = 'sounds/cosmic_battle.mp3'
    pygame.mixer.Sound(sound).play(-1)
    pygame.mixer.Sound(sound).set_volume(1.0)
    while runi:
        a = current_scene.run(sound)
        if a:
            current_scene = Platformer((3000, 1200), screen, clock, player)
    pygame.quit()


if __name__ == '__main__':
    main() 
