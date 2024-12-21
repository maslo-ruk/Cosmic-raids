# import pygame
# from pygame import movie
#
# class VideoPlayer:
#     def __init__(self, video_path):
#         self.video_path = video_path
#         self.playing = False
#
#     def play_video(self):
#         if not self.playing:
#             pygame.init()
#             pygame.display.set_mode((640, 480))
#             self.movie = pygame.movie.Movie(self.video_path)
#             self.movie.set_display(pygame.display.get_surface(), pygame.Rect(0, 0, 640, 480))
#             self.movie.play()
#             self.playing = True
#
#     def stop_video(self):
#         if self.playing:
#             self.movie.stop()
#             self.playing = False
#             pygame.quit()