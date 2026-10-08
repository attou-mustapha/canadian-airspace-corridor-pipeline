from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Tuple
from .corridor_validator import FlightCorridorValidator

app = FastAPI(title="Canadian Airspace 3D Corridor Validation API", version="0.1.0")
validator = FlightCorridorValidator()

class TrajectoryRequest(BaseModel):
    waypoints: List[Tuple[float, float, float]] # (lon, lat, alt_m)
    safety_buffer_m: float = 50.0

@app.get("/health")
def health():
    return {"status": "ok", "service": "airspace-corridor-validator"}

@app.post("/api/v1/validate-corridor")
def validate_corridor(req: TrajectoryRequest):
    if len(req.waypoints) < 2:
        raise HTTPException(status_code=400, detail="At least 2 waypoints required.")
    return validator.validate_trajectory_clearance(req.waypoints, req.safety_buffer_m)
