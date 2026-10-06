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

## Ride photos

The map page accepts photo drops. It reads each photo's EXIF **GPS position and timestamp**
in your browser, places it on the map, and reports how far it sits from the planned line.

- Photos **never leave your computer** — there is no upload, no server, no account.
- Photos more than **75 m** off the planned route are flagged red.
- Off-route photos close in time and space are grouped; a group counts as a
  **likely deviation** when it has 3+ photos or photos from 2+ different cameras.
  A lone stray photo is reported as weak evidence, not a route change.
- **Export placements** downloads a JSON of every photo's day, mile, offset and
  timestamp, plus the detected deviations — no image data, just coordinates.

Because GitHub Pages is static hosting, each person sees only their own photos.
To merge everyone's, collect the exported JSON files; the deviation coordinates are
what's needed to re-snap a route segment.

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
