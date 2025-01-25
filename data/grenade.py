import pygame
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Бросок квадрата")

# Цвета
WHITE = (255, 255, 255)
GREEN = (130, 108, 52)

# Параметры движения
class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # создаем квадрат размером 50x50
        self.image.fill(GREEN)  # заполняем его синим цветом
        self.rect = self.image.get_rect(center=(x, y))  # устанавливаем начальную позицию

        self.velocity_x = 0  # начальная скорость по x
        self.velocity_y = 0  # начальная скорость по y
        self.gravity = 10  # ускорение свободного падения
        self.is_launched = False  # флаг, указывающий, был ли осуществлен бросок
        self.time = 0  # время

    def launch(self, velocity, mouse_x, mouse_y):
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        norm = (dx ** 2 + dy ** 2) ** 0.5
        if norm != 0:  # Проверка для избежания деления на ноль
            self.velocity_x = velocity * dx / norm
            self.velocity_y = -velocity * dy / norm
            self.is_launched = True
            self.time = 0  # сброс времени для нового броска

    def update(self):
        if self.is_launched:
            self.time += 0.1  # обновление времени
            # Обновление положения квадрата
            self.rect.x += self.velocity_x * 0.1
            self.rect.y += self.velocity_y * 0.1 + 0.5 * self.gravity * self.time ** 2

            # Проверка на рикошет
            if self.rect.y >= height - 50:
                self.rect.y = height - 50
                self.velocity_x *= 0.9
                self.velocity_y = -self.velocity_y * 0.7  # уменьшение скорости при рикошете
                self.time = 0  # сброс времени для рикошета

            # Если квадрат упал достаточно низко, сбрасываем флаг
            if self.rect.y >= height - 50 and abs(self.velocity_y) < 1:
                self.is_launched = False

# Создаем спрайт и группу спрайтов
square = Square(25, height - 25)  # начальная позиция по y - ниже на 50
all_sprites = pygame.sprite.Group()
all_sprites.add(square)

# Основной цикл
running = True
flag = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # ЛКМ
            if not flag:
                flag = True
                # Установка начальных параметров броска
                velocity = 200  # начальная скорость
                mouse_x, mouse_y = pygame.mouse.get_pos()
                square.launch(velocity, mouse_x, mouse_y)

    # Очистка экрана
    screen.fill(WHITE)

    # Обновление спрайтов
    all_sprites.update()

    # Отрисовка всех спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()