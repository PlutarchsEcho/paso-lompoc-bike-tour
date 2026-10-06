#!/usr/bin/env python3
"""Detect long gentle grades (1+ mi sustained at ~2.5-6%) from the tour GPX files.

Produces GRADES.json, injected into index.html as `var GRADES = [...]`.
Stretches already covered by the dark-highlighted CLIMBS array are skipped.
Run from the repo root:  python3 tools/find_grades.py && python3 tools/inject.py
"""
import json
import math
import re
import sys
from xml.etree import ElementTree as ET

ROOT = "."
GPX = "{http://www.topografix.com/GPX/1/1}"

html = open(f"{ROOT}/index.html").read()
DAYS = json.loads(re.search(r"var DAYS = (\[.*\]);", html).group(1))
CLIMBS = json.loads(re.search(r"var CLIMBS = (\[.*\]);", html).group(1))


def hav(a, b):
    R = 6371000
    p, q = math.radians(a[0]), math.radians(b[0])
    dp, dl = p - q, math.radians(b[1] - a[1])
    x = math.sin(dp / 2) ** 2 + math.cos(p) * math.cos(q) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(x))


out = []
for di, d in enumerate(DAYS):
    pts = []
    for tp in ET.parse(f"{ROOT}/{d['file']}").getroot().iter(GPX + "trkpt"):
        ele = tp.find(GPX + "ele")
        pts.append((float(tp.get("lat")), float(tp.get("lon")),
                    float(ele.text) if ele is not None else None))
    if any(p[2] is None for p in pts):
        print(f"{d['file']}: no elevation, skipped", file=sys.stderr)
        continue
    n = len(pts)
    dist = [0.0]
    for i in range(1, n):
        dist.append(dist[-1] + hav(pts[i - 1][:2], pts[i][:2]))
    spacing = max(dist[1], 1.0)
    w = max(3, int(round(150 / spacing)))  # elevation smoothing half-window (~150 m)
    se = [sum(p[2] for p in pts[max(0, i - w):i + w + 1]) / len(pts[max(0, i - w):i + w + 1])
          for i in range(n)]
    # smoothed grade at each point, measured over ~180 m centered window
    g = [0.0] * n
    for i in range(n):
        j = i
        while j < n - 1 and dist[j] - dist[i] < 180:
            j += 1
        k = i
        while k > 0 and dist[i] - dist[k] < 180:
            k -= 1
        dd = dist[j] - dist[k]
        if dd >= 60:
            g[i] = (se[j] - se[k]) / dd * 100
    mild = [2.5 <= x <= 6.0 for x in g]
    runs, i = [], 0
    while i < n:
        if mild[i]:
            j = i
            while j < n and mild[j]:
                j += 1
            runs.append([i, j - 1])
            i = j
        else:
            i += 1
    merged = []
    for r in runs:
        if merged and (dist[r[0]] - dist[merged[-1][1]]) / 1609.34 < 0.15:
            merged[-1][1] = r[1]
        else:
            merged.append(r)
    for a, b in merged:
        len_mi = (dist[b] - dist[a]) / 1609.34
        if len_mi < 0.5:
            continue
        s_mi, e_mi = dist[a] / 1609.34, dist[b] / 1609.34
        if any(c["day"] == di and min(e_mi, c["endMi"]) - max(s_mi, c["startMi"]) > 0.25
               for c in CLIMBS):
            continue
        gain_ft = sum(max(0.0, se[i] - se[i - 1]) for i in range(a + 1, b + 1)) * 3.28084
        avg = gain_ft / (len_mi * 5280) * 100
        if not 2.4 <= avg <= 6.2:
            continue
        seg = pts[a:b + 1]
        step = max(1, len(seg) // 40)
        line = [[round(p[0], 5), round(p[1], 5)] for p in seg[::step]]
        if line[-1] != [round(seg[-1][0], 5), round(seg[-1][1], 5)]:
            line.append([round(seg[-1][0], 5), round(seg[-1][1], 5)])
        out.append({
            "startMi": round(s_mi, 2), "endMi": round(e_mi, 2),
            "lenMi": round(len_mi, 2), "gainFt": round(gain_ft),
            "avgPct": round(avg, 1), "maxPct": round(max(g[a:b + 1]), 1),
            "line": line, "day": di,
            "dayName": d["title"].split(" \u00b7")[0],
        })

json.dump(out, open(f"{ROOT}/GRADES.json", "w"), separators=(",", ":"))
for c in out:
    print(f"{c['dayName']}: mi {c['startMi']:>6}-{c['endMi']:<6} {c['lenMi']:>5} mi  "
          f"avg {c['avgPct']:>4}%  max {c['maxPct']:>4}%  gain {c['gainFt']:>5} ft")
print(f"TOTAL: {len(out)} long grades, {len(json.dumps(out))} bytes JSON", file=sys.stderr)
