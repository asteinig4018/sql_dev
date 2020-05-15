CREATE TABLE airports(
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    city VARCHAR,
    country VARCHAR,
    iata_code VARCHAR,
    icao_code VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    altitude INTEGER,
    timezone FLOAT,
    dst VARCHAR,
    tz_type VARCHAR,
    source VARCHAR
);