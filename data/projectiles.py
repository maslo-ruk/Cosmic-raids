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
    def __init__(self, start_pos, rects):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('images/oktavia_grenade.png'), (20, 20)) # картинка гранаты
        # self.image.fill((130, 150, 52)) # болотный зеленый
        self.rect = self.image.get_rect(center=start_pos)
        self.rects = rects
        self.velocity_x = 0  # начальная скорость по x
        self.velocity_y = 0  # начальная скорость по y
        self.is_launched = False  # флаг, указывающий, был ли осуществлен бросок
        self.time = 0  # время

    def update(self, screen, rects, player_rect):
        if self.is_launched:
            self.time += 1  # обновление времени
            # Обновление положения квадрата
            self.rect.x += self.velocity_x
            self.col1 = self.collides(rects, player_rect)
            if self.col1 and (self.velocity_x > 0):
                self.rect.right = self.col1.left
                self.velocity_x = -self.velocity_x * 0.7
            elif self.col1 and (self.velocity_x < 0):
                self.rect.left = self.col1.right
                self.velocity_x = -self.velocity_x * 0.7
            self.rect.y += self.velocity_y
            self.col2 = self.collides(rects, player_rect)
            if not self.col2:
                self.velocity_y += 0.5
            if self.col2 and (self.velocity_y < 0):
                self.rect.top = self.col2.bottom
                print(self.velocity_y)
                self.velocity_y = -self.velocity_y * 0.7
                print(self.velocity_y)
            elif self.col2 and (self.velocity_y > 0):
                self.rect.bottom = self.col2.top
                self.velocity_y = -self.velocity_y * 0.7
            if abs(self.velocity_x) <= 0.7:
                self.velocity_x = 0

            if self.time == 60 * 3: #отслеживаем время взрыва по кадрам, где 60 - fps
                pygame.mixer.Sound('sounds/bolshoy-vzryiv.mp3').play()
                self.babax(rects)

            # Если квадрат упал достаточно низко, сбрасываем флаг
            if self.rect.y >= 600 - 50 and abs(self.velocity_y) < 1:
                self.is_launched = False

    def collides(self, rects, player_rect):
        from data.player import Entity
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != player_rect:
                return i.rect
        return False

    def babax(self, rects):
        from data.player import Entity
        n = pygame.Rect(self.rect.center[0] - 50, self.rect.center[1] - 50, 100, 100)
        for i in rects:
            if n.colliderect(i.rect) and i.rect != n:
                if isinstance(i, Entity):
                    i.hp -= 15
        self.kill()
        self.vzriv = False
