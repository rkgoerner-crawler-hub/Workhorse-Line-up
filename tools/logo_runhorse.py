# Sleek galloping horse silhouette: a smooth closed spline for the body and tapered splines for legs, tail and ear.
import math
def catmull(pts, closed=False, n=8):
    out = []
    P = pts[:]
    if closed: P = [P[-1]] + P + [P[0], P[1]]
    else: P = [P[0]] + P + [P[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in range(2)))
    if not closed: out.append(pts[-1])
    return out
def path(points, close=True):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in points) + (' Z' if close else '')
def limb(spec, n=10):
    pts = [p for p, w in spec]; ws = [w for p, w in spec]
    c = catmull(pts, n=n)
    # widths along the sampled line
    W = []
    for i in range(len(pts) - 1):
        for k in range(n): W.append(ws[i] + (ws[i + 1] - ws[i]) * k / n)
    W.append(ws[-1])
    L, R = [], []
    for i, (x, y) in enumerate(c):
        a = c[max(0, i - 1)]; b = c[min(len(c) - 1, i + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; d = math.hypot(dx, dy) or 1
        nx, ny = -dy / d, dx / d; h = W[i] / 2
        L.append((x + nx * h, y + ny * h)); R.append((x - nx * h, y - ny * h))
    tip = c[-1]
    return path(L + [tip] + R[::-1])
BODY = [(54, 33), (70, 28.5), (94, 31.5), (116, 29.5), (128, 23), (138, 13), (146, 4.5), (152, 0), (160, 3), (170, 10.5), (179, 18), (184.5, 24), (183, 29), (176, 30), (167, 27.5), (160, 24), (155, 23.5), (152, 31), (151, 44), (146, 57), (132, 65), (110, 66.5), (86, 64), (71, 61), (58, 57.5), (50, 50), (48.5, 41)]
LIMBS = [
  [((138, 56), 15), ((152, 64), 9), ((164, 68.5), 6), ((180, 64.5), 4.6), ((190, 60.5), 4)],
  [((130, 58), 14), ((142, 72), 8.5), ((152, 82), 5.6), ((166, 86.5), 4.6), ((175, 85), 4)],
  [((63, 49), 23), ((51, 62), 13), ((40, 72), 6.2), ((22, 80), 4.6), ((8, 84), 4)],
  [((75, 53), 18), ((66, 70), 11), ((56, 82), 6), ((40, 92), 4.6), ((28, 96), 4)],
  [((51, 37), 7), ((37, 32), 9.5), ((22, 32), 7.5), ((10, 36), 4), ((2, 43), 0.5)],
  [((151.5, 3.5), 5.5), ((148.5, -7), 0.5)],
  [((155, 4), 5), ((154, -6), 0.5)],
]
def sleek_horse(fill='currentColor'):
    parts = [path(catmull(BODY, closed=True, n=10))] + [limb(s) for s in LIMBS]
    return ''.join(f'<path d="{d}" fill="{fill}"/>' for d in parts)
VIEWBOX = '0 -10 196 108'
