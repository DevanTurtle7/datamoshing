from moviepy.editor import *
import numpy as np
from util.pixels import *

THRESHOLD = 200
prev_render = []

def make_frame(t, clip):
  global prev_render
  current = clip.get_frame(t)
  time_since_last = 1/clip.fps

  if (t == 0):
    prev_render = current
    return current
    
  frame = []
  prev_frame = clip.get_frame(t - (time_since_last * 2))

  for y in range(0, clip.h):
    row = []
    for x in range(0, clip.w):
      prev_render_pixel = prev_render[y][x]
      prev_frame_pixel = prev_frame[y][x]
      current_pixel = current[y][x]
      diff = color_diff(prev_frame_pixel, current_pixel)

      if diff > THRESHOLD:
        row.append(current_pixel)
      else:
        row.append(prev_render_pixel)

    frame.append(row)

  prev_render = np.array(frame)
  return prev_render

# 1: 31, 33
# 2: 176, 178

def main(filename, start=31, end=33):
  duration = end - start
  clip = VideoFileClip(f'input/{filename}').subclip(start, end)
  fps = clip.fps
  mf = lambda t : make_frame(t, clip)

  output = VideoClip(make_frame=mf, duration=duration)
  output.write_videofile(f'output/memoize_{filename}', fps=fps)

if __name__ == '__main__':
  main('footage1.mp4')