import pygame
from data.functions import get_character

class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle
        self.speed = 24



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
        self.image = pygame.transform.scale(pygame.image.load('images/bullet.png'),
                                                (20, 20)) # картинка пули
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle
        self.speed = 24

    def update(self, rects, t):
        # Двигаем линию в зависимости от угла
        self.rect.x += self.speed * self.angle[0]
        self.rect.y += self.speed * self.angle[1]

        a = self.collides(rects, t)
        # Удаляем линию, если она выходит за границы экрана
        if a:
            self.kill()

    def collides(self, rects, own_rect):
        from data.player import Entity, Player, Land_enemy
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != own_rect.rect:
                if isinstance(i, Entity):
                    if isinstance(i, Player) and isinstance(own_rect, Land_enemy):
                        i.hp -= 1
                        i.health_lost += 1
                    if isinstance(i, Land_enemy) and isinstance(own_rect, Player):
                        i.hp -= 1
                return True


class Grenade(pygame.sprite.Sprite):
    def __init__(self, start_pos, rects, ):
        super().__init__()
        self.is_animated = False
        if get_character()[0][0] == 'Ричард':
            self.image = pygame.transform.scale(pygame.image.load('images/richards_grenade.png'),
                                                (30, 30)) # картинка гранаты
        elif get_character()[0][0] == 'Октавия':
            self.image = pygame.transform.scale(pygame.image.load('images/oktavia_grenade.png'),
                                                (30, 30))  # картинка гранаты
        else:
            self.image = pygame.transform.scale(pygame.image.load('images/astras_grenade.png'),
                                                (30, 30))  # картинка гранаты
        self.rect = self.image.get_rect(center=start_pos)
        self.width = self.rect.width
        self.rects = rects
        self.velocity_x = 0  # начальная скорость по x
        self.velocity_y = 0  # начальная скорость по y
        self.is_launched = False  # флаг, указывающий, был ли осуществлен бросок
        self.time = 0  # время
        #
    def update(self, screen, rects, player_rect):
        self.screen = screen
        if not self.is_animated:
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
                    self.velocity_y = -self.velocity_y * 0.7
                elif self.col2 and (self.velocity_y > 0):
                    self.rect.bottom = self.col2.top
                    self.velocity_y = -self.velocity_y * 0.7
                if abs(self.velocity_x) <= 0.7:
                    self.velocity_x = 0

            if self.time == 60 * 3: #отслеживаем время взрыва по кадрам, где 60 - fps
                self.is_animated = True
                pygame.mixer.Sound('sounds/bolshoy-vzryiv.mp3').play()
                self.babax(rects)
                self.image = pygame.transform.scale(pygame.image.load('images/vzr1.png'),
                                                (40, 40))
        else:
            self.time += 1  # обновление времени
            if self.time == 60 * 3: #отслеживаем время взрыва по кадрам, где 60 - fps
                self.rect.y -= 10
                self.image = pygame.transform.scale(pygame.image.load('images/vzr2.png'),
                                                (60, 60))
                self.rect.x += self.width - 30

            if self.time == 60 * 3.1: #отслеживаем время взрыва по кадрам, где 60 - fps
                self.rect.y -= 20
                self.image = pygame.transform.scale(pygame.image.load('images/vzr3.png'),
                                                (80, 80))
                self.rect.x += self.width - 40

            if self.time == 60 * 3.15: #отслеживаем время взрыва по кадрам, где 60 - fps
                self.rect.y -= 25
                self.image = pygame.transform.scale(pygame.image.load('images/vzr4.png'),
                                                (100, 100))
                self.rect.x += self.width - 50

            if self.time == 60 * 3.2: #отслеживаем время взрыва по кадрам, где 60 - fps
                self.rect.y += 55
                self.kill()

    def collides(self, rects, player_rect):
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
                    if i.hp < 0:
                        i.hp = 0


explosion_anim = ['images/vzr1.png', 'images/vzr2.png', 'images/vzr3.png', 'images/vzr4.png']


# class Explosion(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(explosion_anim[0])
#         self.rect = self.image.get_rect()
#         self.frame = 0
#         self.last_update = pygame.time.get_ticks()
#         self.frame_rate = 50
#
#     def update(self, center):
#         print(self.rect.center)
#         now = pygame.time.get_ticks()
#         if now - self.last_update >= 1000:
#             self.last_update = now
#             self.frame += 1
#             if self.frame > len(explosion_anim):
#                 self.kill()
#             else:
#                 center = self.rect.center
#                 self.image = pygame.transform.scale(pygame.image.load(explosion_anim[self.frame]), (75, 75)).convert_alpha()
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center
