import math

MAG_MEMORY = {}
SQUARE_MEMORY = {}
SQRT_MEMORY = {0: 0}

"""
Retrieves the magnitude of a 3d vector from memory

Returns: None or float

UNUSED
"""
def get_mag(p, mem=MAG_MEMORY, i=0):
  current = p[i]
  stored = current in mem

  if i == len(p) - 1:
    if stored:
      return mem[current]
    else:
      return None
  else:
    if not stored:
      mem[current] = {}

    return get_mag(p, mem[current], i+1)

"""
Stores the magnitude of a 3d vector in memory

UNUSED
"""
def store_mag(p, val, mem=MAG_MEMORY, i=0):
  current = p[i]

  if i == len(p) - 1:
    mem[current] = val 
  else:
    stored = current in mem

    if not stored:
      mem[current] = {}

    return store_mag(p, val, mem[current], i+1) 


def memoize_operation(func, mem, val):
  if val in mem:
    return mem[val]
  else:
    result = func(val)
    mem[val] = result

    return result

def memoized_square(x):
  return memoize_operation(lambda y: y ** 2, SQUARE_MEMORY, x)

def memoized_sqrt(x):
  return memoize_operation(lambda y: math.sqrt(y), SQRT_MEMORY, x)


def color_diff(p1, p2):
  if len(p1) != 3 or len(p2) != 3:
    raise Exception('Color diff function only excepts 3 dimensional vectors')

  magnitude = 0

  for i in range(0, 3):
    diff = p1[i] - p2[i]
    magnitude += memoized_square(diff)

  return memoized_sqrt(magnitude)