import pygame
from moviepy import *

clip = VideoFileClip("../videos/test.mp4").subclipped(10, 20)

# Reduce the audio volume to 80% of his original volume
clip = clip.with_volume_scaled(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font="example.ttf", text="Big Buck Bunny", font_size=70, color="white")

# Say that you want it to appear for 10s at the center of the screen
txt_clip = txt_clip.with_position("center").with_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available!)
video.write_videofile("../videos/result.mp4")