import pygame
from pymediainfo import MediaInfo
from ffpyplayer.player import MediaPlayer
from os.path import exists, basename, splitext
from os import strerror
from errno import ENOENT

class Video:
    def __init__(self, video):
        self.path = video