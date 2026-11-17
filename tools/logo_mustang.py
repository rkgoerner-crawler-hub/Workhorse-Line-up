# A strong running mustang whose tail grows out of the underline. viewBox below; the tail starts at the left edge
# at y = LINE_Y with the line's thickness, so a plain line placed there flows straight into the horse.
import sys; sys.path.insert(0, '/home/claude/brand')
from sleek import catmull, path, limb
LINE_Y, LINE_W = 52, 10.4
VIEWBOX = '0 -14 204 124'
BODY = [(76, 41), (90, 35), (112, 38.5), (134, 33), (146, 22), (156, 11), (165, 5), (172, 5.5), (180, 10), (188, 18), (194, 25), (195, 30.5), (190, 34), (182, 33), (174, 30.5), (168, 30), (163, 38), (160, 50), (160, 61), (152, 70), (136, 75), (112, 75.5), (93, 72), (84, 69.5), (74, 63), (69, 53), (70, 45)]
LIMBS = [
  # front legs: one tucked high, one reaching
  [((148, 63), 17), ((163, 69), 10.5), ((172, 71), 7.5), ((168, 85), 5.8), ((173, 92), 5.4)],
  [((139, 67), 16), ((150, 82), 9.5), ((158, 93), 6.2), ((172, 99.5), 5.4), ((181, 98.5), 5)],
  # hind legs: one driving back, one under the body
  [((84, 57), 28), ((74, 76), 15), ((64, 86), 7.5), ((50, 96), 5.8), ((40, 99.5), 5.4)],
  [((97, 61), 23), ((99, 80), 12.5), ((95, 92), 7.2), ((103, 102), 5.8), ((110, 103), 5.4)],
  # ears
  [((168.5, 7), 6.5), ((164.5, -5), 0.5)], [((173, 7), 5.5), ((172, -4), 0.5)],
  # mane streaming back
  [((166, 7), 10), ((153, 2), 7.5), ((138, 6), 4), ((126, 14), 0.5)],
  [((160, 13), 10), ((146, 11), 7), ((133, 18), 3), ((122, 26), 0.5)],
  [((153, 21), 9), ((141, 22), 6), ((130, 29), 2.5), ((122, 36), 0.5)],
  [((146, 28), 7), ((137, 31), 4), ((130, 37), 0.5)],
  # tail: grows out of the line, sweeps up into the rump, with a couple of loose strands
  [((0, LINE_Y), LINE_W), ((20, LINE_Y), LINE_W + 0.6), ((40, 50.5), 12.5), ((56, 46), 14.5), ((70, 44), 12), ((82, 48), 6)],
  [((40, 50), 4), ((28, 44), 3), ((16, 42), 0.5)],
  [((50, 53), 4), ((38, 58), 2.5), ((26, 59), 0.5)],
]
def mustang(fill='currentColor'):
    parts = [path(catmull(BODY, closed=True, n=10))] + [limb(s) for s in LIMBS]
    return ''.join(f'<path d="{d}" fill="{fill}"/>' for d in parts)
