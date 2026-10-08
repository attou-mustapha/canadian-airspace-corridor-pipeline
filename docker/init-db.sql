CREATE EXTENSION IF NOT EXISTS postgis;

CREATE SCHEMA IF NOT EXISTS airspace;

CREATE TABLE IF NOT EXISTS airspace.restricted_zones (
    zone_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    class VARCHAR(10) NOT NULL,
    lower_limit_m DOUBLE PRECISION NOT NULL,
    upper_limit_m DOUBLE PRECISION NOT NULL,
    geom geometry(PolygonZ, 4326) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_restricted_zones_3d ON airspace.restricted_zones USING GIST (geom);
