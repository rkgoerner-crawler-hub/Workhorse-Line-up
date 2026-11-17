# Vectorize the white strokes inside the dark emblem: threshold, drop the white outside the blob, trace with potrace.
import numpy as np, potrace, json, sys
from PIL import Image
from collections import deque
im = Image.open('ref.png').convert('L')
a = np.array(im)
white = a > 128
h, w = white.shape
# flood-fill white from the border: that's the background outside the dark blob
outside = np.zeros_like(white)
q = deque()
for x in range(w):
    for y in (0, h - 1):
        if white[y, x]: outside[y, x] = True; q.append((y, x))
for y in range(h):
    for x in (0, w - 1):
        if white[y, x] and not outside[y, x]: outside[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and white[ny, nx] and not outside[ny, nx]:
            outside[ny, nx] = True; q.append((ny, nx))
art = white & ~outside
ys, xs = np.nonzero(art); print('art bbox', xs.min(), xs.max(), ys.min(), ys.max(), 'px', art.sum())
Image.fromarray((art * 255).astype('uint8')).save('art.png')
bm = potrace.Bitmap(art)
plist = bm.trace(turdsize=20, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opticurve=True, opttolerance=0.2)
ox, oy = xs.min(), ys.min()
d = []
for curve in plist:
    sp = curve.start_point
    seg = [f'M{sp.x - ox:.1f} {sp.y - oy:.1f}']
    for s in curve.segments:
        if s.is_corner:
            seg.append(f'L{s.c.x - ox:.1f} {s.c.y - oy:.1f}L{s.end_point.x - ox:.1f} {s.end_point.y - oy:.1f}')
        else:
            seg.append(f'C{s.c1.x - ox:.1f} {s.c1.y - oy:.1f} {s.c2.x - ox:.1f} {s.c2.y - oy:.1f} {s.end_point.x - ox:.1f} {s.end_point.y - oy:.1f}')
    d.append(''.join(seg) + 'Z')
W, H = xs.max() - ox + 1, ys.max() - oy + 1
json.dump({'d': ' '.join(d), 'w': int(W), 'h': int(H), 'n': len(plist)}, open('emblem.json', 'w'))
print('curves', len(plist), 'size', W, H, 'chars', len(' '.join(d)))
