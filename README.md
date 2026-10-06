# Paso Robles → Lompoc · 5-day bike tour

Interactive route map: **https://plutarchsecho.github.io/paso-lompoc-bike-tour/**

Five GPX tracks for a Central Coast bike tour, Oct 8–12 2026, plus a self-contained
Leaflet map to view them. Routes are road-snapped with [BRouter](https://brouter.de)
over OpenStreetMap data; basemap tiles are Esri (switchable to topo, satellite or terrain).

| Day | Date | Route | Miles | Climb |
|---|---|---|---|---|
| 1 | Thu Oct 8 | Paso Robles → Peachy Canyon → Opolo → Tin City → Firestone Walker → Vinyl Vineyards | 31.05 | 2,757 ft |
| 2 | Fri Oct 9 | Vinyl Vineyards → Templeton → Santa Rita Rd (gravel) → Cayucos → Morro Bay | 40.69 | 3,318 ft |
| 3 | Sat Oct 10 | Morro Bay → Absolution Cellars → LOVR → There Does Not Exist → Claiborne & Churchill → Kulturhaus → Pismo | 32.49 | 1,358 ft |
| 4 | Sun Oct 11 | Pismo → Nipomo → Santa Maria → Harris Grade → O'Cairns Inn, Lompoc | 49.81 | 2,466 ft |
| 5 | Mon Oct 12 | O'Cairns Inn → Lompoc-Surf Amtrak | 10.41 | 122 ft |
| | | **Total** | **164.44** | **10,022 ft** |

## Notable climbs

The map lists every climb that is **over half a mile averaging 6%+**, or contains
**any pitch over 9%**. Click one to zoom to it and see its grade.

| Climb | Day | Mile | Length | Gain | Avg | Max |
|---|---|---|---|---|---|---|
| Peachy Canyon Rd | 1 | 0.8–1.6 | 0.71 mi | 226 ft | 6.0% | 9.2% |
| Peachy Canyon Rd | 1 | 2.1–3.0 | 0.85 mi | 266 ft | 5.9% | 10.6% |
| Peachy Canyon Rd | 1 | 7.5–7.7 | 0.12 mi | 58 ft | 8.9% | 9.8% |
| Willow Creek Rd | 1 | 11.7 | 0.09 mi | 44 ft | 9.0% | 9.0% |
| Santa Rita Rd | 2 | 20.0–21.0 | 0.95 mi | 283 ft | 5.7% | 16.1% |
| Old Creek Rd | 2 | 27.5–28.3 | 0.81 mi | 242 ft | 5.7% | 9.6% |
| Cabrillo St | 2 | 32.1–32.7 | 0.61 mi | 171 ft | 5.3% | 14.1% |
| Pomeroy Rd | 4 | 8.5–9.1 | 0.67 mi | 170 ft | 4.8% | 10.4% |
| **Harris Grade Rd** | 4 | 39.4–41.0 | 1.68 mi | 485 ft | 5.5% | 12.3% |
| Ocean Ave | 5 | 9.3–9.4 | 0.11 mi | 52 ft | 9.1% | 9.4% |

Days 3 has no qualifying climb. Grades come from SRTM elevation data sampled every
25 m and lightly smoothed; treat them as approximate, especially the maxima.

## Ride photos

The map page accepts photo drops. It reads each photo's EXIF **GPS position and timestamp**
in your browser, places it on the map, and reports how far it sits from the planned line.

- The panel is behind a shared password (ask the group).
  It is a **speed bump, not security** — the page is static, so anyone can bypass the
  gate with browser dev tools. It keeps casual visitors out, nothing more.
- Photos **never leave your computer** — there is no upload, no server, no account.
- Photos more than **15 miles** from every route are **rejected** — they are not placed
  on the map and take no part in the deviation analysis. Distance is measured to the
  nearest point on *any* of the five days, so a shortcut or a side trip still counts.
- Accepted photos more than **75 m** off the planned route are flagged red.
- Off-route photos close in time and space are grouped; a group counts as a
  **likely deviation** when it has 3+ photos or photos from 2+ different cameras.
  A lone stray photo is reported as weak evidence, not a route change.
- **Export placements** downloads a JSON of every photo's day, mile, offset and
  timestamp, plus the detected deviations — no image data, just coordinates.

The planned routes are **fixed**. Photo analysis is reporting only — it tells you where
the group rode off the planned line, and never rewrites a GPX. The five tracks are
byte-identical to the originals and stay that way.

Because GitHub Pages is static hosting, each person sees only their own photos; to
compare, collect the exported JSON files.

## Files

- [`day1_paso_peachy_tincity_vinyl.gpx`](day1_paso_peachy_tincity_vinyl.gpx)
- [`day2_santa_rita_to_morro_bay.gpx`](day2_santa_rita_to_morro_bay.gpx)
- [`day3_morro_bay_to_pismo.gpx`](day3_morro_bay_to_pismo.gpx) — includes waypoints for all 5 stops
- [`day4_pismo_harris_grade_lompoc.gpx`](day4_pismo_harris_grade_lompoc.gpx)
- [`day5_lompoc_to_surf_station.gpx`](day5_lompoc_to_surf_station.gpx)

## Notes

- **Day 2** crosses Santa Rita Road, a multi-mile unpaved gravel pass. Remote, steep, no services.
- **Day 4** matches Apple Maps' cycling route (49 mi / 2,200 ft stated; 49.8 / 2,466 here).
  It includes a **walk-only path** at the Santa Ynez River crossing on N H St in Lompoc —
  plan to push the bike roughly half a mile.
- **Day 5** ends at the Lompoc–Surf Amtrak platform. Confirm the Pacific Surfliner stops
  there that day and accepts bikes — it's a small unstaffed halt and not every train calls.
- Climb figures come from elevation models and vary by tool; Strava will recompute on upload.

## Uploading

Strava: **+ → Create a route → Import**, or **Routes → Import GPX**.
Garmin/Wahoo: sync from Strava, or import under Courses in Garmin Connect.
