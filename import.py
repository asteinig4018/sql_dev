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

def main():
    import_planes()

if __name__ == "__main__":
    main()
