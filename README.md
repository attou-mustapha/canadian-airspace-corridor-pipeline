# Canadian Airspace 3D Corridor Validation Pipeline

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PostGIS 3D](https://img.shields.io/badge/PostGIS-3.4_3D-green.svg)](https://postgis.net/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-teal.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-assurance geospatial pipeline for UAV and autonomous flight trajectory validation against Canadian airspace restrictions (NAV CANADA designated airspace classes) and High-Resolution Digital Elevation Models (HRDEM / Natural Resources Canada).

---

## 🏛 Architecture & 3D Spatial Processing

```text
       [ UAV 3D Flight Plan ]
    (Waypoints: Lon, Lat, Altitude)
                  │
                  ▼
   [ Trajectory Interpolation Engine ]
 - 3D LineString interpolation
 - Altitude profile vs HRDEM terrain mesh
                  │
                  ▼
      [ PostGIS 3D Spatial Index ]
 - ST_3DIntersects & 3D Bounding Box
 - NAV CANADA CYR/CYA restricted zones
                  │
                  ▼
      [ Clearance & Conflict API ]
 - Dynamic clearance certification
 - Immediate conflict identification
```

---

## 🚀 Key Technical Highlights

* **3D Geometry Indexing:** Realizes genuine volumetric intersection queries with PostGIS 3D geometries (`PolygonZ`, `LineStringZ`, `ST_3DIntersects`).
* **HRDEM Altimetry Integration:** Evaluates above-ground-level (AGL) clearance by overlaying trajectories against RNCan high-resolution Canadian elevation models.
* **REST API & CLI:** Packaged with FastAPI for real-time mission planning integration, alongside a command-line interface for batch validation.

---

## 📦 Quickstart

```bash
# 1. Start PostGIS 3D container
docker compose up -d postgis

# 2. Install dependencies
pip install -e ".[dev]"

# 3. Launch validation API
uvicorn airspace_pipeline.api:app --reload --port 8000
```

---

## 🧪 Testing

```bash
pytest -v
```

---

## 👨‍💻 Author & Competency Profile

**Mustapha ATTOU**  
Senior Software Engineer & Geospatial Specialist  
*Algiers, Algeria — Open to Relocation (Canada)*  
- GitHub: [@attou-mustapha](https://github.com/attou-mustapha)
- LinkedIn: [attou-mustapha](https://www.linkedin.com/in/attou-mustapha)
- Email: [attou.mustapha.pro@gmail.com](mailto:attou.mustapha.pro@gmail.com)
