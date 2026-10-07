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

| Climb | Day | Mile | Length | Gain | Avg | Steepest 0.25 mi |
|---|---|---|---|---|---|---|
| Peachy Canyon Rd | 1 | 0.6–2.0 | 1.37 mi | 331 ft | 4.6% | 8.3% |
| Peachy Canyon Rd | 1 | 2.2–2.9 | 0.75 mi | 267 ft | 6.8% | 8.2% |
| Peachy Canyon Rd | 1 | 7.3–7.9 | 0.53 mi | 163 ft | 5.8% | 7.8% |
| Santa Rita Rd | 2 | 19.6–21.0 | 1.35 mi | 354 ft | 5.0% | 7.9% |
| Old Creek Rd | 2 | 27.6–28.2 | 0.67 mi | 252 ft | 7.1% | 8.6% |
| Cabrillo St | 2 | 32.3–32.6 | 0.37 mi | 170 ft | 8.6% | 10.5% |
| Pomeroy Rd | 4 | 8.6–9.0 | 0.34 mi | 150 ft | 8.3% | 9.5% |
| **Harris Grade Rd** | 4 | 39.3–40.9 | 1.62 mi | 490 ft | 5.7% | 8.2% |

The **whole climb** is drawn on the map, with a **black overlay on the steepest stretch**.

Days 3 has no qualifying climb. Grades come from SRTM elevation data sampled every
25 m and lightly smoothed; treat them as approximate, especially the maxima.

## Ride photos

The map page accepts photo drops. It reads each photo's EXIF **GPS position and timestamp**
in your browser, places it on the map, and reports how far it sits from the planned line.

- The panel is behind a shared password (ask the group). The **upload link is encrypted**
  with that password using AES-256-GCM, with the key derived via PBKDF2-SHA256 at 310,000
  iterations. The page holds only ciphertext, so the link genuinely cannot be recovered
  without the password — this is not a hide-the-element gate.
  Caveat: a short password can still be attacked offline by anyone who saves the page.
- Photos **never leave your computer** — there is no upload, no server, no account.
- A photo taken **on one of the ride dates** is trusted even when well off the line —
  being 2 miles off on the right day is a real detour, not a bad photo. It is matched
  to that day's route by date, not by whichever route happens to be nearest.
- Photos more than **15 miles** from the route are **rejected** — they are not placed
  on the map and take no part in the deviation analysis. Distance is measured to the
  nearest point on *any* of the five days, so a shortcut or a side trip still counts.
- Accepted photos more than **75 m** off the planned route are flagged red.
- Off-route photos close in time and space are grouped; a group counts as a
  **likely deviation** when it has 3+ photos or photos from 2+ different cameras.
  A lone stray photo is reported as weak evidence, not a route change.
- **Export placements** downloads a JSON of every photo's day, mile, offset and
  timestamp, plus the detected deviations — no image data, just coordinates.

Each placed photo gets one of four roles, shown by dot colour:

| Role | Dot | Meaning |
|---|---|---|
| **adjust** | orange | Ride date, **07:00–18:00**, **75–250 m** off the line. Proposes a route adjustment. |
| **evening** | purple | Ride date, after 18:00, near the line. Counts **only if that evening covered 0.5 mi or more** — unscheduled evening riding is part of the trip, standing outside a bar is not. |
| **lodging** | grey | Within 300 m of where a day starts or finishes — camp or the hotel. Never changes a route. |
| **poi** | day colour | On the line, or further than 250 m off — a point of interest. Never changes a route. |
| **pretrip** | grey | Not taken on a ride date. Never changes a route. |
| **train** | grey | Day 5, past the Amtrak platform. Never changes a route. |

Photos carrying **no GPS at all** are not discarded. They collect in a **"Photos without
location"** album in the sidebar — a thumbnail grid with whatever timestamp and camera the
file still has. Click any one to view it full size. They are listed in the export too, so
nothing a rider sends goes missing just because their phone had location switched off.

An adjustment is only **confirmed** when a cluster has 3+ photos or photos from 2+ cameras,
**and** the group was actually moving. A huddle of photos inside 180 m spanning more than
20 minutes is read as a stop, not a route — so an evening in one spot never redraws the line,
however many photos it produces.

The page itself never re-routes — it cannot, being static. Export the placements and the
adjustment is applied offline with BRouter, then the updated GPX is published here. The five tracks are
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
