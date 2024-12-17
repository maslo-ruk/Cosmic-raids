# Тест меню
import pygame

# pygame setup
pygame.init()
size = width, height = 1920, 1280
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Тестовое меню")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    fon = pygame.image.load("../images/Space sky.png")
    fon = pygame.transform.scale(fon, (1920, 1280))
    screen.blit(fon, (0, 0))
    galacktika1 = pygame.image.load("../images/Galactika1.png")
    galacktika1 = pygame.transform.scale(galacktika1, (800, 1000))
    screen.blit(galacktika1, (480, -300))
    galacktika2 = pygame.image.load("../images/galactika2.png")
    galacktika2 = pygame.transform.scale(galacktika2, (1000, 500))
    screen.blit(galacktika2, (30, 200))
    # planeta2 = pygame.image.load("../images/planet2.png")
    # planeta2 = pygame.transform.scale(planeta2, (1700, 900))
    # screen.blit(planeta2, (300, 100))
    planeta = pygame.image.load("../images/planet.png")
    planeta = pygame.transform.scale(planeta, (1200, 600))
    screen.blit(planeta, (300, 100))
    pygame.display.update()
    dt = clock.tick(30) / 1000

pygame.quit()
