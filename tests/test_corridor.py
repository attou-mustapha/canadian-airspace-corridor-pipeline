from airspace_pipeline.corridor_validator import FlightCorridorValidator

def test_corridor_validation_structure():
    validator = FlightCorridorValidator()
    waypoints = [
        (-73.5673, 45.5017, 120.0),
        (-73.6000, 45.5200, 140.0),
        (-73.6500, 45.5400, 180.0)
    ]
    res = validator.validate_trajectory_clearance(waypoints, safety_buffer_m=30.0)
    assert "is_valid" in res
    assert res["trajectory_points"] == 3
    assert res["safety_buffer_meters"] == 30.0
