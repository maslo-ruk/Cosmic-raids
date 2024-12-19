import pygame

WIDTH = 30
HEIGHT = 30
COLOR = pygame.Color(215, 215, 215)


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.size = (WIDTH, HEIGHT)
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR)
        self.screen = screen

    def place(self, pos):
        self.screen.blit(self.image, pos)
