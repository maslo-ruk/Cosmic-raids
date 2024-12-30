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
BLUE = (0, 0, 255)

# Параметры движения
x = 100  # начальная позиция по x
y = height  # начальная позиция по y
angle = 90  # угол броска в градусах
velocity = 0  # начальная скорость
gravity = 10  # ускорение свободного падения
time = 0  # время
is_launched = False  # флаг, указывающий, был ли осуществлен бросок
flag = False

# Основной цикл
running = True
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
                dx = mouse_x - x
                dy = mouse_y - y
                angle = (dx, dy)
                print(angle)
                if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
                    norm = (dx ** 2 + dy ** 2) ** 0.5
                    # direction = (dx / norm, dy / norm)
                    # print(direction)
                # angle_rad = math.radians(angle)

                # Начальные скорости
                velocity_x = velocity * dx / norm
                velocity_y = -velocity * dy / norm
                time = 0  # сброс времени для нового броска
                is_launched = True  # устанавливаем флаг броска

    # Очистка экрана
    screen.fill(WHITE)

    if is_launched:
        # Обновление времени
        time += 0.1

        # Обновление положения квадрата
        x += velocity_x * 0.1
        y += velocity_y * 0.1 + 0.5 * gravity * time ** 2

        # Проверка на рикошет
        if y >= height - 50:
            y = height - 50
            velocity_x = velocity_x * 0.9
            velocity_y = -velocity_y * 0.7  # уменьшение скорости при рикошете
            time = 0  # сброс времени для рикошета

        # Отрисовка квадрата
        pygame.draw.rect(screen, BLUE, (x, y, 50, 50))

        # Если квадрат упал достаточно низко, сбрасываем флаг
        if y >= height - 50 and abs(velocity_y) < 1:
            # is_launched = False
            flag = False

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(30)


pygame.quit()