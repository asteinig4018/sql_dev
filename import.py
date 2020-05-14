import os
import csv

from config import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(DATABASE_URI,echo=True)
db = scoped_session(sessionmaker(bind = engine))

def import_planes():
    f = open("data/planes.dat")
    reader = csv.reader(f)
    for name, iata_code, icao_code in reader:
        db.execute("INSERT INTO planes (name, iata_code, icao_code) VALUES (:name, :iata_code, :icao_code)",
        {"name":name, "iata_code":iata_code, "icao_code":icao_code})
        print(f"Added plane {name} with IATA {iata_code} and ICAO {icao_code}.")

    db.commit()

def import_airlines():
    f = open("data/airlines.dat")
    reader = csv.reader(f)
    for ofid, name, alias, iata_code, icao_code, callsign, country, active in reader:
        db.execute("INSERT INTO airlines (ofid, name, alias, iata_code, icao_code, callsign, country, active) VALUES (:ofid, :name, :alias, :iata_code, :icao_code, :callsign, :country, :active)",
        {"ofid":ofid, "name":name, "alias":alias, "iata_code":iata_code, "icao_code":icao_code, "callsign":callsign, "country":country, "active":active})
        print(f"Added {name} with callsign {callsign} and alias {alias} of {country}.")

    db.commit()

def import_countries():
    f=open("data/countries.dat")
    reader = csv.reader(f)
    for name, iso_code, dafif_code in reader:
        db.execute("INSERT INTO countries (name, iso_code, dafif_code) VALUES (:name, :iso_code, :dafif_code)",
        {"name":name, "iso_code":iso_code, "dafif_code":dafif_code})
        print(f"Added {name} {iso_code}.")
    db.commit()

def import_routes():
    f=open("data/routes.dat")
    reader = csv.reader(f)
    for airline, airline_id, source_airport, source_airport_id, destination_airport, destination_airport_id, codeshare, stops, equipment in reader:
        db.execute("INSERT INTO routes (airline, airline_id, source_airport, source_airport_id, destination_airport, destination_airport_id, codeshare, stops, equipment) VALUES(:airline, :airline_id, :source_airport, :source_airport_id, :destination_airport, :destination_airport_id, :codeshare, :stops, :equipment)",
        {"airline":airline, "airline_id":airline_id, "source_airport":source_airport, "source_airport_id":source_airport_id, "destination_airport":destination_airport, "destination_airport_id":destination_airport_id, "codeshare":codeshare, "stops":stops, "equipment":equipment})
        print(f"Added a route from {source_airport} to {destination_airport} with {airline}.")
    db.commit()

def import_airports():
    f=open("data/airports.dat")
    reader = csv.reader(f)
    for in reader:
        db.execute(,
        {})
        print(f"")
    db.commit()


def main():
    #import_planes()
    #import_airlines()
    #import_countries()
    import_routes()


if __name__ == "__main__":
    main()
