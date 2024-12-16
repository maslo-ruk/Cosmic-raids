# Тест меню
import pygame

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Тестовое меню")
running = True

while running:
    fon = pygame.image.load("../images/Space sky.png")
    fon = pygame.transform.scale(fon, (1280, 720))
    screen.blit(fon, (0, 0))
    galacktika1 = pygame.image.load("../images/Galactika1.png")
    galacktika1 = pygame.transform.scale(galacktika1, (800, 1000))
    screen.blit(galacktika1, (480, -300))
    galacktika2 = pygame.image.load("../images/galactika2.png")
    galacktika2 = pygame.transform.scale(galacktika2, (1000, 500))
    screen.blit(galacktika2, (30, -300))
    planeta2 = pygame.image.load("../images/Без названия1153_20241214145529.png")
    planeta2 = pygame.transform.scale(planeta2, (1700, 900))
    screen.blit(planeta2, (300, 100))
    speed_planeta2 = 0.7
    speed_galackika1 = 1
    speed_galackika2 = 0.5
    galacktika2_y = 200
    galacktika1_y = -300
    planeta2_y = 70
    for i in range(20):
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(fon, (0, 0))
        galacktika1_y += speed_galackika1
        galacktika2_y += speed_galackika2
        planeta2_y -= speed_planeta2
        screen.blit(galacktika1, (480, galacktika1_y))
        screen.blit(galacktika2, (30, galacktika2_y))
        screen.blit(planeta2, (-200, planeta2_y))
        pygame.display.update()
    for i in range(20):
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(fon, (0, 0))
        # Изменяем значение координаты Y
        galacktika1_y -= speed_galackika1
        galacktika2_y -= speed_galackika2
        planeta2_y += speed_planeta2
        screen.blit(galacktika1, (480, galacktika1_y))
        screen.blit(galacktika2, (30, galacktika2_y))
        screen.blit(planeta2, (-200, planeta2_y))
        pygame.display.update()
    # limits FPS to 60
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()
