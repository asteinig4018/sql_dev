CREATE TABLE routes(
    id SERIAL PRIMARY KEY,
    airline VARCHAR,
    airline_id INTEGER,
    source_airport VARCHAR,
    source_airport_id INTEGER,
    destination_airport VARCHAR,
    destination_airport_id INTEGER,
    codeshare VARCHAR,
    stops INTEGER,
    equipment VARCHAR
);