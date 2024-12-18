import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mishka Example")


class Mishka:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)  # Красный
        self.mishka_on = False  # По умолчанию мышь не над мишкой

    def update(self, mouse_pos):
        self.mishka_on = self.rect.collidepoint(mouse_pos)
        if self.mishka_on:
            self.color = (0, 255, 0)  # Если мышь над мишкой, делаем цвет зеленым
        else:
            self.color = (255, 0, 0)  # Иначе красный

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


mishka = Mishka(100, 100, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    mishka.update(mouse_pos)

    screen.fill((255, 255, 255))
    mishka.draw(screen)

    pygame.display.flip()

pygame.quit()