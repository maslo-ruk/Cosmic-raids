import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle



    def update(self):
        # Двигаем линию в зависимости от угла
        self.rect.x += 10 * self.angle[0]
        self.rect.y += 10 * self.angle[1]

        # Удаляем линию, если она выходит за границы экрана
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()


class Bullets(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('pink')
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle

    def update(self, rects, t):
        # Двигаем линию в зависимости от угла
        self.rect.x += 10 * self.angle[0]
        self.rect.y += 10 * self.angle[1]

        a = self.collides(rects, t)
        # Удаляем линию, если она выходит за границы экрана
        if a:
            self.kill()

    def collides(self, rects, own_rect):
        from data.player import Entity
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != own_rect:
                if isinstance(i, Entity):
                    i.hp -= 1
                return True


class Grenade(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((130, 150, 52)) # болотный зеленый
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle
        self.velocity_x = 0  # начальная скорость по x
        self.velocity_y = 0  # начальная скорость по y
        self.is_launched = False  # флаг, указывающий, был ли осуществлен бросок
        self.time = 0  # время

    # def launch(self, velocity, mouse_x, mouse_y):
    #     dx = mouse_x - self.rect.centerx
    #     dy = mouse_y - self.rect.centery
    #     norm = (dx  2 + dy  2)  0.5
    #     if norm != 0:  # Проверка для избежания деления на ноль
    #         self.velocity_x = velocity * dx / norm
    #         self.velocity_y = -velocity * dy / norm
    #         self.is_launched = True
    #         self.time = 0  # сброс времени для нового броска

    def update(self, rects, t):
        if self.is_launched:
            self.time += 1  # обновление времени
            # Обновление положения квадрата
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y #* 0.1 + 0.5 * 0.8 * self.time  2 / 0.8 - GRAVI
            self.velocity_y += 0.8

            # Проверка на рикошет
            if self.rect.y >= 600 - 50:
                self.rect.y = 600 - 50
                self.velocity_x *= 0.6
                self.velocity_y = -self.velocity_y * 0.7  # уменьшение скорости при рикошете
                self.time = 0  # сброс времени для рикошета

            if self.rect.x >= 900 - 50:
                self.rect.x = 900 - 50
                self.velocity_y *= 0.8
                self.velocity_x = -self.velocity_x * 0.7  # уменьшение скорости при рикошете
                self.time = 0  # сброс времени для рикошета

            if self.rect.x <= 30:
                self.rect.x = 30
                self.velocity_y *= 0.8
                self.velocity_x = -self.velocity_x * 0.7  # уменьшение скорости при рикошете
                self.time = 0  # сброс времени для рикошета


            # Если квадрат упал достаточно низко, сбрасываем флаг
            if self.rect.y >= 600 - 50 and abs(self.velocity_y) < 1:
                self.is_launched = False

    def collides(self, rects, own_rect):
        from data.player import Entity
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != own_rect:
                if isinstance(i, Entity):
                    i.hp -= 20
                return True
