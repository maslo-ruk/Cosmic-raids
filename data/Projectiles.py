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