"""Crop an SVG's viewBox to its rasterized ink bounding box + 4pt.

Step 3 of the TikZ -> SVG render recipe in README.md. dvisvgm's page box lands on
the TeX reference point and carries dead space, so this measures the true ink bbox
by rasterizing and rewrites width / height / viewBox on the <svg> tag in place.
The 4pt pad matches the `border=4pt` on the standalone document class.

Usage: python3 crop_viewbox.py NAME.svg
Requires: cairosvg + pillow (both in the `mininpu` conda env).
"""

import io
import re
import sys

import cairosvg
from PIL import Image

p, PAD, SCALE = sys.argv[1], 4.0, 8
s = open(p, encoding="utf-8").read()
m = re.search(r"(<svg[^>]*viewBox=')([-\d. ]+)('[^>]*>)", s)
vb = [float(x) for x in m.group(2).split()]
im = Image.open(io.BytesIO(cairosvg.svg2png(url=p, scale=SCALE, background_color="white"))).convert(
    "L"
)
bb = Image.eval(im, lambda q: 255 - q).getbbox()  # ink bbox, px
k = im.width / vb[2]  # px per user unit
x0, y0 = vb[0] + bb[0] / k - PAD, vb[1] + bb[1] / k - PAD
w, h = (bb[2] - bb[0]) / k + 2 * PAD, (bb[3] - bb[1]) / k + 2 * PAD
tag = re.sub(r"width='[^']*'", f"width='{w:f}pt'", m.group(0))
tag = re.sub(r"height='[^']*'", f"height='{h:f}pt'", tag)
tag = re.sub(r"viewBox='[^']*'", f"viewBox='{x0:f} {y0:f} {w:f} {h:f}'", tag)
open(p, "w", encoding="utf-8").write(s.replace(m.group(0), tag, 1))
