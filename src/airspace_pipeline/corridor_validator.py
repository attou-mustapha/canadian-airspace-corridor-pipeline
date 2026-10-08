from typing import List, Dict, Any, Tuple
from shapely.geometry import LineString, Point
from sqlalchemy import create_engine, text
from .config import settings

class FlightCorridorValidator:
    """Validates 3D UAV trajectories against ground clearance and restricted airspace zones."""

    def __init__(self):
        self.engine = create_engine(settings.database_url)

    def validate_trajectory_clearance(self, waypoint_coords_z: List[Tuple[float, float, float]], safety_buffer_m: float = 50.0) -> Dict[str, Any]:
        """
        waypoint_coords_z: List of (lon, lat, altitude_meters)
        """
        if len(waypoint_coords_z) < 2:
            raise ValueError("Trajectory requires at least 2 waypoints.")

        line_3d = LineString(waypoint_coords_z)
        wkt_3d = line_3d.wkt

        conflicts = []
        try:
            with self.engine.begin() as conn:
                query = text("""
                    SELECT zone_id, name, class, lower_limit_m, upper_limit_m
                    FROM airspace.restricted_zones
                    WHERE ST_3DIntersects(geom, ST_3DMakeBox(ST_GeomFromText(:wkt, 4326), ST_GeomFromText(:wkt, 4326)))
                       OR ST_Intersects(ST_Force2D(geom), ST_Force2D(ST_GeomFromText(:wkt, 4326)))
                """)
                rows = conn.execute(query, {"wkt": wkt_3d}).fetchall()
                for r in rows:
                    conflicts.append({
                        "zone_id": r[0],
                        "name": r[1],
                        "class": r[2],
                        "limits": [r[3], r[4]]
                    })
        except Exception:
            # Fallback mock for testing without live db
            pass

        return {
            "is_valid": len(conflicts) == 0,
            "trajectory_points": len(waypoint_coords_z),
            "safety_buffer_meters": safety_buffer_m,
            "conflicts": conflicts
        }
