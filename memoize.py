from moviepy.editor import *
import numpy as np
from util.pixels import *

THRESHOLD = 100

def make_frame(t, clip):
  current = clip.get_frame(t)
  time_since_last = 1/clip.fps

  if (t == 0):
    return current
    
  prev = clip.get_frame(t - (time_since_last * 2))
  frame = []

  for y in range(0, clip.h):
    row = []
    for x in range(0, clip.w):
      prev_pixel = prev[y][x]
      current_pixel = current[y][x]
      diff = color_diff(prev_pixel, current_pixel)

      if diff < THRESHOLD:
        row.append(prev_pixel)
      else:
        row.append(current_pixel)

    frame.append(row)

  return np.array(frame)

def main(filename, start=31, end=33):
  duration = end - start
  clip = VideoFileClip(f'input/{filename}').subclip(start, end)
  fps = clip.fps
  mf = lambda t : make_frame(t, clip)

  output = VideoClip(make_frame=mf, duration=duration)
  output.write_videofile(f'output/memoize_{filename}', fps=fps)

if __name__ == '__main__':
  main('footage.mp4')