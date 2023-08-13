from moviepy.editor import *
import numpy as np

def make_frame(t):
  print(t)
  w, h = 320, 180

  return np.random.random_integers(0, 255, (h, w, 3))

clip = VideoClip(make_frame, duration=2)
clip.write_videofile('output/test.mp4', fps=24)
