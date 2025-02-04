import pygame


def sound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(1)
