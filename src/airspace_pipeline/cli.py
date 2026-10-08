import click
import json
from .corridor_validator import FlightCorridorValidator

@click.group()
def main():
    """Canadian 3D Airspace & Flight Corridor Validation CLI."""
    pass

@main.command()
@click.option("--waypoints-json", required=True, help="JSON file with 3D coordinates [[lon, lat, alt]]")
def validate(waypoints_json):
    with open(waypoints_json) as f:
        pts = json.load(f)
    validator = FlightCorridorValidator()
    res = validator.validate_trajectory_clearance([tuple(p) for p in pts])
    click.echo(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
