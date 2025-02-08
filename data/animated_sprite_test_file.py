import pygame
from config import *


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, sheet_left, image, image_left,  colums, rows, colums2, rows2, x, y):
        super().__init__(all_sprites)
        self.frames_rigth = []
        self.frames_left = []
        self.frames_2 = []
        self.frames_2_left = []
        self.x = x
        self.y = y
        self.flag = False
        self.to_right = True
        self.cut_sheets(sheet, colums, rows, True, True)
        self.cut_sheets(image, colums, rows, False, True)
        self.cut_sheets(image_left, colums, rows, False, False)
        self.cut_sheets(sheet_left, colums, rows, True, False)
        self.cur_frame = 0
        if self.flag:
            if self.to_right:
                self.image = self.frames_rigth[self.cur_frame]
            else:
                self.image = self.frames_left[self.cur_frame]
        else:
            self.image = self.frames_2[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheets(self, sheet, colums, rows, fflag, rightt=None):
        self.rect = pygame.Rect(0,
                                0,
                                sheet.get_width() // colums,
                                sheet.get_height() // rows)
        for i in range(rows):
            for j in range(colums):
                frame_location = (self.rect.w * j, self.rect.h * i)
                if fflag:
                    if rightt:
                        self.frames_rigth.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
                    else:
                        self.frames_left.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
                else:
                    if rightt:
                        self.frames_2.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
                    else:
                        self.frames_2_left.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
    def update(self):
        if self.flag:
            if self.to_right:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_rigth)
                self.image = self.frames_rigth[self.cur_frame]
            else:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left)
                self.image = self.frames_left[self.cur_frame]
        else:
            if self.to_right:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_2)
                self.image = self.frames_2[self.cur_frame]
            else:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_2_left)
                self.image = self.frames_2_left[self.cur_frame]

    def changes(self, x, y):
        self.rect = self.rect.move(x - self.x, y - self.y)
        self.x = x
        self.y = y
    def flagg(self):
        self.flag = True

    def flagg_ne(self):
        self.flag = False

    def right(self):
        self.to_right = True

    def left(self):
        self.to_right = False
