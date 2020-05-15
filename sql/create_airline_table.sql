CREATE TABLE airlines (
    id SERIAL PRIMARY KEY,
    ofid INTEGER NOT NULL,
    name VARCHAR NOT NULL,
    alias VARCHAR,
    iata_code VARCHAR,
    icao_code VARCHAR,
    callsign VARCHAR,
    country VARCHAR,
    active VARCHAR
);